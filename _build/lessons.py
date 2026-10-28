from common import page, HELP_BOX, PRINT_ROW

BASE = '/khoa-hoc/gia-dinh-2-8/tuan-1/'
JOURNAL = '''<div class="table-wrap journal"><table><tbody>
<tr><th class="w38">Con làm được gì</th><td></td></tr>
<tr><th>Con thích gì</th><td></td></tr>
<tr><th>Cần sửa gì</th><td></td></tr>
</tbody></table></div>'''

def sec(n, title, body):
    return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'

def lesson(slug, code, title, strand, desc, meta, sections, prev=None, nxt=None):
    navl = f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else '<span></span>'
    navr = f'<a href="{nxt[0]}">{nxt[1]} →</a>' if nxt else '<span></span>'
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="/khoa-hoc/gia-dinh-2-8/">Gia đình 2–8 tuổi</a> · Tuần 1 · {code}</p>
<h1>{title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{PRINT_ROW}
{''.join(sections)}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau">{navl}{navr}</nav>
</div>'''
    page(BASE + slug + '/', f'{code} – {title}', desc, body, current='/gia-dinh/')

T1 = BASE + 't1-minh-tu-lam-duoc/'
K1 = BASE + 'k1-noi-hay-chim/'
G1 = BASE + 'g1-noi-that-long-nhe/'

# ---------- T1 ----------
lesson('t1-minh-tu-lam-duoc', 'T1', 'Mình tự làm được', 'Thói quen',
 'Bài 1 khóa Gia đình 2–8 tuổi: con tự làm việc buổi sáng, con nhỏ tự cất đồ chơi. Có hướng dẫn cho mẹ dạy theo từng phút.',
 ['Mạch A – Thói quen (Ngón cái)', 'Tuần 1, buổi 1', '20–30 phút'],
 [
 sec(1,'Mục tiêu','''<ul>
<li><strong>Con lớn (khoảng 7 tuổi):</strong> tự kể đủ 4 bước của một việc buổi sáng và chọn 1 việc tự làm trong tuần.</li>
<li><strong>Con nhỏ (khoảng 2 tuổi):</strong> tự cất 3 món đồ chơi vào rổ khi được nhắc một lần.</li></ul>'''),
 sec(2,'Chuẩn bị (5 phút)','''<ul>
<li>1 tờ giấy A4, bút sáp loại to. Không dùng bút có nắp nhỏ khi con nhỏ ở gần.</li>
<li>1 cái rổ và vài món đồ chơi to của con nhỏ.</li>
<li>Băng dính hoặc nam châm tủ lạnh loại to để dán bảng.</li></ul>'''),
 sec(3,'Mở đầu (2 phút)','<p>Giơ ngón cái lên và hỏi: "Ngón này giúp mình cầm được đồ. Sáng nay con tự làm được việc gì rồi?" Cả nhà cùng giơ ngón cái khi ai đó kể một việc.</p>'),
 sec(4,'Hoạt động chính','''<h3>Con lớn (15–20 phút)</h3><ol>
<li><strong>Khởi động "Bố bảo"</strong> (3 phút): chỉ làm theo khi câu bắt đầu bằng "Bố bảo". Ví dụ: "Bố bảo chạm mũi", rồi "Chạm tai" (không làm).</li>
<li><strong>Trò "Người máy"</strong> (5 phút): bố làm người máy, chỉ làm đúng từng lời con nói. Con hướng dẫn bố mặc áo khoác. Bố cố tình làm sai khi con nói thiếu bước.</li>
<li><strong>Vẽ "Bảng buổi sáng"</strong> (7 phút): con vẽ 4–5 ô, mỗi ô một việc: dậy, đánh răng, mặc đồ, ăn sáng, xếp cặp.</li>
<li><strong>Chọn việc</strong> (3 phút): con khoanh tròn 1 việc trước đây bố mẹ hay làm hộ. Tuần này con tự làm việc đó.</li>
<li>Dán bảng ở chỗ con nhìn thấy mỗi sáng.</li></ol>
<h3>Con nhỏ (5–10 phút)</h3><ol>
<li>Đặt 3 món đồ chơi to trên sàn, rổ ở gần.</li>
<li>Hát chậm: "Đồ chơi về nhà, về nhà, về nhà" và làm mẫu cất 1 món.</li>
<li>Mời con cất 2 món còn lại. Con cất xong thì cả nhà giơ ngón cái.</li>
<li>Nếu con không muốn, cầm tay con cất cùng 1 món rồi dừng.</li></ol>'''),
 sec(5,'Câu hỏi trò chuyện','''<ol>
<li>Lúc người máy làm sai, con thấy thế nào? Vì sao nó sai?</li>
<li>Việc nào con muốn tự làm mà chưa ai cho thử?</li>
<li>Nếu con tự làm và chưa được, con sẽ làm gì tiếp?</li></ol>'''),
 sec(6,'An toàn','''<ul>
<li>Con nhỏ: chỉ dùng đồ chơi và bút không lọt lõi giấy vệ sinh. Cất nắp bút, sáp gãy vụn.</li>
<li>Trò "Người máy": dọn chỗ rộng, không có cạnh bàn sắc gần đó.</li></ul>'''),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)','''<div class="mom">
<p><em>Mẹ chỉ cần: 1 tờ giấy, bút sáp to, 1 cái rổ. Tổng 20 phút.</em></p><ol>
<li><strong>Phút 0–2 – Mở đầu.</strong> Mẹ giơ ngón cái: "Sáng nay con tự làm được gì?" Con kể việc nào, cả nhà giơ ngón cái.</li>
<li><strong>Phút 2–5 – "Mẹ bảo".</strong> Chơi như trên, đổi "Bố bảo" thành "Mẹ bảo". Con lớn có thể làm người ra lệnh 1 lượt.</li>
<li><strong>Phút 5–12 – Vẽ bảng.</strong> Bỏ trò "Người máy" nếu mẹ mệt. Con vẽ 4–5 việc buổi sáng lên giấy.</li>
<li><strong>Phút 12–15 – Chọn việc.</strong> Con khoanh 1 việc sẽ tự làm tuần này. Mẹ dán bảng lên tủ lạnh.</li>
<li><strong>Phút 15–20 – Con nhỏ cất đồ chơi.</strong> Hát "Đồ chơi về nhà", mẹ cất mẫu 1 món, con cất 2 món.</li></ol>
<p><strong>Khi con làm được:</strong> "Con tự cố gắng làm đó!" Khen sự cố gắng, không khen "giỏi quá".</p>
<p><strong>Khi con làm chưa được:</strong> "Chưa được thôi. Con muốn thử lại hay muốn mẹ chỉ một bước?"</p>
<p><strong>Khi con mệt hoặc quấy:</strong> dừng ở bước đang làm. Bảng vẽ dở vẫn dán lên được.</p>
<p><strong>Nhắn bố 1 câu:</strong> con chọn việc gì để tự làm.</p></div>'''),
 sec(8,'Ôn lại','''<ul>
<li><strong>Sau 1 ngày:</strong> sáng hôm sau, chỉ vào bảng: "Hôm nay việc nào con tự làm?" Con tự đánh dấu.</li>
<li><strong>Sau 1 tuần:</strong> đếm số ngày con tự làm việc đã chọn. Chọn tiếp việc thứ hai nếu con muốn.</li></ul>'''),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn','''<ul>
<li><span class="label">[Đã xác nhận]</span> Trò kiểu "Simon says" có trong gợi ý hoạt động cho trẻ 5–7 tuổi của <a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Harvard Center on the Developing Child</a>.</li>
<li><span class="label">[Đánh giá chuyên môn]</span> Bảng việc buổi sáng và trò "Người máy" do daynentang.com thiết kế, chưa có nghiên cứu riêng.</li>
<li><span class="label">[Suy luận]</span> Khen sự cố gắng thay vì khen "giỏi". Các can thiệp "tư duy phát triển" chỉ có hiệu quả rất nhỏ, nên chúng tôi dùng kèm hành động cụ thể như thử lại, đổi cách.</li>
<li><span class="label">[Đánh giá chuyên môn]</span> Mẹo lõi giấy vệ sinh là cách thử nhanh tại nhà, không thay thế tiêu chuẩn đồ chơi.</li></ul>'''),
 ], prev=None, nxt=(K1,'K1 – Nổi hay chìm?'))

# ---------- K1 ----------
lesson('k1-noi-hay-chim', 'K1', 'Nổi hay chìm?', 'Khoa học',
 'Bài khoa học bằng tay: con đoán rồi thử vật nổi hay chìm trong chậu nước. Có hướng dẫn an toàn nước và phần cho mẹ dạy.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 1, buổi 2', '25–30 phút'],
 [
 sec(1,'Mục tiêu','''<ul>
<li><strong>Con lớn:</strong> đoán trước rồi thử 8 vật, ghi kết quả, và nói được "vật nặng chưa chắc đã chìm".</li>
<li><strong>Con nhỏ:</strong> thả vật vào nước và nói hoặc chỉ "nổi" hay "chìm".</li></ul>'''),
 sec(2,'Chuẩn bị (5 phút)','''<ul>
<li>1 chậu nhựa lớn, nước sâu khoảng 10–15 cm. Đặt trên khăn tắm cũ ở sàn.</li>
<li>8 vật to (đều to hơn lõi giấy vệ sinh): thìa inox lớn, chai nhựa rỗng đậy nắp, chai nhựa đầy nước đậy nắp, quả cam còn vỏ, khối gỗ đồ chơi, bát nhựa, hòn đá cỡ nắm tay, khối Lego/Duplo to.</li>
<li>1 tờ giấy kẻ 3 cột: Vật · Con đoán · Kết quả.</li>
<li>1 cái rổ nhựa để vớt đồ.</li></ul>'''),
 sec(3,'Mở đầu (2 phút)','<p>Cầm thìa inox và chai nhựa rỗng: "Cái nào nặng hơn? Cái nào sẽ chìm?" Để con đoán, chưa nói đáp án.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại','''<h3>Con lớn (20–25 phút)</h3><ol>
<li><strong>Quan sát:</strong> con cầm từng vật, nói nó nặng hay nhẹ, cứng hay mềm, rỗng hay đặc.</li>
<li><strong>Đoán:</strong> con ghi "N" (nổi) hoặc "C" (chìm) vào cột "Con đoán" cho cả 8 vật.</li>
<li><strong>Thử:</strong> con thả từng vật, ghi kết quả. Đoán sai thì vẽ dấu hỏi, không gạch xóa.</li>
<li><strong>So sánh bất ngờ:</strong> đặt cạnh nhau chai rỗng và chai đầy nước. Hai chai giống nhau, vì sao chai đầy nước nằm thấp hơn hẳn?</li>
<li><strong>Thử thêm:</strong> thả bát nhựa cho nổi như thuyền. Con bỏ từng khối Lego vào bát. Đếm xem bao nhiêu khối thì bát chìm.</li>
<li><strong>Kể lại:</strong> con kể cho bố mẹ 1 điều làm con bất ngờ nhất.</li></ol>
<h3>Con nhỏ (5–10 phút)</h3><ol>
<li>Ngồi sát chậu; người lớn ngồi ngay cạnh, tay trong tầm với của con.</li>
<li>Đưa con từng vật: "Thả nào!" Nói theo: "Nổi!" hoặc "Chìm, xuống đáy rồi!"</li>
<li>Cho con vớt đồ bằng rổ nhựa.</li>
<li>Lặp lại vật con thích. Trẻ 2 tuổi thích lặp lại; đó là cách con học.</li></ol>'''),
 sec(5,'Câu hỏi trò chuyện','''<ol>
<li>Vật nào con đoán sai? Lần sau con sẽ nhìn gì để đoán?</li>
<li>Chai rỗng và chai đầy nước khác nhau ở đâu?</li>
<li>Ở nhà mình còn vật nào con muốn thử lần sau?</li></ol>'''),
 sec(6,'An toàn','''<ul>
<li>Người lớn ngồi sát, con nhỏ luôn trong tầm tay. Có chuông cửa hay điện thoại thì bế con theo.</li>
<li>Không để con lớn trông con nhỏ bên chậu nước.</li>
<li>Xong buổi: đổ hết nước ngay, úp chậu, cất chỗ con không với tới.</li>
<li>Lau sàn ướt ngay để không trượt ngã.</li>
<li>Mọi vật phải to hơn lõi giấy vệ sinh. Không dùng bi, nắp chai, pin, nam châm nhỏ.</li></ul>'''),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)','''<div class="mom">
<p><em>Mẹ chỉ cần: chậu nước, khăn tắm cũ, 5 vật (thìa inox, chai rỗng, chai đầy nước, quả cam, khối gỗ), giấy bút. Tổng 20 phút.</em></p>
<p><strong>Trước khi bắt đầu:</strong> mẹ đặt điện thoại xa, ngồi sát chậu. Nếu phải rời đi, mẹ dừng buổi và bế con nhỏ theo.</p><ol>
<li><strong>Phút 0–2 – Mở đầu.</strong> Mẹ giơ thìa và chai rỗng: "Cái nào sẽ chìm?" Con đoán, mẹ chưa trả lời.</li>
<li><strong>Phút 2–6 – Đoán.</strong> Con lớn ghi N hoặc C cho 5 vật. Con nhỏ ngồi xem, cầm thử từng vật.</li>
<li><strong>Phút 6–12 – Thử.</strong> Hai con thay phiên thả. Con nhỏ thả, con lớn ghi kết quả.</li>
<li><strong>Phút 12–15 – Bất ngờ.</strong> Thả chai rỗng và chai đầy nước cạnh nhau. Hỏi: "Sao hai chai khác nhau?"</li>
<li><strong>Phút 15–18 – Kể lại.</strong> Con lớn kể 1 điều bất ngờ. Mẹ chụp tờ ghi kết quả gửi bố (không chụp mặt con).</li>
<li><strong>Phút 18–20 – Dọn.</strong> Đổ nước ngay, úp chậu, lau sàn. Con lớn phụ lau.</li></ol>
<p><strong>Nếu con hỏi "vì sao" mà mẹ chưa chắc:</strong> "Mẹ cũng chưa biết. Mình ghi lại, tối hỏi bố nhé." Không cần trả lời đúng ngay.</p>
<p><strong>Một ý đơn giản để nói với con lớn:</strong> vật có nhiều không khí bên trong thường dễ nổi. Không phải cứ to hay nặng là chìm.</p>
<p><strong>Bỏ qua bước "Thử thêm"</strong> (Lego trong bát) nếu mẹ chỉ có một mình. Để dành cho buổi bố về.</p></div>'''),
 sec(8,'Ôn lại','''<ul>
<li><strong>Sau 1 ngày:</strong> lúc tắm, đưa con 1 vật mới (an toàn), hỏi "Nổi hay chìm?" trước khi thả.</li>
<li><strong>Sau 1 tuần:</strong> xem lại tờ ghi kết quả. Con đoán đúng bao nhiêu vật? Thử 3 vật mới con tự chọn.</li></ul>'''),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn','''<ul>
<li><span class="label">[Đã xác nhận]</span> Trẻ nhỏ có thể đuối nước chỉ với vài inch nước; luôn giữ trẻ trong tầm tay, đổ nước sau khi dùng, không để trẻ lớn trông trẻ nhỏ khi tắm (<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">CPSC, Hoa Kỳ</a>).</li>
<li><span class="label">[Đánh giá chuyên môn]</span> Kết quả từng vật (ví dụ quả cam) chúng tôi không đoán trước. Đó là việc con tự thử.</li>
<li><span class="label">[Đánh giá chuyên môn]</span> Câu "nhiều không khí thì dễ nổi" là cách nói đơn giản cho trẻ, chưa phải định nghĩa đầy đủ về lực đẩy.</li></ul>'''),
 ], prev=(T1,'T1 – Mình tự làm được'), nxt=(G1,'G1 – Nói thật, lòng nhẹ'))

# ---------- G1 ----------
lesson('g1-noi-that-long-nhe', 'G1', 'Nói thật, lòng nhẹ', 'Giá trị',
 'Bài giá trị trung thực với truyện "Khủng long Tí" và kỹ năng Dừng – Thở – Nói. Truyện khen người nói thật, không dọa.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 1, buổi 3', '20–30 phút'],
 [
 sec(1,'Mục tiêu','''<ul>
<li><strong>Con lớn:</strong> kể lại chuyện "Khủng long Tí" và tập nói câu nhận lỗi theo 3 bước: dừng – thở – nói.</li>
<li><strong>Con nhỏ:</strong> chỉ tay hoặc nói "con" khi được hỏi ai làm đổ tháp khối.</li></ul>'''),
 sec(2,'Chuẩn bị (5 phút)','''<ul>
<li>Câu chuyện bên dưới (in ra hoặc đọc trên giấy).</li>
<li>6–8 khối gỗ hoặc Duplo to, 1 gối ôm.</li>
<li>Một chỗ ngồi yên, tắt tivi.</li></ul>'''),
 sec(3,'Mở đầu (2 phút)','<p>"Có khi nào con làm đổ, làm vỡ gì đó chưa? Lúc đó trong bụng con thấy thế nào?" Nghe con nói, không nhận xét.</p>'),
 sec(4,'Hoạt động chính','''<h3>Câu chuyện: Khủng long Tí và chậu cây của bà</h3>
<blockquote class="story">
<p>Khủng long Tí thích chạy vòng quanh vườn nhà bà. Một hôm, Tí quẫy đuôi mạnh quá. Chậu cây hoa của bà đổ xuống, vỡ làm hai.</p>
<p>Tí đứng im. Bụng Tí thấy nặng như nuốt phải hòn đá. Tí nghĩ: "Hay mình chạy ra sau nhà, không ai biết đâu."</p>
<p>Nhưng Tí dừng lại. Tí hít một hơi thật sâu, rồi thở ra thật chậm. Tí đi vào nhà, nói nhỏ: "Bà ơi, cháu quẫy đuôi làm vỡ chậu cây rồi. Cháu xin lỗi bà."</p>
<p>Bà ôm Tí: "Cảm ơn cháu đã nói thật với bà. Chậu vỡ thì mình thay. Cháu nói thật thì bà rất vui."</p>
<p>Hai bà cháu cùng xúc đất sang chậu mới. Cây hoa vẫn tươi. Tí thấy bụng mình nhẹ tênh, như vừa đặt hòn đá xuống.</p>
</blockquote>
<p class="small muted">Truyện viết mới cho daynentang.com.</p>
<h3>Con lớn (15–20 phút)</h3><ol>
<li><strong>Nghe chuyện</strong> (4 phút): đọc chậm. Dừng ở đoạn Tí định chạy đi, hỏi: "Con nghĩ Tí sẽ làm gì?"</li>
<li><strong>Kể lại</strong> (4 phút): con kể lại chuyện bằng lời của con. Con có thể dùng gối ôm làm Tí.</li>
<li><strong>Tập Dừng – Thở – Nói</strong> (5 phút): bố mẹ nêu tình huống, con làm 3 bước. Ví dụ: "Con làm đổ nước ra bàn." Con: dừng, hít thở 1 lần, nói "Bố ơi, con làm đổ nước rồi."</li>
<li><strong>Đổi vai</strong> (4 phút): bố mẹ làm đổ "giả", con đóng vai bà. Con tập nói: "Cảm ơn bố đã nói thật."</li>
<li><strong>Luật nhà mình</strong> (2 phút): cùng nói to: "Nói thật thì được cảm ơn. Rồi mình cùng sửa."</li></ol>
<h3>Con nhỏ (5–10 phút)</h3><ol>
<li>Cùng con xây tháp 6 khối.</li>
<li>Cho con đẩy đổ tháp. Hỏi vui: "Ai làm đổ tháp nhỉ?"</li>
<li>Con chỉ tay hoặc nói "con". Cười: "Cảm ơn con đã nói! Mình xây lại nào."</li>
<li>Lặp lại 3–4 lần. Con nhỏ học câu "cảm ơn con đã nói" qua trò chơi.</li></ol>'''),
 sec(5,'Câu hỏi trò chuyện','''<ol>
<li>Lúc Tí định chạy đi, bụng Tí thấy thế nào? Lúc nói thật xong thì sao?</li>
<li>Bà làm gì khi Tí nói thật?</li>
<li>Nếu con làm vỡ đồ, con muốn bố mẹ nói gì với con?</li></ol>'''),
 sec(6,'An toàn','''<ul>
<li>Khối xây phải to hơn lõi giấy vệ sinh. Xây trên thảm, không xây cao quá đầu con nhỏ.</li>
<li>Bài này không dọa hay phạt. Nếu con kể một lỗi thật trong buổi học, cảm ơn con trước, sửa sau.</li></ul>'''),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)','''<div class="mom">
<p><em>Mẹ chỉ cần: câu chuyện in ra, 6 khối xây, 1 gối ôm. Tổng 20 phút. Nên dạy buổi tối trước giờ ngủ.</em></p><ol>
<li><strong>Phút 0–2 – Mở đầu.</strong> Mẹ hỏi: "Có lần nào con làm vỡ gì chưa?" Chỉ nghe, không nhắc lại lỗi cũ của con.</li>
<li><strong>Phút 2–6 – Đọc chuyện.</strong> Đọc chậm. Đến đoạn Tí định chạy đi, mẹ dừng và hỏi: "Con đoán Tí làm gì?"</li>
<li><strong>Phút 6–10 – Con nhỏ chơi tháp.</strong> Mẹ xây tháp, con nhỏ đẩy đổ. Mẹ hỏi "Ai làm đổ?", con chỉ, mẹ cảm ơn. Con lớn phụ xây lại.</li>
<li><strong>Phút 10–15 – Tập 3 bước.</strong> Mẹ nêu 2 tình huống: "Con làm rơi bát", "Con làm rách sách của em". Con lớn làm: dừng – thở – nói.</li>
<li><strong>Phút 15–18 – Đổi vai.</strong> Mẹ giả làm đổ đồ, con lớn đóng vai bà và nói: "Cảm ơn mẹ đã nói thật."</li>
<li><strong>Phút 18–20 – Luật nhà mình.</strong> Cả nhà nói: "Nói thật thì được cảm ơn. Rồi mình cùng sửa."</li></ol>
<p><strong>Điều quan trọng nhất:</strong> trong tuần này, khi con tự nhận lỗi thật, mẹ nói "cảm ơn con đã nói thật" trước. Rồi mới cùng con sửa.</p>
<p><strong>Tránh:</strong> dọa "nói dối thì mũi dài ra" hay "nói dối bị phạt". Truyện dọa không giúp trẻ nói thật hơn (xem nguồn).</p>
<p><strong>Nếu con lớn hỏi "mẹ có nói dối bao giờ không":</strong> trả lời thật, ngắn gọn. Ví dụ: "Có lúc mẹ cũng sợ. Nhưng nói thật xong mẹ thấy nhẹ lòng."</p>
<p><strong>Nhắn bố 1 câu:</strong> con thích đoạn nào trong chuyện.</p></div>'''),
 sec(8,'Ôn lại','''<ul>
<li><strong>Sau 1 ngày:</strong> trước giờ ngủ, hỏi con kể lại 1 câu trong chuyện Khủng long Tí.</li>
<li><strong>Sau 1 tuần:</strong> hỏi "Tuần này có lần nào con nói thật dù hơi sợ không?" Nếu có, cảm ơn con lần nữa.</li></ul>'''),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn','''<ul>
<li><span class="label">[Đã xác nhận]</span> Nghiên cứu 268 trẻ 3–7 tuổi: chỉ truyện có nhân vật được khen vì nói thật làm tăng việc trẻ nhận lỗi; truyện dọa hậu quả nói dối không hiệu quả hơn truyện không liên quan (Lee, Talwar et al., <em>Psychological Science</em>, 2014; <a href="https://www.psychologicalscience.org/news/releases/moral-tales-with-positive-outcomes-motivate-kids-to-be-honest.html">tóm tắt của APS</a>).</li>
<li><span class="label">[Đã xác nhận]</span> Khi đổi kết thúc truyện thành tiêu cực, hiệu quả biến mất; hiệu quả lâu dài chưa được kiểm chứng (cùng nguồn).</li>
<li><span class="label">[Suy luận]</span> "Cảm ơn trước, sửa sau" là cách áp dụng phát hiện trên vào gia đình; nghiên cứu không thử trực tiếp cách này.</li>
<li><span class="label">[Đánh giá chuyên môn]</span> Truyện "Khủng long Tí" viết mới hoàn toàn, chỉ mượn ý tưởng "khen người nói thật".</li></ul>'''),
 ], prev=(K1,'K1 – Nổi hay chìm?'), nxt=('/khoa-hoc/gia-dinh-2-8/','Về trang khóa học'))
