// Cho biết lượt truy cập có từ Việt Nam hay không, để trang chỉ gợi ý tiếng Anh cho khách ở nước ngoài.
// Chỉ trả về đúng/sai. Không lưu IP, không lưu quốc gia, không ghi nhật ký.
export async function onRequestGet({ request }) {
  const c = request.cf && request.cf.country;
  const vn = c ? c === 'VN' : null;
  return new Response(JSON.stringify({ vn }), {
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'private, no-store' },
  });
}
