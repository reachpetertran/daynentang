import os
from common import page, HELP_BOX, PRINT_ROW, ROOT, SITE

# ---------- Công cụ ----------
page('/cong-cu/', 'Công cụ', 'Công cụ in miễn phí cho gia đình: bảng quan sát tiến bộ của con, bảng thói quen 7 ngày, phiếu giá trị, biên bản họp gia đình.',
'''
<h1>Công cụ</h1>
<p class="lead">Công cụ in được, dùng ngay. Không cần tài khoản, không lưu dữ liệu của bạn.</p>
<div class="grid">
<a class="card" href="/cong-cu/bang-quan-sat/"><span class="tag">Có thể in</span><h3>Bảng quan sát 0–1–2</h3><p>Theo dõi tiến bộ của con ở tuần 0, 6 và 12 của khóa Gia đình 2–8.</p></a>
<a class="card" href="/cong-cu/bang-thoi-quen/"><span class="tag">Có thể in</span><h3>Bảng thói quen 7 ngày</h3><p>Con tự đánh dấu việc mình tự làm mỗi ngày.</p></a>
<a class="card" href="/cong-cu/phieu-gia-tri/"><span class="tag">Có thể in</span><h3>Phiếu giá trị</h3><p>20 thẻ giá trị, bảng việc làm, nội quy, tự đánh giá. Cho khóa Giá trị nhà mình.</p></a>
<a class="card" href="/cong-cu/bien-ban-hop-gia-dinh/"><span class="tag">Có thể in</span><h3>Biên bản họp gia đình</h3><p>Năm phần của buổi họp 15 phút mỗi tuần.</p></a>
<a class="card" href="/cong-cu/bang-thu-chi/"><span class="tag">Có thể in</span><h3>Bảng thu chi</h3><p>Ghi chi 7 ngày, bảng tháng, quỹ khẩn cấp, danh sách nợ. Cho khóa Tiền nhà mình.</p></a>
<a class="card" href="/cong-cu/hu-ba-ngan/"><span class="tag">Có thể in</span><h3>Hũ ba ngăn</h3><p>Nhãn hũ, thanh mục tiêu, tranh cần – muốn cho con.</p></a>
<a class="card" href="/cong-cu/phieu-ra-soat-nha/"><span class="tag">Có thể in</span><h3>Phiếu rà soát nhà</h3><p>An toàn từng phòng, phòng cháy, bảo trì. Cho khóa Nhà gọn, nhà an toàn.</p></a>
<a class="card" href="/cong-cu/so-tay-cong-dong/"><span class="tag">Có thể in</span><h3>Sổ tay cộng đồng</h3><p>Phỏng vấn ông bà, người có thể nhờ, kế hoạch màn hình. Cho khóa Gia đình và cộng đồng.</p></a>
<a class="card" href="/cong-cu/so-tay-vo-chong/"><span class="tag">Có thể in</span><h3>Sổ tay vợ chồng</h3><p>Mở lời nhẹ, tạm dừng, họp vợ chồng. Cho khóa Vợ chồng đồng lòng.</p></a>
<a class="card" href="/cong-cu/thoa-thuan-gia-dinh/"><span class="tag">Có thể in</span><h3>Thỏa thuận gia đình</h3><p>Thỏa thuận, kế hoạch thiết bị, mật mã gọi đón. Cho khóa Gia đình có con 10–14.</p></a>
<a class="card" href="/cong-cu/nhat-ky-giao-dap/"><span class="tag">Có thể in</span><h3>Nhật ký giao và đáp</h3><p>5 phút mỗi ngày, kế hoạch khi con khóc. Cho khóa Gia đình 0–2 tuổi.</p></a>
<a class="card" href="/cong-cu/bang-viec-nha/"><span class="tag">Có thể in</span><h3>Bảng việc nhà</h3><p>Danh sách việc có phần nghĩ, Ai lo việc gì, bảng việc của con. Cho khóa Việc nhà chia đều.</p></a>
</div>
''', current='/cong-cu/')

items = [('Ngón cái','Tự làm một việc tự phục vụ phù hợp tuổi'),('Ngón trỏ','Nói hoặc chỉ được mục tiêu trước khi làm'),
 ('Ngón giữa','Làm việc chính trước khi chơi'),('Ngón áp út','Chờ lượt; nhắc lại ý người khác'),
 ('Ngón út','Đi ngủ đúng giờ; tự dùng cách bình tĩnh'),('Khoa học','Đưa ra dự đoán; kể lại kết quả'),
 ('Trung thực','Tự nhận khi làm đổ hay làm hỏng'),('Biết ơn, tử tế','Tự nói cảm ơn; giúp người khác không cần nhắc')]
rows = ''.join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td></td><td></td><td></td></tr>' for a,b in items)
page('/cong-cu/bang-quan-sat/', 'Bảng quan sát 0–1–2', 'Bảng in để bố mẹ theo dõi tiến bộ của con trong khóa Gia đình 2–8 tuổi.',
f'''
<h1>Bảng quan sát 0–1–2</h1>
<p>Chấm cho mỗi con một bảng. <strong>0</strong> = chưa làm · <strong>1</strong> = làm khi được nhắc · <strong>2</strong> = tự làm.</p>
{PRINT_ROW}
<p>Con: ……………… (chỉ ghi trên giấy, không đăng lên mạng) &nbsp; Tuổi: ……</p>
<div class="table-wrap"><table>
<thead><tr><th>Mục</th><th>Hành vi quan sát</th><th>Tuần 0</th><th>Tuần 6</th><th>Tuần 12</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<h2>Bố mẹ tự theo dõi (đếm trong 3 ngày)</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Tuần 0</th><th>Tuần 6</th><th>Tuần 12</th></tr></thead>
<tbody><tr><td>Số lần khen cụ thể mỗi ngày</td><td></td><td></td><td></td></tr>
<tr><td>Số lần la mắng mỗi ngày</td><td></td><td></td><td></td></tr></tbody></table></div>
<p class="small muted">Bảng này để tự theo dõi, không dùng để chẩn đoán. Nếu lo lắng về sự phát triển của con, hãy hỏi bác sĩ nhi.</p>
''', current='/cong-cu/')

days = ''.join(f'<th>{d}</th>' for d in ['T2','T3','T4','T5','T6','T7','CN'])
blank = '<td></td>'*7
trows = ''.join(f'<tr><td class="tall">{i}. ……………………</td>{blank}</tr>' for i in range(1,6))
page('/cong-cu/bang-thoi-quen/', 'Bảng thói quen 7 ngày', 'Bảng in cho con tự đánh dấu việc tự làm mỗi ngày trong tuần.',
f'''
<h1>Bảng thói quen 7 ngày</h1>
<p>Con viết hoặc vẽ việc mình tự làm ở cột trái. Mỗi ngày làm được thì con tự vẽ một ngôi sao hoặc dán sticker.</p>
{PRINT_ROW}
<div class="table-wrap"><table>
<thead><tr><th>Việc con tự làm</th>{days}</tr></thead>
<tbody>{trows}</tbody></table></div>
<p class="small muted">Gợi ý: bắt đầu với 1–2 việc. Thêm việc mới khi con đã làm đều 5/7 ngày.</p>
''', current='/cong-cu/')

# ---------- Bằng chứng ----------
EV = [
 ('Parenting for Lifelong Health – trẻ nhỏ: thử nghiệm ngẫu nhiên 296 người chăm sóc ở Nam Phi; hành vi nuôi dạy tích cực quan sát được +39% sau 4–5 tháng, +24% sau 17 tháng','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC7155004/','Ward et al. 2019'),
 ('Tài liệu PLH trên trang WHO dùng giấy phép CC BY-NC-ND 4.0 (không phái sinh)','Đã xác nhận','https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health','WHO'),
 ('Học tập cảm xúc – xã hội: phân tích gộp 424 nghiên cứu, 53 nước; chủ yếu ở trường học','Đã xác nhận','https://eric.ed.gov/?id=EJ1394000','Cipriano et al. 2023'),
 ('Truyện khen nhân vật nói thật làm trẻ 3–7 tuổi nhận lỗi nhiều hơn; truyện dọa không hiệu quả hơn','Đã xác nhận','https://pubmed.ncbi.nlm.nih.gov/24928424/','Lee et al. 2014'),
 ('Can thiệp "tư duy phát triển" có hiệu quả rất nhỏ (d ≈ 0,02–0,05)','Đã xác nhận','https://artscimedia.case.edu/wp-content/uploads/sites/141/2020/06/26110416/Macnamara-Burgoyne-2023.pdf','Macnamara & Burgoyne 2023'),
 ('Chương trình chánh niệm đại trà ở trường (MYRIAD, 8.376 học sinh) không vượt nhóm so sánh sau 1 năm','Đã xác nhận','https://www.kcl.ac.uk/news/schools-based-mindfulness-programme-improves-school-culture-and-reduces-teacher-burnout','Kuyken et al. 2022'),
 ('Hướng dẫn hoạt động chức năng điều hành theo tuổi','Đã xác nhận','https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/','Harvard Center on the Developing Child'),
 ('Reach Up: tài liệu theo giấy phép CC BY-NC-SA 4.0','Đã xác nhận','https://reachupandlearn.com/resources/','Reach Up'),
 ('Trẻ nhỏ có thể đuối nước chỉ với vài inch nước trong nhà; giữ trẻ trong tầm tay','Đã xác nhận','https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/','CPSC'),
 ('Bữa cơm gia đình ≥3 lần/tuần gắn với ăn uống lành mạnh hơn (tương quan, không phải nhân quả)','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC3387875/','Hammons & Fiese 2011'),
 ('Tổng đài 111 bảo vệ trẻ em: miễn phí, 24/7','Đã xác nhận','https://tongdai111.vn/','tongdai111.vn'),
 ('Đường dây Ngày Mai 096 306 1414: 13:00–20:30, thứ Tư đến Chủ nhật','Đã xác nhận','https://duongdaynongngaymai.vn/','duongdaynongngaymai.vn'),
 ('113 công an, 114 cứu hỏa, 115 cấp cứu; Bộ Y tế đề xuất gộp thành một số khẩn cấp, chưa có hiệu lực','Đã xác nhận (tra 28/10/2026)','https://thuvienphapluat.vn/hoi-dap-phap-luat/111-113-114-115-la-so-dien-thoai-gi-138013545.html','Thư viện Pháp luật; LuatVietnam'),
 ('Đếm điều may mắn: thử nghiệm 221 học sinh đầu tuổi thiếu niên, tăng biết ơn, lạc quan, hài lòng cuộc sống','Đã xác nhận','https://proofpositive.org/bc-science/counting-blessings-in-early-adolescents-an-experimental-study-of-gratitude-and-subjective-wellbeing/','Froh, Sefick & Emmons 2008'),
 ('Lòng biết ơn gắn với hạnh phúc ở 80 trẻ khoảng 5 tuổi (tương quan)','Đã xác nhận','https://ideas.repec.org/a/spr/jhappi/v21y2020i8d10.1007_s10902-019-00188-6.html','Nguyen & Gordon 2020'),
 ('Thưởng vật chất làm trẻ 20 tháng giúp đỡ ít hơn về sau','Đã xác nhận','https://scholars.duke.edu/publication/1458228','Warneken & Tomasello 2008'),
 ('Bố mẹ làm mẫu, đáp lại, chỉ dạy về cảm xúc gắn với kỹ năng cảm xúc của trẻ mầm non; mức liên hệ nhỏ, chủ yếu tương quan','Đã xác nhận','https://figshare.com/articles/journal_contribution/Parents_socialization_of_preschool-aged_children_s_emotion_skills_A_meta-analysis_using_an_emotion-focused_parenting_practices_framework/14515686','Zinsser, Gordon & Jiang 2021'),
 ('Anh chị em 4 và 6 tuổi dạy nhau tự nhiên, thường xuyên (quan sát 39 gia đình)','Đã xác nhận','https://www.sciencedaily.com/releases/2014/07/140709115505.htm','Howe et al., Journal of Cognition and Development'),
 ('Đèn càng gần vật, bóng càng to; mặt trời thấp thì bóng dài (nội dung K–2 trong NGSS)','Đã xác nhận','https://www.nsta.org/sites/default/files/journal-articles/supplemental-resources/3-27-2020%20-%20Lesson%20Plan%20-%20%20Daily%20Do%20-%20Why%20Is%20My%20Shadow%20Always%20Changing.pdf','NSTA'),
 ('Cách "đầu tiên… rồi…" dựa trên nguyên tắc Premack; mức bằng chứng khi dùng ở nhà chưa kiểm tra','Cần kiểm chứng','','Chưa đọc được nguồn tổng quan toàn văn'),
 ('Giờ ngủ khuyến nghị trong 24 giờ: 1–2 tuổi 11–14 giờ; 3–5 tuổi 10–13 giờ; 6–12 tuổi 9–12 giờ','Đã xác nhận','https://www.sciencedaily.com/releases/2016/06/160613122419.htm','AASM 2016, J Clin Sleep Med'),
 ('Trẻ 3,5–6 tuổi chờ khoảng 12 phút khi người lớn giữ lời, khoảng 3 phút khi người lớn thất hứa (28 trẻ, phòng thí nghiệm)','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC3730121/','Kidd, Palmeri & Aslin 2013'),
 ('Chuẩn thiết kế kỹ thuật cho lớp mẫu giáo – lớp 2: xác định vấn đề, vẽ mô hình, so sánh dữ liệu thử của hai thiết kế','Đã xác nhận','https://www.nextgenscience.org/node/1116','NGSS K-2-ETS1'),
 ('Tự trắc ẩn cao gắn với ít lo âu, trầm cảm, căng thẳng ở thanh thiếu niên 10–19 tuổi (r = −0,55; tương quan)','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC6061226','Marsh, Chan & MacBeth 2018'),
 ('Hướng dẫn vận động, ít ngồi và giấc ngủ cho trẻ dưới 5 tuổi','Đã xác nhận','https://www.who.int/publications/i/item/9789241550536','WHO 2019'),
 ('Với trẻ 2–4 tuổi: giữ 2–3 luật một lúc, nói rõ hành vi muốn thấy, mọi người chăm con dùng cùng luật, khen cụ thể, dán bảng luật có hình','Đã xác nhận','https://www.cdc.gov/parenting-toddlers/structure-rules/rules.html','CDC – Essentials for Parenting'),
 ('Đánh đòn gây hại cho trẻ, làm hành vi xấu tăng theo thời gian và không có kết quả tích cực','Đã xác nhận','https://www.who.int/news-room/fact-sheets/detail/corporal-punishment-and-health','WHO, tờ thông tin 2026'),
 ('Mô hình lý thuyết: con tiếp nhận giá trị khi hiểu đúng thông điệp của bố mẹ và chấp nhận nó','Đã xác nhận','','Grusec & Goodnow 1994, Developmental Psychology 30(1):4–19'),
 ('Lập kế hoạch "Nếu… thì…" giúp đạt mục tiêu tốt hơn (94 thử nghiệm, d = 0,65; chủ yếu người lớn)','Đã xác nhận','https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f','Gollwitzer & Sheeran 2006'),
 ('Nếp sinh hoạt và nghi thức gia đình gắn với năng lực nuôi dạy, sự thích nghi của trẻ, hài lòng hôn nhân (tổng quan 32 công trình; liên hệ)','Đã xác nhận','https://pubmed.ncbi.nlm.nih.gov/12561283/','Fiese et al. 2002'),
 ('Bố mẹ nên xem lại giá trị mình thực sự truyền cho con; cho con thực hành quan tâm người khác','Đã xác nhận','https://mcc.gse.harvard.edu/reports/children-mean-raise','Making Caring Common, Harvard 2014'),
 ('Họp gia đình 15 phút, Mái nhà giá trị, Phiếu giá trị của khóa Giá trị nhà mình','Đánh giá chuyên môn','',''),
 ('Ba khối nền năng lực tài chính: chức năng điều hành (từ 3–5 tuổi), thói quen và chuẩn mực tiền (hình thành rõ ở 6–12 tuổi), kiến thức và ra quyết định (13–21 tuổi)','Đã xác nhận','https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/learn/','CFPB'),
 ('Giáo dục tài chính cải thiện hiểu biết và hành vi tài chính (76 thử nghiệm ngẫu nhiên, hơn 160.000 người)','Đã xác nhận','https://repository.upenn.edu/prc_papers/676','Kaiser, Lusardi, Menkhoff & Urban (bản 2020)'),
 ('Lãi suất vay thỏa thuận không vượt 20%/năm, trừ khi luật khác quy định khác; phần vượt không có hiệu lực','Đã xác nhận','https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam','Bộ luật Dân sự 2015 (91/2015/QH13), Điều 468'),
 ('Cho vay lãi suất gấp 5 lần mức cao nhất của Bộ luật Dân sự có thể bị xử lý hình sự','Đã xác nhận','https://tapchitoaan.vn/huong-dan-ap-dung-dieu-201-cua-blhs-va-viec-xet-xu-vu-an-cho-vay-lai-nang','Bộ luật Hình sự 2015, Điều 201'),
 ('Luật 86/2025/QH15 (hiệu lực 01/07/2025) có sửa mức phạt Điều 201 hay không','Cần kiểm chứng','',''),
 ('Phụ nữ làm 76,2% tổng số giờ việc chăm sóc không lương trên thế giới, gấp hơn 3 lần nam giới','Đã xác nhận','https://www.ilo.org/resource/news/ilo-calls-urgent-action-prevent-looming-global-care-crisis','ILO 2018, Care work and care jobs'),
 ('"Việc nghĩ" trong nhà gồm dự đoán, nghĩ cách, quyết định, theo dõi; phụ nữ làm nhiều hơn phần dự đoán và theo dõi (35 cặp)','Đã xác nhận','https://inequality.hks.harvard.edu/publications/cognitive-dimension-household-labor','Daminger 2019, American Sociological Review 84(4)'),
 ('Việc nhà theo tuổi 5–12, bảng việc, thêm từng việc một, khen cố gắng hơn kết quả','Đã xác nhận','https://www.healthychildren.org/English/family-life/family-dynamics/communication-discipline/Pages/Chores-and-Responsibility.aspx','AAP – HealthyChildren.org (2024)'),
 ('Việc tự chăm sóc và chăm sóc gia đình gắn với trí nhớ làm việc, kiềm chế tốt hơn ở trẻ 5–13 tuổi (207 phụ huynh; tương quan)','Đã xác nhận','https://neurosciencenews.com/child-chores-brain-function-20827/','Tepper et al. 2022'),
 ('Năm bước giao và đáp: nhận ra lời giao, đáp lại, gọi tên, thay phiên và chờ, kết thúc và bắt đầu','Đã xác nhận','https://bettercarenetwork.org/sites/default/files/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf','Harvard Center on the Developing Child (2019)'),
 ('Thăm nhà hằng tuần dạy mẹ chơi, nói chuyện với con ở Jamaica: sau khoảng 20 năm, thu nhập cao hơn 25% (105 người theo dõi)','Đã xác nhận','https://sciencedaily.com/releases/2014/05/140529142354.htm','Gertler et al. 2014, Science'),
 ('Ngủ an toàn: nằm ngửa, mặt phẳng cứng, không đồ mềm, cùng phòng không chung giường ít nhất 6 tháng đầu','Đã xác nhận','https://aap.org/en/news-room/news-releases/aap/2022/american-academy-of-pediatrics-updates-safe-sleep-recommendations-back-is-best','AAP 2022'),
 ('Trẻ dưới 1 tuổi: ≥30 phút nằm sấp khi thức; 1–2 tuổi: ≥180 phút vận động; không ngồi ghế, xe đẩy quá 1 giờ liền; không màn hình dưới 2 tuổi (2 tuổi ≤1 giờ)','Đã xác nhận','https://new.chconline.org/new-who-guidelines-on-physical-activity-sedentary-behaviour-and-sleep-for-children-under-5-years-of-age','WHO 2019'),
 ('Đọc to cho con bắt đầu từ lúc mới sinh','Đã xác nhận','https://www.physiciansweekly.com/aap-why-literacy-promotion-is-crucial-during-clinical-visits/','AAP 2024, Pediatrics'),
 ('Khóc là nguyên nhân chính dẫn đến lắc trẻ; đặt trẻ chỗ an toàn, tạm rời đi khi bực, gọi người giúp; không bao giờ lắc','Đã xác nhận','https://webarchive.library.unt.edu/web/20201221232327/https://www.cdc.gov/violenceprevention/childabuseandneglect/Abusive-Head-Trauma.html','CDC (bản lưu trữ)'),
 ('Danh sách mốc phát triển CDC 2022 dùng ngưỡng 75% trẻ cùng tuổi','Đã xác nhận','https://www.disabilityscoop.com/2022/02/10/cdc-revises-developmental-milestones-for-young-kids/29698/','CDC, qua Disability Scoop'),
 ('Strengthening Families 10–14: mức bằng chứng 3; thử nghiệm Mỹ 446 gia đình: con ít bắt đầu uống rượu hơn; thử nghiệm châu Âu chưa rõ ràng','Đã xác nhận','https://foundations.org.uk/toolkit/guidebook/strengthening-families-programme-10-14','Foundations (Anh)'),
 ('PLH cho thanh thiếu niên ở Nam Phi (552 gia đình): bố mẹ báo cáo bạo hành giảm, nuôi dạy tích cực tăng; con báo cáo giám sát tốt hơn nhưng không giảm bạo hành','Đã xác nhận','https://www.research.ed.ac.uk/en/publications/parenting-for-lifelong-health-a-pragmatic-cluster-randomised-cont/','Cluver et al. 2018, BMJ Global Health'),
 ('Hiểu biết của bố mẹ gắn với việc con tự kể nhiều hơn là theo dõi; cảm giác bị kiểm soát gắn với thích nghi kém (nghiên cứu liên hệ)','Đã xác nhận','https://pubmed.ncbi.nlm.nih.gov/10830980','Kerr & Stattin 2000, Child Development'),
 ('Kế hoạch dùng thiết bị gia đình, giờ và chỗ không máy, bố mẹ làm gương','Đã xác nhận','https://www.ksat.com/business/2023/05/23/the-us-surgeon-general-has-some-tips-for-parents-and-teens-on-social-media-use/','Tổng Y sĩ Hoa Kỳ 2023 (qua AP)'),
 ('Cấm bán, cung cấp, khuyến mại rượu bia cho người chưa đủ 18 tuổi','Đã xác nhận','https://luatvietnam.vn/an-ninh-trat-tu/luat-phong-chong-tac-hai-cua-ruou-bia-2019-so-44-2019-qh14-175006-d1.html','Luật 44/2019/QH14, Điều 5 khoản 3 (hiệu lực 01/01/2020)'),
 ('Cấm thuốc lá điện tử, thuốc lá nung nóng từ năm 2025 (Quốc hội thông qua 30/11/2024)','Đã xác nhận','https://baovanhoa.vn/thoi-su/quoc-hoi-ra-nghi-quyet-ve-cam-thuoc-la-dien-tu-thuoc-la-nung-nong-tu-nam-2025-113542.html','Báo Văn hóa'),
 ('Số hiệu nghị quyết cấm thuốc lá điện tử và mức xử phạt','Cần kiểm chứng','',''),
 ('Lớp 8 buổi về đồng nuôi dạy cho cặp sắp có con đầu lòng (169 cặp, thử nghiệm ngẫu nhiên): tăng ủng hộ nhau, giảm trầm cảm và lo âu ở mẹ','Đã xác nhận','https://pure.psu.edu/en/publications/establishing-family-foundations-intervention-effects-on-coparenti/','Feinberg & Kan 2008, J Fam Psychol 22(2)'),
 ('Đồng nuôi dạy liên hệ yếu với vấn đề hành vi, cảm xúc ở trẻ (93 nghiên cứu, r khoảng 0,16–0,20; tương quan)','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC9407961','Zhao et al. 2022, IJERPH'),
 ('Xung đột giữa bố mẹ ảnh hưởng đến con; cách thể hiện và xử lý xung đột là điều quan trọng','Đã xác nhận','https://pubmed.ncbi.nlm.nih.gov/29574737/','Harold & Sellers 2018'),
 ('Cặp mới cưới về sau ly hôn có nhiều biểu hiện tiêu cực hơn trong 3 phút đầu cuộc bàn bất đồng (124 cặp, 17 ly hôn)','Đã xác nhận','https://washington.edu/news/1999/09/27/first-three-minutes-of-discussion-about-on-going-area-of-marital-conflict-are-predictive-of-divorce-for-newlyweds','Carrère & Gottman 1999'),
 ('Luật Phòng, chống bạo lực gia đình 13/2022/QH15 (hiệu lực 01/07/2023): các nhóm hành vi bạo lực gia đình','Đã xác nhận','https://luatvietnam.vn/hon-nhan-gia-dinh/luat-phong-chong-bao-luc-gia-dinh-so-13-2022-qh15-238397-d1.html','LuatVietnam'),
 ('62,9% phụ nữ Việt Nam từng chịu ít nhất một hình thức bạo lực hoặc hành vi kiểm soát từ chồng; khoảng một nửa chưa từng kể với ai','Đã xác nhận','https://www.sggp.org.vn/gan-63-phu-nu-o-nuoc-ta-tung-chiu-bao-luc-50-khong-ke-voi-ai-post620554.html','Nghiên cứu quốc gia 2019 (Bộ LĐ-TB&XH, TCTK, UNFPA)'),
 ('Tổng đài 117 về phòng, chống bạo lực gia đình hoạt động 24/7 toàn quốc từ 9/2026; có miễn phí hay không','Cần kiểm chứng','https://thuonghieucongluan.com.vn/tong-dai-117-hoat-dong-24-7-tiep-nhan-tin-bao-bao-luc-gia-dinh-tren-toan-quoc-a333505.html','Báo Thương hiệu và Công luận'),
 ('Mỗi năm khoảng 2.000 trẻ em Việt Nam tử vong do đuối nước','Đã xác nhận','https://www.who.int/vietnam/vi/news/feature-stories/item/in-viet-nam--low-cost-water-safety-actions-help-reduce-child-drowning-deaths','WHO Việt Nam, 12/2023'),
 ('Tivi, đồ đạc đổ: tại Mỹ trung bình khoảng 2 tuần có 1 trẻ tử vong; nên bắt vít vào tường','Đã xác nhận','https://www.cpsc.gov/Newsroom/News-Releases/2015/Anchor-It-CPSC-Launches-Nations-Largest-Campaign-to-Prevent-Furniture-and-TV-Tip-Over-Deaths-and-Injuries','CPSC 2015'),
 ('Luật PCCC và CNCH 55/2024/QH15 (hiệu lực 01/07/2025): trách nhiệm chủ hộ tự kiểm tra, khắc phục nguy cơ cháy nổ','Đã xác nhận','https://luatvietnam.vn/dat-dai/luat-phong-chay-chua-chay-va-cuu-nan-cuu-ho-2024-so-55-2024-qh15-379071-d1.html','LuatVietnam'),
 ('Sạc xe điện: không sạc qua đêm, dùng sạc chính hãng, không độ chế, không sạc gần đồ dễ cháy','Đã xác nhận','https://lsvn.vn/canh-bao-4-nguyen-nhan-chu-yeu-gay-chay-no-xe-dien-gia-tang-a165609.html','Cảnh sát PCCC Phú Thọ, 11/2025'),
 ('Năm chìa khóa an toàn thực phẩm','Đã xác nhận','https://www.paho.org/en/news/21-12-2015-pahowho-recommends-five-keys-safer-food-healthy-holiday-season','PAHO/WHO'),
 ('Sơ cứu bỏng: nước mát đang chảy 20 phút; không đá, kem, kem đánh răng','Đã xác nhận','https://www.schn.health.nsw.gov.au/kids-health-hub/safety-and-injury-prevention/burns-and-fire/first-aid-burns','Sydney Children\'s Hospitals Network'),
 ('Quan hệ xã hội mạnh gắn với khả năng sống sót cao hơn (148 nghiên cứu, OR 1,50; quan sát)','Đã xác nhận','https://www.rti.org/publication/social-relationships-mortality-risk-meta-analytic-review','Holt-Lunstad et al. 2010'),
 ('Trẻ biết nhiều chuyện gia đình có lòng tự trọng cao hơn (40 gia đình; liên hệ)','Đã xác nhận','https://www.medicalnewstoday.com/releases/31955','Fivush & Duke, Emory'),
 ('Kế hoạch màn hình gia đình: chỗ không màn hình, chọn nội dung, tắt tự phát, bố mẹ làm gương','Đã xác nhận','https://healthychildren.org/English/family-life/Media/Pages/How-to-Make-a-Family-Media-Use-Plan.aspx','AAP (cập nhật 1/2026)'),
 ('Mẹo "không lọt lõi giấy vệ sinh" để loại vật nhỏ','Đánh giá chuyên môn','',''),
 ('Lịch 12 tuần và các hoạt động của khóa Gia đình 2–8','Đánh giá chuyên môn','',''),
]
def _src(u,s): return f'<a href="{u}">{s}</a>' if u else (s or 'Thiết kế hoặc đánh giá của daynentang.com')
erows = ''.join(f'<tr><td>{c}</td><td><span class="label">[{l}]</span></td><td>{_src(u,s)}</td></tr>' for c,l,u,s in EV)
page('/bang-chung/', 'Bằng chứng và nguồn', 'Bảng kiểm chứng: các nhận định trên daynentang.com, nhãn mức độ chắc chắn và nguồn gốc.',
f'''
<h1>Bằng chứng và nguồn</h1>
<p class="lead">Mỗi nhận định quan trọng trên trang được gắn một trong bốn nhãn.</p>
<ul>
<li><strong>[Đã xác nhận]</strong> – có nguồn đã đọc, ghi rõ bên cạnh.</li>
<li><strong>[Suy luận]</strong> – rút ra từ nguồn, nhưng nguồn không nói trực tiếp.</li>
<li><strong>[Đánh giá chuyên môn]</strong> – ý kiến của người soạn, chưa có nghiên cứu riêng.</li>
<li><strong>[Cần kiểm chứng]</strong> – chưa tìm được nguồn đủ tin cậy.</li>
</ul>
<div class="table-wrap"><table>
<thead><tr><th>Nhận định</th><th>Nhãn</th><th>Nguồn</th></tr></thead>
<tbody>{erows}</tbody></table></div>
<p class="small muted">Tra cứu ngày 28/10/2026. Thấy sai sót? Chúng tôi sửa công khai trong nhật ký sửa đổi ở trang Giới thiệu.</p>
''', current=None)

# ---------- 404 ----------
page('/404.html', 'Không tìm thấy trang', 'Trang bạn tìm không có trên daynentang.com.',
'''<h1>Không tìm thấy trang</h1><p>Trang này không có hoặc đã đổi địa chỉ.</p>
<p><a class="btn primary" href="/">Về trang chủ</a> <a class="btn" href="/gia-dinh/">Khóa cho gia đình</a></p>''')

# ---------- robots, sitemap, headers ----------
urls = []
for d, _, files in os.walk(ROOT):
    if '/.git' in d: continue
    for f in files:
        if f == 'index.html':
            rel = os.path.relpath(d, ROOT)
            urls.append('/' if rel == '.' else '/' + rel + '/')
urls.sort()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     ''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>2026-10-28</lastmod></url>\n' for u in urls) + '</urlset>\n'
open(os.path.join(ROOT,'sitemap.xml'),'w').write(sm)
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(os.path.join(ROOT,'_headers'),'w').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self' 'unsafe-inline'; frame-ancestors 'none'; base-uri 'self'; form-action 'none'
  X-Frame-Options: DENY
''')
print(len(urls), 'pages')
