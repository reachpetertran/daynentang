// API trang Chia sẻ của daynentang.com
// - GET: trả về các bài đã duyệt và được phép công khai.
// - POST: nhận bài mới, luôn ở trạng thái "chờ duyệt".
// Không lưu địa chỉ IP, email, số điện thoại hay bất kỳ dấu vết nào của người gửi.

const KINDS = new Set(['kho-khan', 'y-tuong', 'ket-qua', 'gop-y']);
const VIS = new Set(['cong-khai-ten', 'cong-khai-an-danh', 'rieng-tu']);
const SLUG = /^[a-z0-9-]{1,40}$/;
const AGES = /^[0-9 ,]{0,20}$/;

const json = (data, status = 200, extra = {}) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', ...extra },
  });

const clean = (v, max) => (typeof v === 'string' ? v.replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max) : '');

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const course = url.searchParams.get('course') || '';
  const lesson = url.searchParams.get('lesson') || '';
  const limit = Math.min(parseInt(url.searchParams.get('limit') || '30', 10) || 30, 50);
  const where = ["status = 'da-duyet'", "visibility != 'rieng-tu'"];
  const args = [];
  if (course && SLUG.test(course)) { where.push('course = ?'); args.push(course); }
  if (lesson && SLUG.test(lesson)) { where.push('lesson = ?'); args.push(lesson); }
  const sql = `SELECT id, substr(created_at,1,10) AS ngay, course, lesson, kind, body,
      CASE WHEN visibility = 'cong-khai-ten' THEN display_name ELSE NULL END AS ten,
      region, child_ages, reply
    FROM posts WHERE ${where.join(' AND ')} ORDER BY id DESC LIMIT ?`;
  args.push(limit);
  try {
    const { results } = await env.DB.prepare(sql).bind(...args).all();
    return json({ ok: true, posts: results }, 200, { 'cache-control': 'public, max-age=60' });
  } catch (e) {
    return json({ ok: false, error: 'Không đọc được dữ liệu. Vui lòng thử lại sau.' }, 500);
  }
}

export async function onRequestPost({ request, env }) {
  if (!(request.headers.get('content-type') || '').includes('application/json')) {
    return json({ ok: false, error: 'Định dạng không hợp lệ.' }, 415);
  }
  let d;
  try { d = await request.json(); } catch { return json({ ok: false, error: 'Dữ liệu không hợp lệ.' }, 400); }

  // Chống thư rác đơn giản: ô bẫy phải trống, và người gửi đã ở trên trang ít nhất 5 giây.
  if (d.website) return json({ ok: true });
  const opened = Number(d.t);
  if (!opened || Date.now() - opened < 5000) {
    return json({ ok: false, error: 'Bạn gửi hơi nhanh. Vui lòng đợi vài giây rồi gửi lại.' }, 429);
  }
  if (d.dong_y !== true) return json({ ok: false, error: 'Bạn cần đồng ý với điều khoản chia sẻ.' }, 400);

  const course = SLUG.test(d.course || '') ? d.course : 'chung';
  const lesson = SLUG.test(d.lesson || '') ? d.lesson : 'chung';
  const kind = KINDS.has(d.kind) ? d.kind : null;
  const visibility = VIS.has(d.visibility) ? d.visibility : null;
  const body = clean(d.body, 3000);
  const name = visibility === 'cong-khai-ten' ? clean(d.display_name, 40) : '';
  const region = clean(d.region, 40);
  const ages = clean(d.child_ages, 20);

  if (!kind || !visibility) return json({ ok: false, error: 'Vui lòng chọn loại chia sẻ và chế độ hiển thị.' }, 400);
  if (body.length < 10) return json({ ok: false, error: 'Nội dung quá ngắn (ít nhất 10 ký tự).' }, 400);
  if (visibility === 'cong-khai-ten' && !name) return json({ ok: false, error: 'Vui lòng nhập tên hiển thị, hoặc chọn ẩn danh.' }, 400);
  if (!AGES.test(ages)) return json({ ok: false, error: 'Tuổi con chỉ gồm số và dấu phẩy, ví dụ: 2, 7.' }, 400);

  try {
    const r = await env.DB.prepare(
      `INSERT INTO posts (created_at, course, lesson, kind, body, visibility, display_name, region, child_ages)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
    ).bind(new Date().toISOString(), course, lesson, kind, body, visibility, name || null, region || null, ages || null).run();
    return json({ ok: true, id: r.meta && r.meta.last_row_id }, 201, { 'cache-control': 'no-store' });
  } catch (e) {
    return json({ ok: false, error: 'Chưa lưu được. Vui lòng thử lại sau.' }, 500);
  }
}
