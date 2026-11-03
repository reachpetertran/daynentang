# Khóa C1 – bài 2–8 và công cụ "Bản đồ an toàn của tôi".
# Tệp này được exec() trong c1.py, dùng chung lesson, sec, ul, ol, lb, TALK, nguồn.
TOOL = '/cong-cu/ban-do-an-toan/'
GAFF = '<a href="https://ojp.gov/ncjrs/virtual-library/abstracts/evaluating-effectiveness-school-bullying-prevention-programs">Gaffney, Ttofi &amp; Farrington 2019, <em>Aggression and Violent Behavior</em></a>'
VOH = '<a href="https://voh.com.vn/phap-luat/cong-an-canh-bao-3-chieu-bat-coc-online-nham-vao-hoc-sinh-sinh-vien-625691.html">Bộ Công an (Cục A05) tại Cyber Day 2025, VOH đưa tin 12/10/2025</a>'
AAP = '<a href="https://healthychildren.org/English/family-life/Media/Pages/How-to-Make-a-Family-Media-Use-Plan.aspx">AAP – Kế hoạch dùng thiết bị gia đình</a>'
RUOU = '<a href="https://luatvietnam.vn/an-ninh-trat-tu/luat-phong-chong-tac-hai-cua-ruou-bia-2019-so-44-2019-qh14-175006-d1.html">Luật Phòng, chống tác hại của rượu, bia số 44/2019/QH14, Điều 5 khoản 3</a>'
TLDT = '<a href="https://baovanhoa.vn/thoi-su/quoc-hoi-ra-nghi-quyet-ve-cam-thuoc-la-dien-tu-thuoc-la-nung-nong-tu-nam-2025-113542.html">Nghị quyết Quốc hội ngày 30/11/2024</a>'
WHOVN = '<a href="https://www.who.int/vietnam/vi/news/feature-stories/item/in-viet-nam--low-cost-water-safety-actions-help-reduce-child-drowning-deaths">WHO Việt Nam, 12/2023</a>'
BURN = '<a href="https://www.schn.health.nsw.gov.au/kids-health-hub/safety-and-injury-prevention/burns-and-fire/first-aid-burns">Sydney Children\'s Hospitals Network</a>'
SAC = '<a href="https://lsvn.vn/canh-bao-4-nguyen-nhan-chu-yeu-gay-chay-no-xe-dien-gia-tang-a165609.html">Cảnh sát PCCC Phú Thọ, 11/2025</a>'
SO = '<a href="https://thuvienphapluat.vn/hoi-dap-phap-luat/111-113-114-115-la-so-dien-thoai-gi-138013545.html">Thư viện Pháp luật (tra 28/10/2026)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'

L.update({
 '2': (2, 'ranh-gioi-co-the', 'Bài 2', 'Cơ thể của mình, ranh giới của mình'),
 '3': (3, 'an-toan-tren-mang', 'Bài 3', 'An toàn trên mạng'),
 '4': (4, 'nhan-ra-lua-dao', 'Bài 4', 'Nhận ra lừa đảo và dụ dỗ'),
 '5': (5, 'ban-be-va-bat-nat', 'Bài 5', 'Bạn bè và bắt nạt'),
 '6': (6, 'noi-khong-van-giu-ban', 'Bài 6', 'Nói "không" mà vẫn giữ bạn'),
 '7': (7, 'an-toan-duong-nuoc-dien', 'Bài 7', 'An toàn đường, nước, điện'),
 '8': (8, 'cam-xuc-va-khi-can-giup', 'Bài 8', 'Cảm xúc và khi nào cần giúp'),
})
ORDER[:] = list(L)

def selftab(items, a='Hôm nay', b='Sau 7 ngày'):
    rows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in items)
    return ('<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')
def lines(labels):
    rows = ''.join(f'<tr><th class="w38">{x}</th><td></td></tr>' for x in labels)
    return f'<div class="table-wrap journal"><table><tbody>{rows}</tbody></table></div>'
def quiz(items, head=('Tình huống (giả định)', 'Bạn chọn', 'Gợi ý đáp án')):
    rows = ''.join(f'<tr><td>{q}</td><td></td><td class="small">{a}</td></tr>' for q, a in items)
    return (f'<div class="table-wrap"><table><thead><tr><th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')
def std(k, desc, goals, prep, read, do, talk, safety, selfq, adult, src):
    lesson(k, desc, [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (5 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Nói với người lớn (5 phút)', talk),
        sec(6, 'An toàn', ul(safety)),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho người lớn đồng hành', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))])

# ======================= BÀI 2 =======================
std('2', 'Khóa Lớn lên an toàn, bài 2: vùng riêng tư, bí mật vui và bí mật phải kể, bàn tay 5 người lớn tin cậy.',
 ['Phân biệt được <strong>bí mật vui</strong> và <strong>bí mật phải kể</strong>.',
  'Viết tên <strong>5 người lớn tin cậy</strong> lên bàn tay của mình.',
  'Tập nói <strong>"Dừng lại"</strong> rõ ràng, nhìn thẳng.'],
 ['Nên đọc bài này cùng một người lớn tin cậy.', f'In trang 1 của <a href="{TOOL}">Bản đồ an toàn của tôi</a>, hoặc vẽ bàn tay ra giấy.'],
 ['<strong>Cơ thể bạn là của bạn.</strong> Bạn có quyền quyết định ai được ôm, được chạm vào bạn. Kể cả người thân.',
  '<strong>Vùng riêng tư</strong> là phần cơ thể đồ bơi che lại. Không ai được chạm, nhìn hay chụp ảnh vùng đó của bạn.',
  '<strong>Ngoại lệ:</strong> khi khám bệnh, bác sĩ có thể cần khám. Lúc đó nên có bố mẹ hoặc người lớn tin cậy ở bên.',
  '<strong>Luật này đi hai chiều.</strong> Bạn cũng không chạm, không chụp, không gửi ảnh vùng riêng tư của người khác.',
  '<strong>Bí mật vui</strong> làm người khác vui và sẽ được kể sớm, như quà sinh nhật bất ngờ.',
  '<strong>Bí mật phải kể</strong> làm bạn sợ, buồn, khó chịu. Hoặc ai đó bảo "đừng kể bố mẹ". Hoặc liên quan đến cơ thể.',
  '<strong>Người làm bạn khó chịu</strong> có thể là người lạ, cũng có thể là người quen. Điều đó không thay đổi quy tắc.',
  '<strong>Kể ra không phải lỗi của bạn.</strong> Dù bạn đã lỡ giữ bí mật lâu, dù được tặng quà, kể lúc nào cũng được.'],
 '<p><strong>Bài 1: phân loại.</strong> Đọc từng tình huống, viết "vui" hay "phải kể".</p>' + quiz([
   ('Bạn và em chuẩn bị thiệp bất ngờ cho mẹ.', 'Vui. Sẽ được kể vào ngày sinh nhật.'),
   ('Một người lớn tặng quà rồi dặn "đừng nói với bố mẹ nhé".', 'Phải kể. Người lớn tốt không bắt trẻ giấu bố mẹ.'),
   ('Có người nhắn tin xin ảnh bạn mặc ít đồ.', 'Phải kể. Không gửi, chụp màn hình, chặn.'),
   ('Bạn thân kể bạn ấy thích một bạn cùng lớp.', 'Giữ được. Nhưng nếu bạn ấy gặp nguy hiểm thì phải kể.'),
   ('Ai đó chạm vào bạn làm bạn khó chịu, rồi bảo "chuyện của hai ta".', 'Phải kể ngay. Không phải lỗi của bạn.')]) +
 '<p><strong>Bài 2: bàn tay.</strong> Viết 5 người lớn tin cậy lên 5 ngón tay. Ít nhất 1 người không sống cùng nhà, như thầy cô hay y tế trường.</p>' +
 '<p><strong>Bài 3: tập nói.</strong> Đứng thẳng, nhìn vào mắt, nói to: <em>"Dừng lại. Tôi không thích."</em> Tập 3 lần.</p>',
 ol(['Đưa bàn tay đã viết cho người lớn xem. Hỏi: "Bố/mẹ đồng ý là người con có thể kể không?"',
     'Hỏi người lớn: "Nếu con kể chuyện khó, bố/mẹ sẽ làm gì?"',
     'Cùng chọn chỗ cất bàn tay: trong cặp, dán trong tủ, hoặc chụp lưu trong máy của bố mẹ.']),
 [TALK, 'Người đầu tiên không tin bạn? Kể tiếp người thứ hai, thứ ba. Đừng dừng lại.',
  'Đừng tự đối mặt với người làm hại bạn. Hãy để người lớn lo việc đó.'],
 ['Tôi nói được khác nhau giữa bí mật vui và bí mật phải kể', 'Tôi có tên 5 người lớn tin cậy', 'Tôi nói được "Dừng lại. Tôi không thích." rõ ràng'],
 ['Nên đọc bài này cùng con. Dùng đúng tên bộ phận cơ thể, giọng bình thường.',
  'Hứa với con: con kể gì, bố mẹ cũng không giận con. Giữ lời hứa đó.',
  'Nếu con kể chuyện bị xâm hại: tin con, giữ bình tĩnh, cảm ơn con. Không hỏi dồn nhiều lần; gọi 111 để được hướng dẫn.',
  'Không bắt con ôm, hôn người khác khi con không muốn, kể cả họ hàng.',
  f'Xem thêm khóa bố mẹ <a href="{G4}">Gia đình có con 10–14</a>, bài 2 Lắng nghe để con muốn kể.'],
 [lb('Đã xác nhận', f'Tổng hợp 24 thử nghiệm với 5.802 trẻ: chương trình dạy ở trường về phòng xâm hại giúp trẻ hiểu biết hơn, có hành vi tự bảo vệ hơn và kể ra nhiều hơn ({COCH}).'),
  lb('Đã xác nhận', f'Cùng tổng hợp đó: ít dấu hiệu chương trình gây lo lắng; chưa rõ chương trình có giảm số vụ xâm hại hay không ({COCH}).'),
  lb('Đánh giá chuyên môn', f'Khái niệm vùng riêng tư, bí mật vui và bí mật phải kể là ý tưởng phổ biến trong giáo dục phòng xâm hại; cách viết do daynentang.com soạn. Chủ đề theo {ITGSE}.'),
  lb('Suy luận', 'Các chương trình gốc dạy ở trường, có thầy cô. Đọc tại nhà cùng người lớn có thể cho kết quả khác.')])

# ======================= BÀI 3 =======================
std('3', 'Khóa Lớn lên an toàn, bài 3: giữ kín thông tin cá nhân, mật khẩu, ảnh, người lạ trên mạng, quy tắc Dừng – Chặn – Chụp – Kể.',
 ['Kiểm tra <strong>cài đặt riêng tư</strong> cùng người lớn, đủ 6 mục trong phiếu.',
  'Nói được <strong>4 dấu hiệu</strong> của người lạ nguy hiểm trên mạng.',
  'Nhớ quy tắc <strong>Dừng – Chặn – Chụp – Kể</strong>.'],
 [f'Trang 2 của <a href="{TOOL}">Bản đồ an toàn của tôi</a>.', 'Phần Làm cần điện thoại của bạn hoặc của bố mẹ, làm cùng người lớn.'],
 ['<strong>Thông tin luôn giữ kín:</strong> địa chỉ nhà, trường và lớp, số điện thoại, mật khẩu, lịch đi lại hằng ngày.',
  '<strong>Mật khẩu:</strong> dài, mỗi ứng dụng một mật khẩu khác nhau. Không cho bạn bè biết. Bố mẹ có thể giữ một bản.',
  '<strong>Ảnh:</strong> ảnh đã gửi đi có thể bị lưu, bị chuyển tiếp. Đã đăng rồi thì rất khó lấy lại.',
  '<strong>Không bao giờ gửi</strong> ảnh hay video mặc ít đồ, dù người kia là ai, dù họ hứa xóa.',
  '<strong>Bốn dấu hiệu người lạ nguy hiểm:</strong> khen quá mức, tặng quà hay tiền; bảo giữ bí mật với bố mẹ; xin ảnh riêng tư; rủ gặp riêng.',
  '<strong>Người trên mạng</strong> có thể nói dối về tuổi, tên, ảnh. Bạn không thể chắc họ là ai.',
  '<strong>Gặp điều xấu:</strong> dừng trả lời, chặn, chụp màn hình làm bằng chứng, kể cho người lớn. Đừng xóa tin nhắn.',
  '<strong>Ngủ và màn hình:</strong> để điện thoại ngoài phòng ngủ ban đêm giúp bạn ngủ đủ giờ.'],
 '<p><strong>Phiếu kiểm tra riêng tư.</strong> Cùng người lớn mở từng ứng dụng bạn dùng. Đánh dấu ✓ khi xong.</p>' +
 '<div class="table-wrap"><table><thead><tr><th>Việc cần kiểm tra</th><th>Ứng dụng 1</th><th>Ứng dụng 2</th><th>Ứng dụng 3</th></tr></thead><tbody>' +
 ''.join(f'<tr><td>{x}</td><td></td><td></td><td></td></tr>' for x in [
   'Tài khoản để chế độ riêng tư', 'Chỉ bạn bè đã biết mới nhắn được', 'Tắt chia sẻ vị trí',
   'Ảnh đại diện không lộ trường, đồng phục', 'Mật khẩu mạnh, không trùng', 'Biết nút chặn và báo cáo ở đâu']) +
 '</tbody></table></div><p class="small muted">Mỗi ứng dụng có quy định tuổi riêng. Người lớn đọc quy định đó cùng bạn.</p>',
 ol(['Cho người lớn xem phiếu đã làm.', 'Hỏi: "Nếu con gặp chuyện xấu trên mạng và kể, con có bị mất điện thoại không?" Thống nhất câu trả lời.',
     'Cùng viết giờ dùng máy và chỗ sạc máy ban đêm vào trang 2 của Bản đồ an toàn.']),
 [TALK, 'Bị đe dọa bằng ảnh, bị đòi tiền: không trả tiền, không gửi thêm gì. Giữ bằng chứng, kể ngay người lớn, gọi 111.',
  'Không bao giờ đi gặp người chỉ quen trên mạng mà không có bố mẹ đi cùng.'],
 ['Tôi đã kiểm tra cài đặt riêng tư cùng người lớn', 'Tôi nói được 4 dấu hiệu người lạ nguy hiểm', 'Tôi nhớ Dừng – Chặn – Chụp – Kể'],
 ['Hứa trước: con kể chuyện xấu trên mạng thì con không bị phạt vì đã kể. Nếu tịch thu máy ngay, lần sau con có thể giấu.',
  'Bố mẹ cũng giữ quy tắc: hỏi ý con trước khi đăng ảnh có con.',
  f'Xem thêm khóa bố mẹ <a href="{G4}">Gia đình có con 10–14</a>, bài 5 Điện thoại, mạng xã hội.'],
 [lb('Đã xác nhận', f'Kế hoạch dùng thiết bị gia đình gồm chỗ không màn hình, chọn nội dung và bố mẹ làm gương ({AAP}).'),
  lb('Đã xác nhận', f'Giờ ngủ khuyến nghị theo tuổi ({AASM}).'),
  lb('Đánh giá chuyên môn', 'Bốn dấu hiệu người lạ nguy hiểm là tóm tắt ở mức chung, không đầy đủ. Phiếu kiểm tra riêng tư và quy tắc Dừng – Chặn – Chụp – Kể do daynentang.com soạn.'),
  lb('Suy luận', 'Để máy ngoài phòng ngủ giúp ngủ đủ giờ là suy luận từ khuyến nghị về giờ ngủ và giờ không màn hình.')])

# ======================= BÀI 4 =======================
std('4', 'Khóa Lớn lên an toàn, bài 4: năm dấu hiệu lừa đảo, "bắt cóc online", việc nhẹ lương cao, quy tắc Dừng – Hỏi – Kể.',
 ['Nhận ra <strong>5 dấu hiệu lừa đảo</strong> trong tình huống giả định.',
  'Dùng quy tắc <strong>Dừng – Hỏi – Kể</strong> trong 4 tình huống.',
  'Biết rằng <strong>kể ra vẫn đúng</strong>, kể cả khi đã lỡ làm theo.'],
 ['Giấy, bút.', f'Trang 2 của <a href="{TOOL}">Bản đồ an toàn của tôi</a>.'],
 ['<strong>Kẻ lừa đảo nhắm cả vào học sinh.</strong> Năm 2025, Bộ Công an cảnh báo các chiêu "bắt cóc online" nhắm vào học sinh, sinh viên.',
  '<strong>Chiêu 1: dọa.</strong> Kẻ gian giả danh công an hay cơ quan nhà nước, nói bạn vi phạm pháp luật, rồi ép bạn làm theo.',
  '<strong>Chiêu 2: làm thân lâu.</strong> Kẻ gian kết bạn, trò chuyện thân thiết nhiều tuần, rồi dần điều khiển suy nghĩ của bạn.',
  '<strong>Chiêu 3: dụ.</strong> Kẻ gian hứa việc làm, tiền, nổi tiếng để lấy ảnh hay video riêng tư, rồi khống chế bạn.',
  '<strong>Năm dấu hiệu:</strong> vội, phải làm ngay; dọa, làm bạn sợ; bắt giữ bí mật; đòi tiền, ảnh, mã OTP, mật khẩu; hứa quá hời.',
  '<strong>Một dấu hiệu là đủ</strong> để dừng lại. Không cần chờ đủ cả năm.',
  '<strong>Quy tắc vàng:</strong> dù người kia nói họ là ai, nếu bắt bạn giấu bố mẹ, đừng làm theo.',
  '<strong>Đã lỡ làm theo?</strong> Vẫn kể ngay. Kể sớm giúp người lớn xử lý dễ hơn. Bạn là người bị lừa, không phải người có lỗi.'],
 '<p><strong>Tìm dấu hiệu.</strong> Mỗi tình huống có những dấu hiệu nào (1–5)? Bạn sẽ làm gì?</p>' + quiz([
   ('Có người gọi video, mặc áo công an, nói bạn liên quan vụ án. Họ bảo bạn đến khách sạn một mình và không được nói với ai.', 'Dấu hiệu 1, 2, 3. Tắt máy, kể ngay bố mẹ.'),
   ('Một tài khoản lạ mời làm "cộng tác viên", mỗi ngày 500.000 đồng, chỉ cần nộp trước 200.000 đồng.', 'Dấu hiệu 4, 5. Không nộp tiền, hỏi người lớn.'),
   ('Bạn quen trên mạng 2 tháng, rất tốt với bạn. Giờ xin ảnh riêng tư, dặn đừng kể ai.', 'Dấu hiệu 3, 4. Không gửi, chụp màn hình, chặn, kể.'),
   ('Tin nhắn báo bạn trúng thưởng điện thoại, bấm link và nhập mã OTP gửi về máy bố mẹ trong 5 phút.', 'Dấu hiệu 1, 4, 5. Không bấm, không gửi mã.')],
   ('Tình huống (giả định)', 'Dấu hiệu bạn thấy', 'Gợi ý đáp án')),
 ol(['Đọc cho người lớn nghe một tình huống bạn thấy khó nhất. Hỏi người lớn sẽ làm gì.',
     'Thống nhất: nếu có người tự xưng công an, ngân hàng, nhà trường gọi cho bạn, bạn làm gì?',
     'Hỏi người lớn: "Bố/mẹ từng gặp lừa đảo chưa?"']),
 [TALK, 'Bị ép đi đâu một mình, bị dọa, bị đòi tiền chuộc: gọi 113 hoặc kể ngay người lớn gần nhất.',
  'Không bao giờ gửi mã OTP, mật khẩu, ảnh giấy tờ của bố mẹ cho ai.'],
 ['Tôi nói được 5 dấu hiệu lừa đảo', 'Tôi tìm đúng dấu hiệu trong ít nhất 3/4 tình huống', 'Tôi biết kể ra vẫn đúng dù đã lỡ làm theo'],
 ['Nói với con: nếu con bị lừa, bố mẹ sẽ giúp con trước, không trách trước.',
  'Thống nhất một "câu hỏi gia đình" chỉ nhà mình biết, để kiểm tra khi ai đó gọi nhân danh người nhà.',
  'Tình huống trong bài là giả định, dựa trên các chiêu cơ quan công an đã cảnh báo.'],
 [lb('Đã xác nhận', f'Ba chiêu "bắt cóc online" nhắm vào học sinh, sinh viên: đe dọa, giả danh cơ quan nhà nước; thao túng cảm xúc qua làm thân lâu; dụ bằng việc làm, tiền, danh tiếng để lấy ảnh riêng tư ({VOH}).'),
  lb('Đã xác nhận', f'Khuyến cáo cùng nguồn: bố mẹ đồng hành, trò chuyện thường xuyên để con sẵn sàng chia sẻ; học sinh nhận biết dấu hiệu dụ dỗ, đe dọa ({VOH}).'),
  lb('Đánh giá chuyên môn', 'Năm dấu hiệu, quy tắc Dừng – Hỏi – Kể và các tình huống giả định do daynentang.com soạn.')])

# ======================= BÀI 5 =======================
std('5', 'Khóa Lớn lên an toàn, bài 5: bắt nạt trực tiếp và trên mạng, bốn vai, ba câu nói của người giúp, báo cho ai.',
 ['Nói được <strong>bắt nạt là gì</strong> và khác trêu đùa ở đâu.',
  'Có <strong>3 câu nói</strong> của người giúp, viết bằng lời của mình.',
  'Viết tên <strong>2 người lớn ở trường</strong> để báo khi có bắt nạt.'],
 ['Giấy, bút. Nếu được, một bạn hay người lớn để đóng vai.'],
 ['<strong>Bắt nạt</strong> là cố ý làm tổn thương người khác, lặp đi lặp lại, khi người kia khó tự bảo vệ.',
  '<strong>Trêu đùa</strong> là cả hai cùng vui. Khi một người buồn, xin dừng mà vẫn bị làm tiếp, đó không còn là đùa.',
  '<strong>Các dạng bắt nạt:</strong> đánh, đẩy, lấy đồ; chửi, đặt biệt danh xấu; cô lập, tung tin đồn; nhắn tin, đăng ảnh để chế giễu.',
  '<strong>Bốn vai:</strong> người bị bắt nạt, người bắt nạt, người đứng xem, người giúp. Người đứng xem thường đông nhất.',
  '<strong>Người giúp không cần đánh nhau.</strong> Không cười theo, không chia sẻ, đứng cạnh bạn bị bắt nạt, báo người lớn.',
  '<strong>Nếu bạn bị bắt nạt:</strong> nói "Dừng lại" rồi rời đi. Đi cùng bạn bè. Kể người lớn. Đó không phải lỗi của bạn.',
  '<strong>Bắt nạt trên mạng:</strong> không trả lời, chụp màn hình, chặn, báo cáo, kể người lớn.',
  '<strong>Nếu chính bạn đã bắt nạt ai:</strong> dừng lại, xin lỗi thật lòng, nhờ người lớn giúp sửa. Ai cũng có thể thay đổi.'],
 '<p><strong>Viết 3 câu bằng lời của bạn.</strong></p>' +
 lines(['Câu nói với người bắt nạt', 'Câu nói với bạn bị bắt nạt', 'Câu nói với người lớn']) +
 '<p><strong>Đóng vai (giả định).</strong> Trong giờ ra chơi, một nhóm bạn giấu cặp của một bạn và cười. Bạn đi ngang qua. Tập nói 3 câu.</p>' +
 '<p><strong>Người lớn ở trường tôi có thể báo:</strong> 1. ………………… 2. …………………</p>',
 ol(['Kể cho người lớn nghe 3 câu bạn đã viết.', 'Hỏi: "Hồi bằng tuổi con, bố/mẹ có thấy bắt nạt không? Bố/mẹ đã làm gì?"',
     'Thống nhất: nếu con bị bắt nạt, con muốn bố mẹ làm gì trước, và không làm gì.']),
 [TALK, 'Không đánh trả, không tự trả thù. Có thể làm việc tệ hơn và bạn bị phạt.',
  'Bị đe dọa, bị đánh, bị chặn đường: tìm người lớn gần nhất ngay. Nguy hiểm tức thì gọi 113.'],
 ['Tôi nói được khác nhau giữa bắt nạt và trêu đùa', 'Tôi có 3 câu nói của người giúp', 'Tôi biết 2 người lớn ở trường để báo'],
 ['Khi con kể bị bắt nạt: nghe hết, tin con, không bảo con "kệ nó" hay "đánh lại".',
  'Cùng con ghi lại sự việc: ngày, nơi, ai, chuyện gì. Liên hệ giáo viên chủ nhiệm, bình tĩnh.',
  'Nếu con là người bắt nạt: giữ bình tĩnh, tìm hiểu lý do, giúp con sửa lỗi và xin lỗi.'],
 [lb('Đã xác nhận', f'Phân tích gộp cập nhật cho thấy chương trình phòng bắt nạt ở trường giúp giảm cả hành vi bắt nạt và tình trạng bị bắt nạt ({GAFF}).'),
  lb('Cần kiểm chứng', 'Mức giảm cụ thể (tỉ lệ phần trăm) trong phân tích gộp trên: chúng tôi mới đọc tóm tắt, chưa đọc toàn văn.'),
  lb('Đánh giá chuyên môn', 'Định nghĩa bắt nạt, bốn vai và ba câu nói là mô tả phổ biến, viết lại đơn giản. Bài tập do daynentang.com soạn.'),
  lb('Suy luận', 'Các chương trình gốc làm cả trường cùng tham gia. Một học sinh tự học có thể không đạt kết quả tương tự.')])

# ======================= BÀI 6 =======================
std('6', 'Khóa Lớn lên an toàn, bài 6: áp lực bạn bè, rượu bia, thuốc lá điện tử, ma túy; bốn cách nói không và mật mã gọi đón.',
 ['Tập đủ <strong>4 cách nói không</strong> trong 3 tình huống đóng vai.',
  'Có <strong>câu mật mã gọi đón</strong>, thống nhất với bố mẹ.',
  'Nói được luật Việt Nam về rượu bia và thuốc lá điện tử với người dưới 18 tuổi.'],
 [f'Trang 3 (thẻ mật mã) của <a href="{TOOL}">Bản đồ an toàn của tôi</a>.', 'Một người lớn để đóng vai.'],
 ['<strong>Muốn được nhóm bạn chấp nhận</strong> là bình thường ở tuổi bạn. Vì vậy, nói "không" cần tập trước.',
  '<strong>Luật Việt Nam:</strong> cấm bán, cung cấp rượu bia cho người dưới 18 tuổi. Thuốc lá điện tử, thuốc lá nung nóng bị cấm từ năm 2025.',
  '<strong>Ma túy</strong> bị pháp luật cấm. Ai mời bạn thứ lạ, kẹo lạ, nước lạ: không nhận, rời đi, kể người lớn.',
  '<strong>Cách 1: "Không, cảm ơn."</strong> Ngắn, rõ, không cần giải thích.',
  '<strong>Cách 2: đưa lý do.</strong> "Bố mẹ mình sắp đón." "Mình có trận bóng sáng mai."',
  '<strong>Cách 3: đổi chủ đề.</strong> "Thôi, đi ăn kem đi." Rủ bạn làm việc khác.',
  '<strong>Cách 4: rời đi và gọi mật mã.</strong> Mật mã là một câu bình thường đã thống nhất, như "Mẹ ơi con quên áo khoác".',
  '<strong>Bạn thật</strong> sẽ tôn trọng lời "không" của bạn. Người cứ ép mãi thì chưa phải bạn tốt.'],
 '<p><strong>Đóng vai (giả định).</strong> Người lớn làm "người rủ". Bạn dùng mỗi cách ít nhất một lần.</p>' + quiz([
   ('Ở sinh nhật bạn, mấy anh lớn mời thử thuốc lá điện tử "vị trái cây".', 'Cách 1 rồi cách 3.'),
   ('Bạn thân rủ trốn tiết để đi quán game.', 'Cách 2 hoặc cách 3.'),
   ('Ở một buổi tụ tập, mọi người uống bia, ép bạn "một ly thôi". Bạn thấy không ổn.', 'Cách 4: rời đi, nhắn mật mã.')],
   ('Tình huống (giả định)', 'Cách bạn dùng', 'Gợi ý')) +
 '<p><strong>Câu mật mã của tôi:</strong> "…………………………………………"</p>',
 ol(['Cùng người lớn chọn câu mật mã. Lưu vào điện thoại. Viết vào thẻ.',
     'Hỏi người lớn hứa: "Khi con nhắn mật mã, bố/mẹ đến đón ngay và nói chuyện sau, được không?"',
     'Chọn thêm một người lớn dự phòng có thể đón khi bố mẹ vắng.']),
 [TALK, 'Bạn bè có biểu hiện lạ sau khi uống, hút hay dùng gì đó (lơ mơ, khó thở, co giật): gọi 115 ngay, ở lại bên bạn.',
  'Không nhận đồ ăn, nước uống từ người lạ hay để ly nước không có người trông.'],
 ['Tôi tập đủ 4 cách nói không', 'Tôi có câu mật mã, bố mẹ đã đồng ý', 'Tôi biết luật về rượu bia, thuốc lá điện tử cho người dưới 18 tuổi'],
 ['Giữ lời hứa mật mã: đến đón ngay, không tra hỏi lúc đó, nói chuyện sau khi bình tĩnh.',
  'Nói rõ quan điểm nhà mình về rượu bia, thuốc lá, kèm lý do.',
  f'Xem thêm khóa bố mẹ <a href="{G4}">Gia đình có con 10–14</a>, bài 6 Bạn bè, rượu bia, thuốc lá điện tử.'],
 [lb('Đã xác nhận', f'{RUOU}: nghiêm cấm bán, cung cấp, khuyến mại rượu bia cho người chưa đủ 18 tuổi. Hiệu lực 01/01/2020; tra cứu 28/10/2026.'),
  lb('Đã xác nhận', f'Quốc hội thông qua ngày 30/11/2024 việc cấm sản xuất, kinh doanh, sử dụng thuốc lá điện tử, thuốc lá nung nóng từ năm 2025 ({TLDT}).'),
  lb('Cần kiểm chứng', 'Số hiệu nghị quyết về thuốc lá điện tử và văn bản xử phạt: bài báo nguồn không ghi; chúng tôi chưa đọc văn bản gốc.'),
  lb('Đã xác nhận', f'{SFP} có phần tập từ chối áp lực bạn bè; thử nghiệm ở Mỹ cho thấy con ít bắt đầu uống rượu hơn. Bài này chỉ mượn ý tưởng.'),
  lb('Đánh giá chuyên môn', 'Bốn cách nói không, mật mã gọi đón và tình huống giả định do daynentang.com soạn.')])

# ======================= BÀI 7 =======================
std('7', 'Khóa Lớn lên an toàn, bài 7: mũ bảo hiểm, qua đường, an toàn ở gần nước, điện và cháy, checklist ra khỏi nhà.',
 ['Có <strong>checklist ra khỏi nhà</strong> và dùng đủ 7 ngày.',
  'Nói được <strong>3 quy tắc</strong> khi ở gần nước.',
  'Biết làm gì khi <strong>bị bỏng</strong> và khi <strong>có cháy</strong>.'],
 [f'Trang 4 của <a href="{TOOL}">Bản đồ an toàn của tôi</a>.', 'Mũ bảo hiểm của bạn, để kiểm tra quai.'],
 ['<strong>Mũ bảo hiểm:</strong> luôn đội khi ngồi xe máy, đi xe đạp điện, xe đạp. Cài quai, vừa đầu, không lắc.',
  '<strong>Qua đường:</strong> dừng ở mép, nhìn hai phía, nghe tiếng xe, rồi đi thẳng, không chạy. Không vừa đi vừa xem điện thoại.',
  '<strong>Đi xe đạp:</strong> đi sát lề phải, không đi hàng ba, không buông tay, có đèn khi trời tối.',
  '<strong>Nước:</strong> mỗi năm ở Việt Nam có khoảng 2.000 trẻ em tử vong do đuối nước. Biết bơi vẫn có thể đuối nước.',
  '<strong>Ba quy tắc nước:</strong> không bơi một mình, luôn có người lớn; không xuống ao, hồ, sông, suối lạ; không đùa đẩy nhau gần nước.',
  '<strong>Thấy người đuối nước:</strong> gọi to người lớn, gọi 115. Ném vật nổi như phao, can nhựa rỗng. Không tự nhảy xuống cứu.',
  '<strong>Điện:</strong> không chạm ổ điện, dây hở khi tay ướt. Không sạc xe điện qua đêm. Dùng sạc chính hãng.',
  '<strong>Bỏng:</strong> xả nước mát đang chảy 20 phút. Không bôi đá, kem đánh răng. <strong>Cháy:</strong> ra ngoài trước, gọi 114, không quay lại lấy đồ.'],
 '<p><strong>Checklist ra khỏi nhà.</strong> Chọn 5 mục quan trọng nhất với bạn, đánh dấu mỗi lần đi ra ngoài.</p>' +
 '<div class="table-wrap"><table><thead><tr><th class="w38">Trước khi đi</th>' + ''.join(f'<th>{d}</th>' for d in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']) + '</tr></thead><tbody>' +
 ''.join(f'<tr><td>{x}</td>' + '<td></td>' * 7 + '</tr>' for x in [
   'Báo người lớn: đi đâu, với ai, về lúc mấy giờ', 'Mũ bảo hiểm, cài quai', 'Điện thoại có pin, nhớ câu mật mã',
   'Nhớ số điện thoại của bố hoặc mẹ', 'Nước uống, áo mưa', 'Về trễ thì gọi báo trước']) + '</tbody></table></div>' +
 '<p><strong>Kiểm tra mũ:</strong> đội mũ, cài quai. Lắc đầu mạnh. Mũ không xoay, không tụt là vừa.</p>',
 ol(['Cho người lớn xem checklist. Thống nhất giờ về và cách báo khi về trễ.', 'Cùng nhau đi một vòng nhà: tìm 1 chỗ điện, 1 chỗ nước có thể nguy hiểm.',
     'Hỏi: "Khu nhà mình, chỗ nước nào nguy hiểm nhất?"']),
 ['Gần nước luôn có người lớn trông. Mặc áo phao khi đi thuyền, đò.',
  'Không tự sửa đồ điện, không leo cột điện, không thả diều gần đường dây điện.', TALK],
 ['Tôi dùng checklist ra khỏi nhà', 'Tôi nói được 3 quy tắc ở gần nước', 'Tôi biết sơ cứu bỏng và làm gì khi có cháy'],
 ['Cho con học bơi ở nơi có người dạy và người cứu hộ. Biết bơi không thay cho người lớn trông.',
  'Kiểm tra mũ bảo hiểm của con: đúng cỡ, có quai, không nứt vỡ.',
  'Kiểm tra chỗ sạc xe điện, ổ điện trong nhà. Xem thêm khóa Nhà gọn, nhà an toàn.'],
 [lb('Đã xác nhận', f'Mỗi năm khoảng 2.000 trẻ em Việt Nam tử vong do đuối nước ({WHOVN}).'),
  lb('Đã xác nhận', f'Sơ cứu bỏng: nước mát đang chảy 20 phút; không dùng đá, kem, kem đánh răng ({BURN}).'),
  lb('Đã xác nhận', f'Sạc xe điện: không sạc qua đêm, dùng sạc chính hãng, không sạc gần đồ dễ cháy ({SAC}). Số 114 cứu hỏa, 115 cấp cứu ({SO}).'),
  lb('Cần kiểm chứng', 'Điều khoản cụ thể về mũ bảo hiểm cho trẻ em trong Luật Trật tự, an toàn giao thông đường bộ 2024 và nghị định xử phạt: chúng tôi chưa đọc được văn bản gốc.'),
  lb('Đánh giá chuyên môn', 'Quy tắc qua đường, đi xe đạp, ở gần nước, cách kiểm tra mũ và checklist là lời khuyên an toàn chung, do daynentang.com soạn.')])

# ======================= BÀI 8 =======================
std('8', 'Khóa Lớn lên an toàn, bài 8: gọi tên cảm xúc, cách tự bình tĩnh, dấu hiệu cần nhờ giúp, Bản đồ an toàn của tôi.',
 ['Gọi tên được <strong>6 cảm xúc</strong> và chọn <strong>2 cách tự bình tĩnh</strong>.',
  'Nói được <strong>dấu hiệu</strong> khi cần nhờ người lớn giúp.',
  'Hoàn thành <strong>Bản đồ an toàn của tôi</strong> và cất ở chỗ dễ tìm.'],
 [f'In toàn bộ <a href="{TOOL}">Bản đồ an toàn của tôi</a>.', 'Lấy lại bàn tay 5 người (bài 2) và câu mật mã (bài 6).'],
 ['<strong>Cảm xúc nào cũng bình thường:</strong> vui, buồn, giận, sợ, lo, xấu hổ. Việc mình làm với cảm xúc mới quan trọng.',
  '<strong>Gọi tên cảm xúc:</strong> "Mình đang giận vì bị nói oan." Nói ra giúp người khác hiểu bạn.',
  '<strong>Cách tự bình tĩnh:</strong> thở chậm 1 phút, đi bộ, uống nước, nghe nhạc, viết ra giấy, nói với người tin cậy.',
  '<strong>Nền của cảm xúc:</strong> ngủ đủ giờ, vận động khoảng 60 phút mỗi ngày, ăn đều, có bạn để chơi.',
  '<strong>Vài ngày buồn, giận</strong> rồi qua là bình thường.',
  '<strong>Cần nhờ giúp khi:</strong> buồn hay lo kéo dài nhiều tuần; mất ngủ, bỏ ăn; không muốn gặp ai, không muốn đi học.',
  '<strong>Cần nhờ giúp ngay khi:</strong> bạn nghĩ đến cái chết hay muốn làm đau bản thân. Nói ngay với người lớn tin cậy.',
  '<strong>Nhờ giúp là dũng cảm,</strong> không phải yếu đuối. Người lớn, thầy cô, bác sĩ đều có thể giúp.'],
 '<p><strong>Bài 1: nhật ký cảm xúc 3 ngày.</strong> Mỗi tối viết một cảm xúc mạnh nhất trong ngày và bạn đã làm gì.</p>' +
 lines(['Ngày 1: cảm xúc, việc tôi làm', 'Ngày 2: cảm xúc, việc tôi làm', 'Ngày 3: cảm xúc, việc tôi làm']) +
 '<p><strong>Bài 2: hai cách tự bình tĩnh của tôi:</strong> 1. ………………… 2. …………………</p>' +
 f'<p><strong>Bài 3: Bản đồ an toàn.</strong> Điền đủ các trang của <a href="{TOOL}">Bản đồ an toàn của tôi</a>.</p>',
 ol(['Cùng người lớn đọc lại Bản đồ an toàn. Người lớn ký tên.', 'Cùng lưu các số khẩn cấp vào điện thoại.',
     'Mỗi người kể một điều mình học được sau 8 tuần.']),
 ['Nếu bạn đang nghĩ đến cái chết hay muốn làm đau bản thân: nói ngay với người lớn ở gần, hoặc gọi 115.',
  'Đường dây Ngày Mai 096 306 1414 hỗ trợ người đang trầm cảm và người thân. Tổng đài 111 hỗ trợ trẻ em, miễn phí, 24/7.', TALK],
 ['Tôi gọi tên được 6 cảm xúc', 'Tôi có 2 cách tự bình tĩnh', 'Tôi đã hoàn thành Bản đồ an toàn của tôi'],
 ['Con nói về cái chết hay làm đau bản thân: ở bên con, không để con một mình, gọi 115 hoặc đưa con đến cơ sở y tế.',
  'Dấu hiệu kéo dài nhiều tuần: đưa con gặp bác sĩ hoặc chuyên gia tâm lý. Đừng chê con yếu đuối.',
  'Cùng con chấm phiếu tự đánh giá cuối khóa trong Bản đồ an toàn. So với tuần 1.'],
 [lb('Đã xác nhận', f'Trẻ 5–17 tuổi nên vận động vừa đến mạnh khoảng 60 phút mỗi ngày ({PA}). Giờ ngủ theo tuổi ({AASM}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}). Tổng đài 111 bảo vệ trẻ em, miễn phí, 24/7 ({T111}). Kiểm tra lại mỗi quý.'),
  lb('Đánh giá chuyên môn', 'Danh sách dấu hiệu cần nhờ giúp là tóm tắt chung, không dùng để chẩn đoán. Khóa không thay thế bác sĩ hay nhà tâm lý.'),
  lb('Đánh giá chuyên môn', 'Nhật ký cảm xúc, cách tự bình tĩnh và Bản đồ an toàn do daynentang.com soạn.')])

# ======================= CÔNG CỤ =======================
fingers = ''.join(f'<tr><th class="w38">Ngón {i}</th><td class="tall">Tên: ……………… · Số: ……………</td></tr>' for i in range(1, 6))
priv = ''.join(f'<tr><td>{x}</td><td></td></tr>' for x in ['Tài khoản riêng tư', 'Chỉ bạn bè đã biết nhắn được', 'Tắt vị trí', 'Ảnh đại diện không lộ trường', 'Mật khẩu mạnh, không trùng', 'Biết nút chặn, báo cáo'])
FINAL = ['Tôi làm đều 5 việc chăm cơ thể', 'Tôi có 5 người lớn tin cậy', 'Tôi phân biệt bí mật vui và bí mật phải kể', 'Cài đặt riêng tư đã kiểm tra',
         'Tôi nhận ra dấu hiệu lừa đảo', 'Tôi có 3 câu nói khi thấy bắt nạt', 'Tôi có câu mật mã gọi đón', 'Tôi dùng checklist ra khỏi nhà', 'Tôi có 2 cách tự bình tĩnh']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Bản đồ an toàn của tôi', 'Trang in cho khóa Lớn lên an toàn: 5 người lớn tin cậy, quy tắc an toàn, mật mã gọi đón, số khẩn cấp, checklist, tự đánh giá.',
f'''
<h1>Bản đồ an toàn của tôi</h1>
<p>Dùng cho khóa <a href="{U}">Lớn lên an toàn (10–14)</a>. Chỉ để in, trang không lưu dữ liệu của bạn.
Cất bản đã điền ở nhà. Không chụp đăng lên mạng. Không ghi mật khẩu thật vào đây.</p>
{PRINT_ROW}
<h2>1. Bàn tay 5 người lớn tin cậy (bài 2)</h2>
<div class="table-wrap"><table><tbody>{fingers}</tbody></table></div>
<p>Người thứ nhất chưa nghe? Kể tiếp người thứ hai.</p>
<h2>2. Quy tắc của tôi (bài 2–4)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Khi gặp chuyện lạ, khó</th><td>Dừng · Nghĩ · Chọn việc an toàn · Kể người lớn</td></tr>
<tr><th>Gặp điều xấu trên mạng</th><td>Dừng trả lời · Chặn · Chụp màn hình · Kể</td></tr>
<tr><th>Nghi bị lừa</th><td>Dừng · Hỏi người lớn · Kể, dù đã lỡ làm theo</td></tr>
<tr><th>Bí mật phải kể</th><td>Làm tôi sợ, khó chịu · Bị bảo "đừng kể bố mẹ" · Liên quan cơ thể</td></tr>
</tbody></table></div>
<p><strong>Phiếu kiểm tra riêng tư (bài 3):</strong></p>
<div class="table-wrap"><table><thead><tr><th>Việc cần kiểm tra</th><th>Đã xong ✓</th></tr></thead><tbody>{priv}</tbody></table></div>
<h2>3. Thẻ mật mã gọi đón (bài 6)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Câu mật mã</th><td class="tall">"……………………………………"</td></tr>
<tr><th>Gọi ai</th><td>Bố …………… · Mẹ …………… · Người dự phòng ……………</td></tr>
<tr><th>Lời hứa của người lớn</th><td>Đến đón ngay, không tra hỏi lúc đó, nói chuyện sau khi bình tĩnh.</td></tr>
</tbody></table></div>
<h2>4. Số khẩn cấp và checklist ra khỏi nhà (bài 7–8)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">111</th><td>Bảo vệ trẻ em, miễn phí, 24/7</td></tr>
<tr><th>113</th><td>Công an, khi nguy hiểm ngay lúc đó</td></tr>
<tr><th>114</th><td>Cứu hỏa</td></tr>
<tr><th>115</th><td>Cấp cứu y tế</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<p><strong>Trước khi ra khỏi nhà:</strong> báo đi đâu, với ai, về mấy giờ · mũ bảo hiểm cài quai · điện thoại có pin · nhớ số bố mẹ · về trễ gọi báo.</p>
<p><strong>Hai cách tự bình tĩnh của tôi:</strong> 1. ………………… 2. …………………</p>
<h2>5. Tự đánh giá (tuần 1 và tuần 8)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 8</th></tr></thead><tbody>{frows}</tbody></table></div>
<p>Người lớn đồng hành ký: ………………… &nbsp; Ngày: ……/……/……</p>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán.</p>
{HELP_BOX}
''', current='/cong-cu/')
