# Bản tiếng Anh – daynentang.com
# Dịch từ trang tiếng Việt. Khi hai bản khác nhau, bản tiếng Việt là bản gốc.
import os, html
from common import page, ROOT, PRINT_ROW_EN, HELP_BOX_EN

V, I, E, C = ('<span class="label">[Verified]</span>', '<span class="label">[Inference]</span>',
              '<span class="label">[Expert judgement]</span>', '<span class="label">[Needs checking]</span>')

# ======================= Hình minh họa tiếng Anh =======================
FIG_SRC = os.path.join(ROOT, 'assets', 'minh-hoa')
FIG_OUT = os.path.join(FIG_SRC, 'en')
os.makedirs(FIG_OUT, exist_ok=True)

# Chuỗi trong SVG gốc -> chuỗi tiếng Anh (thay trong >…</text>, <title> và aria-label)
FIG_TEXT = {
 'khoa-1.svg': {'Bàn tay nền tảng': 'The Foundation Hand', 'Ngón cái': 'Thumb', 'Tự làm được': 'I can do it',
                'Ngón trỏ': 'Index', 'Nhìn đích': 'See the goal', 'Ngón giữa': 'Middle',
                'Việc quan trọng trước': 'Important things first', 'Áp út': 'Ring', 'Cùng vui': 'Fun together',
                'Ngón út': 'Little', 'Chăm cây': 'Grow well'},
 'khoa-2.svg': {'Chu trình Khoa học bằng tay': 'Hands-on science cycle', 'Khoa học bằng tay': 'Hands-on science',
                '1. Quan sát': '1. Look', '2. Đoán': '2. Guess', '3. Thử': '3. Try', '4. Kể lại': '4. Tell'},
 'khoa-3.svg': {'Một buổi 30 phút': 'A 30-minute session', 'Kết nối': 'Connect', 'Thở': 'Breathe',
                'Hoạt động': 'Activity', 'Kể lại': 'Retell', 'Mang về': 'Use it',
                'Mệt thì dừng ở bước đang làm': 'Tired? Stop at the current step'},
 't1-1.svg': {'Bảng buổi sáng': 'Morning chart', 'Bảng buổi sáng của con': 'My morning chart', 'Dậy': 'Get up',
              'Đánh răng': 'Teeth', 'Mặc đồ': 'Dress', 'Ăn sáng': 'Breakfast', 'Xếp cặp': 'Pack bag',
              'Con khoanh 1 việc sẽ tự làm tuần này': 'Circle 1 job you will do yourself this week'},
 't1-2.svg': {'Trò Người máy': 'Robot game', '"Bố giơ tay trái lên!"': '"Robot, lift your left arm!"',
              'Trò "Người máy": làm đúng từng lời con nói': 'Robot game: do exactly what the child says'},
 't1-3.svg': {'Cất đồ chơi vào rổ': 'Toys back in the basket', '"Đồ chơi về nhà…"': '"Toys go home…"'},
 'k1-1.svg': {'Chậu nước thử nổi chìm': 'Float-or-sink tub', 'Nổi hay chìm?': 'Float or sink?', 'nổi': 'floats', 'chìm': 'sinks'},
 'k1-2.svg': {'Chai rỗng và chai đầy nước': 'Empty bottle and full bottle',
              'Hai chai giống nhau – vì sao khác?': 'Same bottles – why different?',
              'chai rỗng': 'empty bottle', 'chai đầy nước (nằm thấp)': 'full bottle (sits low)'},
 'k1-3.svg': {'Bảng ghi Vật – Đoán – Kết quả': 'Record sheet: Object – Guess – Result', 'Vật': 'Object',
              'Con đoán': 'My guess', 'Kết quả': 'Result', 'Thìa': 'Spoon', 'Chai rỗng': 'Empty bottle',
              'Quả cam': 'Orange', 'Khối gỗ': 'Wood block', 'C': 'S', 'N': 'F'},
 'g1-1.svg': {'Khủng long Tí làm vỡ chậu cây': 'Ti the Dinosaur breaks a flower pot',
              'Tí lỡ quẫy đuôi làm vỡ chậu cây': 'Ti’s tail knocks over the flower pot'},
 'g1-2.svg': {'Tí nói thật với bà': 'Ti tells Grandma the truth', '"Bà ơi, cháu xin lỗi"': '"Grandma, I’m sorry"',
              '"Cảm ơn cháu nói thật"': '"Thanks for telling me"'},
 'g1-3.svg': {'Ba bước Dừng – Thở – Nói': 'Three steps: Stop – Breathe – Tell', 'Dừng – Thở – Nói': 'Stop – Breathe – Tell',
              'DỪNG': 'STOP', '1. Dừng lại': '1. Stop', '2. Thở 1 hơi': '2. One breath', '3. Nói thật': '3. Tell the truth'},
}

def _fig_text(fn, mapping):
    s = open(os.path.join(FIG_SRC, fn), encoding='utf-8').read()
    for vi, en in mapping.items():
        ev, ee = html.escape(vi, quote=False), html.escape(en, quote=False)
        s = s.replace(f'>{ev}</text>', f'>{ee}</text>').replace(f'<title>{ev}</title>', f'<title>{ee}</title>')
        s = s.replace(f'aria-label="{html.escape(vi)}"', f'aria-label="{html.escape(en)}"')
    s = s.replace('<svg ', '<svg xml:lang="en" ', 1)
    open(os.path.join(FIG_OUT, fn), 'w', encoding='utf-8').write(s)

for _fn, _m in FIG_TEXT.items():
    _fig_text(_fn, _m)

FIGS_EN = {
 'KHOA': [('khoa-1.svg', 'The Foundation Hand', 'Five fingers, five habits. Children look at their hand and remember.'),
          ('khoa-2.svg', 'Hands-on science cycle', 'Every science session: look, guess, try, then tell what happened.'),
          ('khoa-3.svg', 'A 30-minute session', 'Connect 3′, breathe 1′, activity 15′, retell 5′, use it in daily life 5′.')],
 'T1': [('t1-1.svg', 'Morning chart', 'The child draws 4–5 morning jobs and circles one to do alone.'),
        ('t1-2.svg', 'Robot game', 'The parent plays a robot; the child gives step-by-step orders.'),
        ('t1-3.svg', 'Toys back in the basket', 'The toddler puts big toys in the basket while you sing.')],
 'K1': [('k1-1.svg', 'Float-or-sink tub', 'Drop each object into a shallow tub. An adult always sits close.'),
        ('k1-2.svg', 'Empty bottle and full bottle', 'Surprise test: the empty bottle floats high, the full one sits much lower.'),
        ('k1-3.svg', 'Record sheet', 'Write F (float) or S (sink) before dropping. A wrong guess gets a question mark.')],
 'G1': [('g1-1.svg', 'Ti the Dinosaur breaks a flower pot', 'Ti breaks Grandma’s flower pot and thinks about running away.'),
        ('g1-2.svg', 'Ti tells Grandma the truth', 'Grandma hugs Ti and thanks Ti for telling the truth.'),
        ('g1-3.svg', 'Stop – Breathe – Tell', 'Three steps after a mistake: stop, take one breath, tell the truth.')],
}
def figure_block_en(code):
    items = ''.join(f'<figure><img src="/assets/minh-hoa/en/{fn}" alt="{html.escape(alt)}" width="320" height="200" loading="lazy">'
                    f'<figcaption>{cap}</figcaption></figure>' for fn, alt, cap in FIGS_EN.get(code, []))
    return f'<div class="figs">{items}</div>' if items else ''

VI_ONLY = ' <span class="vi-only">(Vietnamese)</span>'

# ======================= Trang chủ =======================
page('/en/', 'Day Nen Tang – foundations for life, free self-study – daynentang.com',
 'Free, evidence-based courses that help families and individuals learn four foundations: skills, character, mind and body.',
 f'''
<section class="hero">
  <div>
    <p class="eyebrow">Free self-study</p>
    <h1>Foundations for life, starting at home</h1>
    <p class="lead">daynentang.com helps every family and every person learn four foundations for free: skills, character, mind and body.
    Each lesson is based on evidence and can be used right away, even with no money and no teacher.</p>
    <div class="cta">
      <a class="btn primary" href="/en/family/">I am a parent</a>
      <a class="btn" href="/en/personal/">I study on my own</a>
      <a class="btn warm" href="/en/get-help/">I need help now</a>
    </div>
  </div>
  <img src="/assets/logo/daynentang-logo.svg" alt="Day Nen Tang logo: mountains, a sun and animals under a ribbon banner" width="400" height="428">
</section>

<div class="box">
  <h3>About the English pages</h3>
  <p>The site is written in Vietnamese for Vietnamese families. We are translating it step by step.
  The first English course week is <a href="/en/courses/family-2-8/">Family 2–8: Week 1</a>.
  Pages marked <span class="vi-only">(Vietnamese)</span> are not translated yet; your browser’s Translate option can help with those.</p>
</div>

<h2>Every course makes two promises</h2>
<div class="two">
  <div class="card"><h3>Help now</h3><p>A real result you can see within 1–2 weeks.</p></div>
  <div class="card"><h3>Build for the long term</h3><p>One way of thinking and one skill you can use for years.</p></div>
</div>

<h2>Four pillars</h2>
<div class="grid">
  <div class="card"><h3>Skills</h3><p>Looking after yourself, planning, putting first things first, managing money and housework.</p></div>
  <div class="card"><h3>Character</h3><p>Honesty, gratitude, kindness, responsibility, a good work ethic.</p></div>
  <div class="card"><h3>Mind</h3><p>Naming feelings, short breathing, staying calm when angry, knowing when to ask for help.</p></div>
  <div class="card"><h3>Body</h3><p>Sleep, movement, family meals, safety at home.</p></div>
</div>

<div class="box">
  <h3>How we work</h3>
  <p>Every lesson lists its sources and a label for how certain each claim is. We borrow only ideas from copyrighted programmes and rewrite everything.
  Lessons are tried first in the author’s own family. <a href="/en/about/">Read our principles</a>.</p>
</div>
''', current='/en/', lang='en')

# ======================= Gia đình =======================
FAM = [
 ('Family 2–8: The Foundation Hand', 'Self-reliant habits, hands-on science and kind values through 30 minutes of play.', '12 weeks', '/en/courses/family-2-8/', '/khoa-hoc/gia-dinh-2-8/', 'Week 1 in English'),
 ('Our family values', 'Agree on 3–5 family values and house rules; a 15-minute family meeting each week.', '4 weeks', None, '/khoa-hoc/gia-tri-nha-minh/', ''),
 ('Our family money', 'A monthly budget, an emergency fund, teaching children to earn, save and spend.', '6 weeks', None, '/khoa-hoc/tien-nha-minh/', ''),
 ('Sharing housework fairly', 'Divide housework fairly; age-appropriate chore charts for children.', '4 weeks', None, '/khoa-hoc/viec-nha-chia-deu/', ''),
 ('Family 0–2: Serve and return', 'Five minutes of “serve and return” play a day to build attachment and language.', '8 weeks', None, '/khoa-hoc/gia-dinh-0-2/', ''),
 ('Families with children 10–14', 'Supporting early adolescence: talking, boundaries, independence.', '7 weeks', None, '/khoa-hoc/gia-dinh-10-14/', ''),
 ('Parents as one team', 'One team when raising children; talking through disagreements.', '6 weeks', None, '/khoa-hoc/vo-chong-dong-long/', ''),
 ('A tidy, safe home', 'Home safety check, weekly menu, maintenance calendar.', '4 weeks', None, '/khoa-hoc/nha-gon-nha-an-toan/', ''),
 ('Family and community', 'Grandparents, relatives, neighbours, a family screen plan.', '4 weeks', None, '/khoa-hoc/gia-dinh-va-cong-dong/', ''),
]
cards = ''
for name, desc, dur, en_href, vi_href, tag in FAM:
    if en_href:
        cards += f'<a class="card" href="{en_href}"><span class="tag">{tag}</span><h3>{name}</h3><p>{desc}</p><p class="small muted">{dur}</p></a>'
    else:
        cards += (f'<a class="card" href="{vi_href}" hreflang="vi"><span class="tag soon">Vietnamese only</span><h3>{name}</h3>'
                  f'<p>{desc}</p><p class="small muted">{dur}</p></a>')
page('/en/family/', 'Family', 'Free courses for parents: raising children, family values, money, housework, home and relationships.',
f'''
<p class="eyebrow">Main focus</p>
<h1>Family</h1>
<p class="lead">These courses give parents a mindset, skills and tools to build a family with clear values, hard work, integrity and kindness.
With young children, the parent guides and learns alongside the child.</p>
<div class="grid">{cards}</div>
<p class="small muted">All courses are free. Courses marked “Vietnamese only” open the Vietnamese page; your browser can translate it.
Every course is still a trial version that we revise after real families use it.</p>
''', current='/en/family/', lang='en')


# ======================= Cá nhân =======================
PERS = [
 ('Growing up safe', 'Ages 10–14, with an adult alongside', '/khoa-hoc/lon-len-an-toan/'),
 ('Knowing myself', 'Ages 13–17, self-study', '/khoa-hoc/hieu-minh/'),
 ('Self-study, self-management', 'Final-year secondary and university students', '/khoa-hoc/tu-hoc-tu-quan/'),
 ('Solid in my trade', 'Vocational learners aged 15–24', '/khoa-hoc/vung-nghe/'),
 ('15 minutes a day', 'Factory and shift workers', '/khoa-hoc/15-phut-moi-ngay/'),
 ('Confident and safe', 'Girls and women', '/khoa-hoc/tu-tin-an-toan/'),
 ('Independent, step by step', 'People with disabilities and their families', None),
 ('Basic care for the mind', 'People facing emotional difficulties', None),
 ('Safe movement', 'People with low strength or mobility', None),
 ('Foundations without electricity', 'Places short of power, water or schools', None),
]
pc = ''.join(
 (f'<a class="card" href="{h}" hreflang="vi"><span class="tag soon">Vietnamese only</span><h3>{n}</h3><p class="muted">{a}</p></a>' if h
  else f'<div class="card"><span class="tag soon">In preparation</span><h3>{n}</h3><p class="muted">{a}</p></div>') for n, a, h in PERS)
page('/en/personal/', 'Personal', 'Free self-study courses by audience: young people, students, workers, people with disabilities and other groups.',
f'''
<h1>Personal</h1>
<p class="lead">Courses for people learning on their own, for different life situations. Six courses are open, in Vietnamese only for now;
your browser’s Translate option can help. Several are written for readers under 18, and a trusted adult should read alongside them.</p>
<div class="grid">{pc}</div>
<p class="small muted">All open courses are trial versions, not yet tested with learners or reviewed by specialists. Vietnamese laws and phone numbers in these courses apply in Vietnam only.</p>
<div class="box"><p>Want to go deeper on the mind (Stoicism, Buddhism, meditation, a disciplined way of life)? That will be on our sister site <strong>tamhonkhoe.com</strong> (in Vietnamese, coming soon).</p></div>
{HELP_BOX_EN}
''', current='/en/personal/', lang='en')

# ======================= Cần giúp ngay =======================
page('/en/get-help/', 'Get help now', 'Emergency and support phone numbers in Vietnam, and how to find a helpline in other countries.',
'''
<h1>Get help now</h1>
<p class="lead">If you or someone else is in danger, call now. This website does not replace a doctor, a psychologist or the authorities.</p>

<h2>In Vietnam</h2>
<div class="table-wrap"><table>
<thead><tr><th>Number</th><th>When to call</th><th>Hours</th></tr></thead>
<tbody>
<tr><td><strong>115</strong></td><td>Medical emergency</td><td>24/7</td></tr>
<tr><td><strong>111</strong></td><td>National child protection hotline: a child is abused, hurt, abandoned, or needs advice</td><td>24/7, free</td></tr>
<tr><td><strong>096 306 1414</strong></td><td>Ngày Mai hotline: people with depression or thoughts of self-harm, and their families (in Vietnamese)</td><td>13:00–20:30, Wednesday to Sunday</td></tr>
<tr><td><strong>117</strong></td><td>National domestic violence hotline: advice, support, referral to services (running since September 2026)</td><td>24/7</td></tr>
<tr><td><strong>112</strong></td><td>Search and rescue</td><td>24/7</td></tr>
<tr><td><strong>113 / 114</strong></td><td>Police / Fire</td><td>24/7</td></tr>
</tbody></table></div>
<p class="small muted">Checked on 28 October 2026 from tongdai111.vn and duongdaynongngaymai.vn. We re-check every quarter. If a number does not answer, call 115 or go to the nearest health facility.
Most lines answer in Vietnamese.</p>

<h2>Outside Vietnam</h2>
<ul>
<li>Call your local emergency number straight away if someone is in danger.</li>
<li><a href="https://findahelpline.com/">Find A Helpline</a> lists free, confidential crisis lines in many countries (run by ThroughLine).</li>
</ul>

<h2>While you wait</h2>
<ul>
<li>Stay with the person in danger, if you are safe.</li>
<li>Move dangerous things away: knives, medicines, cords.</li>
<li>Speak slowly and listen more. You don’t need the right words; just be there.</li>
</ul>
''', current=None, lang='en')

# ======================= Giới thiệu =======================
page('/en/about/', 'About', 'Mission, principles, privacy policy and licence of daynentang.com.',
'''
<h1>About</h1>
<h2>Mission</h2>
<p>daynentang.com helps every family and every person learn four foundations for free: skills, character, mind and body.
Each lesson is based on evidence and can be used right away, even with no money and no teacher.</p>
<p><strong>Vision:</strong> every Vietnamese family, however poor or far away, has a set of foundations they can trust, to stand on their own feet and help others.</p>

<h2>Six principles</h2>
<ol>
<li><strong>Evidence.</strong> Every lesson lists sources and one of four labels: Verified, Inference, Expert judgement, Needs checking.</li>
<li><strong>Truly free.</strong> No fees, no ads, no selling of data.</li>
<li><strong>Privacy for children.</strong> We never publish a child’s name, photo or voice.</li>
<li><strong>Safety.</strong> Every lesson has a Safety section. Lessons about the mind always include helpline numbers.</li>
<li><strong>Accessible.</strong> Printable, clear text, works on weak phones and slow connections.</li>
<li><strong>Integrity.</strong> No exaggerated claims, no use of other people’s brands, mistakes corrected in public.</li>
</ol>

<h2>Who writes the lessons?</h2>
<p>The author is a father who works in auditing and training. Lessons are written with an AI assistant, sources are checked, and then the lessons are tried with his own family before publishing.
Results from one family are not scientific evidence; each course says so.</p>

<h2>About the translation</h2>
<p>The site is written in Vietnamese. English pages are translated with an AI assistant and reviewed by the author.
Some examples are adapted for families outside Vietnam. If the English and Vietnamese pages differ, the Vietnamese page is the reference.
If you see a translation error, please tell us through the <a href="/chia-se/" hreflang="vi">sharing page</a> (in Vietnamese; adults 18+).</p>

<h2 id="privacy">Privacy</h2>
<ul>
<li>The site uses no cookies, no tracking tools and no ads.</li>
<li>The site loads no fonts or code from other websites.</li>
<li>Tools on the site (if any) save data only on your device and send nothing anywhere.</li>
<li>When you choose a language (Tiếng Việt or English), your browser remembers that choice on your device. The site does not send it anywhere.</li>
<li>If your browser is not set to Vietnamese, the site asks Cloudflare one question: is this visit from Vietnam? The answer is only “yes” or “no”, used once to decide whether to suggest English. Nothing is stored.</li>
<li>Our hosting provider (Cloudflare) may keep basic technical logs to run the service and block attacks.</li>
</ul>
<p>The sharing page stores only what you write and choose to show; it never stores IP addresses, emails or phone numbers.
Full details are on the <a href="/gioi-thieu/#chia-se" hreflang="vi">Vietnamese privacy section</a>.</p>

<h2 id="licence">Licence</h2>
<p>Our own content is shared under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>:
you may print, share and adapt it for non-commercial use, credit daynentang.com and keep the same licence.
Materials from other organisations belong to them; we only link to them.</p>

<h2>Change log (English pages)</h2>
<ul>
<li>3 November 2026: First English pages: home, Family, Personal, About, Get help now, Evidence, and Week 1 of Family 2–8. The full change log is on the <a href="/gioi-thieu/" hreflang="vi">Vietnamese About page</a>.</li>
</ul>
''', current='/en/about/', lang='en')

# ======================= Bằng chứng =======================
EV_EN = [
 ('Parenting for Lifelong Health – young children: randomised trial with 296 caregivers in South Africa; observed positive parenting +39% after 4–5 months, +24% after 17 months', 'Verified', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7155004/', 'Ward et al. 2019'),
 ('PLH materials on the WHO website use the CC BY-NC-ND 4.0 licence (no derivatives), so we only link to them', 'Verified', 'https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health', 'WHO'),
 ('Social and emotional learning: meta-analysis of 424 studies in 53 countries, mostly in schools', 'Verified', 'https://eric.ed.gov/?id=EJ1394000', 'Cipriano et al. 2023'),
 ('Stories that praise a character for telling the truth made children aged 3–7 confess more; stories that threaten punishment did not work better', 'Verified', 'https://pubmed.ncbi.nlm.nih.gov/24928424/', 'Lee et al. 2014'),
 ('“Growth mindset” interventions have very small effects (d ≈ 0.02–0.05)', 'Verified', 'https://artscimedia.case.edu/wp-content/uploads/sites/141/2020/06/26110416/Macnamara-Burgoyne-2023.pdf', 'Macnamara & Burgoyne 2023'),
 ('Whole-school mindfulness (MYRIAD, 8,376 students) did not beat the comparison group after one year', 'Verified', 'https://www.kcl.ac.uk/news/schools-based-mindfulness-programme-improves-school-culture-and-reduces-teacher-burnout', 'Kuyken et al. 2022'),
 ('Age-based activities to build executive function skills', 'Verified', 'https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/', 'Harvard Center on the Developing Child'),
 ('Reach Up materials use the CC BY-NC-SA 4.0 licence', 'Verified', 'https://reachupandlearn.com/resources/', 'Reach Up'),
 ('Young children can drown in a few inches of water at home; keep them within arm’s reach', 'Verified', 'https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/', 'CPSC'),
 ('Morning chart and “Robot” game in Week 1 were designed by daynentang.com; no study of their own', 'Expert judgement', '', ''),
 ('Toilet-paper-tube test is a quick home check for small parts; it does not replace toy safety standards', 'Expert judgement', '', ''),
 ('Vietnam child protection hotline 111: free, 24/7', 'Verified', 'https://tongdai111.vn/', 'tongdai111.vn'),
 ('Ngày Mai hotline 096 306 1414: 13:00–20:30, Wednesday to Sunday', 'Verified', 'https://duongdaynongngaymai.vn/', 'duongdaynongngaymai.vn'),
]
def _src(u, s): return f'<a href="{u}">{s}</a>' if u else (s or 'Design or judgement of daynentang.com')
erows = ''.join(f'<tr><td>{c}</td><td><span class="label">[{l}]</span></td><td>{_src(u, s)}</td></tr>' for c, l, u, s in EV_EN)
page('/en/evidence/', 'Evidence and sources', 'Fact-check table: claims on daynentang.com, certainty labels and original sources.',
f'''
<h1>Evidence and sources</h1>
<p class="lead">Every important claim on the site carries one of four labels.</p>
<ul>
<li><strong>[Verified]</strong> – we have read the source; it is named next to the claim.</li>
<li><strong>[Inference]</strong> – drawn from a source, but the source does not say it directly.</li>
<li><strong>[Expert judgement]</strong> – the author’s view; no study of its own yet.</li>
<li><strong>[Needs checking]</strong> – no reliable source found yet.</li>
</ul>
<p>Correlation is never written as cause. This table covers the general claims and the English lessons.
The <a href="/bang-chung/" hreflang="vi">full table in Vietnamese</a> covers every course.</p>
<div class="table-wrap"><table>
<thead><tr><th>Claim</th><th>Label</th><th>Source</th></tr></thead>
<tbody>{erows}</tbody></table></div>
<p class="small muted">Checked 28 October 2026. Found an error? We correct it publicly in the change log on the About page.</p>
''', current='/en/evidence/', lang='en')

# ======================= Trang khóa G3 =======================
CB = '/en/courses/family-2-8/'
W1 = CB + 'week-1/'
T1, K1, G1 = W1 + 't1-i-can-do-it-myself/', W1 + 'k1-float-or-sink/', W1 + 'g1-honest-and-light/'
VB = '/khoa-hoc/gia-dinh-2-8/'
WEEKS_EN = [
 ('1', f'<a href="{T1}">I can do it myself</a>', f'<a href="{K1}">Float or sink?</a>', f'<a href="{G1}">Honest and light</a>', 'Older child: does the chosen job alone ≥4 of 7 days. Toddler: puts away 3 toys when reminded'),
 ('2', 'Try – fail – try again', 'Water: pour, measure, soak', 'Three thank-yous', 'Older: says “I’ll try another way”. Toddler: pours water from a small jug'),
 ('3', 'Look at the goal, then go', 'Bean seeds sprouting', 'Secret good deeds', 'Older: sets 1 goal and checks it. Toddler: picks 1 of 2 job pictures'),
 ('4', 'Before – During – After', 'How tall is the sprout?', 'Stop – Breathe – Talk', 'Older: draws a 3-step plan. Toddler: points to 2 feeling faces'),
 ('5', 'Important things first', 'Light and shadow', 'My own housework', 'Older: main job first ≥4 of 7 days. Toddler: tidies up with a song'),
 ('6', 'Red light – green light', 'Slopes and force', 'Owning and fixing mistakes', 'Older: stops on signal ≥8/10. Toddler: ≥5/10'),
 ('7', 'The talking stick', 'Mystery bag', 'Feelings detective', 'Older: repeats what someone said. Toddler: waits for a turn once'),
 ('8', 'Big sibling teaches', 'Weather around the house', 'Thanking workers', 'Older: teaches the sibling 1 task. Toddler: follows 1 step'),
 ('9', 'Grow well: sleep, food, movement', 'Dinosaurs and fossils', 'Walk slowly, eat slowly', 'Regular bedtime ≥5 of 7 days (both children)'),
 ('10', 'A calm-down corner', 'Design a boat that carries the most', 'Keeping small promises', 'Older: uses the calm corner once. Toddler: accepts a hug or breathing together'),
 ('11', 'The whole hand: a family vegetable pot', 'I ask – I test', 'Being kind to yourself', 'Older: asks a question and predicts. Toddler: names 3 plant parts'),
 ('12', 'Foundation Hand celebration', 'Family science fair', 'Review values, draw a wish', 'End-of-course review'),
]
rows = ''.join(f'<tr><td>{w}</td><td>{t}</td><td>{k}</td><td>{g}</td><td>{m}</td></tr>' for w, t, k, g, m in WEEKS_EN)

page(CB, 'Family 2–8: The Foundation Hand',
 'A free 12-week course for parents: teach children aged 2–8 self-reliant habits, hands-on science and kind values with things already at home.',
f'''
<p class="eyebrow">Family · Course G3 · Trial version</p>
<h1>Family 2–8: The Foundation Hand</h1>
<p class="lead">Parents, even one parent alone, build three foundations through 30 minutes of purposeful play:
self-reliant habits, a curious, testing mind, and kind values. And there is less shouting at home.</p>

<div class="table-wrap"><table>
<tbody>
<tr><th>For</th><td>Parents, grandparents and carers of children aged 2–8</td></tr>
<tr><th>Length</th><td>12 weeks × 3 sessions × 30 minutes. About 30 minutes of preparation per week</td></tr>
<tr><th>You need</th><td>Things already at home, paper, chunky crayons. Children need no screens</td></tr>
<tr><th>Status</th><td>All 12 weeks written in Vietnamese. Week 1 is translated and was tried in one family; weeks 2–12 are not yet tried</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Help now (1–2 weeks)</h3>
    <ul><li>A fun play time with your child every day.</li><li>Your child does at least one small job alone.</li><li>You have ready-made phrases to use instead of shouting.</li></ul></div>
  <div class="card"><h3>Build for the long term</h3>
    <ul><li>Executive function: attention, working memory, self-control.</li><li>The habit of asking, guessing and checking.</li><li>Honesty, gratitude, kindness, responsibility.</li></ul></div>
</div>

<h2>The Foundation Hand</h2>
<p>Five fingers are five habits. Children look at their own hand and remember.</p>
{figure_block_en('KHOA')}
<div class="table-wrap"><table>
<thead><tr><th>Finger</th><th>Habit</th></tr></thead>
<tbody>
<tr><td>Thumb</td><td>I can do it myself</td></tr>
<tr><td>Index finger</td><td>Look at the goal, then go</td></tr>
<tr><td>Middle finger</td><td>Important things first</td></tr>
<tr><td>Ring finger</td><td>Listen – understand – have fun together</td></tr>
<tr><td>Little finger</td><td>Grow well: sleep, food, movement, calm</td></tr>
</tbody></table></div>

<h2>The 12 weeks</h2>
<p>Three sessions each week: <strong>T</strong> Habits, <strong>K</strong> Hands-on science (Look → Guess → Try → Tell), <strong>G</strong> Values and mindfulness.
Week 1 is in English. For weeks 2–12, open the <a href="{VB}" hreflang="vi">Vietnamese course page</a>; your browser can translate it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Week</th><th>T – Habits</th><th>K – Science</th><th>G – Values</th><th>Measurable goal</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="small muted">“Older child” = about 7 years old; “toddler” = about 2 years old. Adjust to your own children’s ages.</p>

<h2>One 30-minute session</h2>
<ol>
<li><strong>Connect</strong> (0–3′): say hello, sit close. The toddler sits on your lap.</li>
<li><strong>Breathe for 1 minute</strong> (3–5′): “smell the flower – blow out the candle”.</li>
<li><strong>Main activity</strong> (5–20′): two levels, for the older child and the toddler.</li>
<li><strong>Child retells</strong> (20–25′): the toddler points, names or copies.</li>
<li><strong>Take it into daily life</strong> (25–30′): pick one thing to do this week, add a sticker.</li>
</ol>
<p>A 2-year-old joins for 10–15 minutes, then plays alongside. Don’t make them sit for the full 30 minutes.</p>

<h2>Track progress</h2>
<p>Score the <a href="/cong-cu/bang-quan-sat/" hreflang="vi">observation chart</a> <span class="vi-only">(Vietnamese)</span> at weeks 0, 6 and 12: 0 = not yet, 1 = with a reminder, 2 = on their own.
Also count, over 3 days, how often you give specific praise and how often you shout. This is self-tracking, not a test.</p>

<h2>Where the method comes from</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Idea we borrow</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td><a href="https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health">Parenting for Lifelong Health</a> (WHO/UNICEF)</td><td>One-to-one play, specific praise, clear instructions, non-violent consequences</td><td>{V} Randomised trial in South Africa (296 caregivers): observed positive parenting +39% after 4–5 months (Ward et al. 2019)</td></tr>
<tr><td><a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Executive function activities guide</a> (Harvard)</td><td>Games by age, 18–36 months and 5–7 years</td><td>{V} Expert guidance, not a randomised trial</td></tr>
<tr><td><a href="https://casel.org/what-is-sel/">CASEL</a></td><td>Naming goals after five social-emotional competencies</td><td>{V} Meta-analysis of 424 studies (Cipriano et al. 2023), mostly in schools</td></tr>
<tr><td><a href="https://reachupandlearn.com/resources/">Reach Up</a></td><td>Play with home-made toys for young children</td><td>{V} Long-term follow-up in Jamaica (Gertler et al.)</td></tr>
<tr><td>Lee, Talwar et al. 2014, <em>Psychological Science</em></td><td>Stories that praise honesty</td><td>{V} 268 children aged 3–7; short-term effect</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Limits, honestly</h3>
  <p>{I} Most of these programmes were tested in groups with a facilitator. Self-study at home has not been shown to work as well.
  This course is being tried in one family, with no comparison group. We make no promises about grades or IQ.</p>
</div>

<h2>Watch before you teach</h2>
<ul>
<li><a href="https://developingchild.harvard.edu/resources/videos/how-to-5-steps-for-brain-building-serve-and-return/">5 Steps for Brain-Building Serve and Return – Harvard Center on the Developing Child</a> (video)</li>
<li><a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Executive function activities guide – Harvard</a> (PDF)</li>
<li><a href="https://reachupandlearn.com/resources/">Reach Up – resources and videos</a></li>
</ul>

<h2>Safety for every session</h2>
<ul>
<li>Under 3s: keep small objects out of reach. Home tip: anything that fits through a toilet-paper tube is too small.</li>
<li>No button batteries, small magnets, plastic bags or sharp knives and scissors near the toddler.</li>
<li>Water play: an adult always within arm’s reach; empty the water right after.</li>
</ul>
{HELP_BOX_EN}
''', current='/en/family/', lang='en')

# ======================= Bài học =======================
JOURNAL_EN = '''<div class="table-wrap journal"><table><tbody>
<tr><th class="w38">What my child could do</th><td></td></tr>
<tr><th>What my child enjoyed</th><td></td></tr>
<tr><th>What to change</th><td></td></tr>
</tbody></table></div>'''

def sec(n, title, body):
    return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'

def lesson(path, code, title, desc, meta, sections, prev=None, nxt=None, vi_path=''):
    navl = f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else '<span></span>'
    navr = f'<a href="{nxt[0]}"{nxt[2] if len(nxt) > 2 else ""}>{nxt[1]} →</a>' if nxt else '<span></span>'
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{CB}">Family 2–8</a> · Week 1 · {code}</p>
<h1>{title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{PRINT_ROW_EN}
{''.join(sections[:3])}
{figure_block_en(code)}
{''.join(sections[3:])}
<div class="box share-cta no-print"><h3>Tried this lesson?</h3><p>Tell us what was hard or what worked, through our <a href="/chia-se/?bai=g3-{code.lower()}#gui" hreflang="vi">sharing page</a> (in Vietnamese, adults 18+).</p></div>
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Translated from Vietnamese · Updated 3 November 2026</p>
<nav class="lesson-nav no-print" aria-label="Previous and next lesson">{navl}{navr}</nav>
</div>'''
    page(path, f'{code} – {title}', desc, body, current='/en/family/', lang='en')

# ---------- T1 ----------
lesson(T1, 'T1', 'I can do it myself',
 'Lesson 1 of Family 2–8: the older child does a morning job alone, the toddler puts toys away. Includes a minute-by-minute plan for one parent.',
 ['Strand A – Habits (Thumb)', 'Week 1, session 1', '20–30 minutes'],
 [
 sec(1, 'Goals', '''<ul>
<li><strong>Older child (about 7):</strong> names all 4 steps of one morning job and picks 1 job to do alone this week.</li>
<li><strong>Toddler (about 2):</strong> puts 3 toys into a basket after one reminder.</li></ul>'''),
 sec(2, 'Get ready (5 minutes)', '''<ul>
<li>1 sheet of A4 paper and chunky crayons. No pens with small caps near the toddler.</li>
<li>1 basket and a few of the toddler’s big toys.</li>
<li>Tape or a large fridge magnet to put the chart up.</li></ul>'''),
 sec(3, 'Opening (2 minutes)', '<p>Hold up your thumb and ask: “This finger helps us hold things. What did you do by yourself this morning?” Everyone gives a thumbs-up when someone names a job.</p>'),
 sec(4, 'Main activity', '''<h3>Older child (15–20 minutes)</h3><ol>
<li><strong>Warm-up: “Dad says”</strong> (3 minutes): only do the action if the sentence starts with “Dad says” (or “Mum says”). Example: “Dad says touch your nose”, then “Touch your ear” (don’t move!).</li>
<li><strong>The Robot game</strong> (5 minutes): the parent is a robot and does exactly what the child says, step by step. The child tells the robot how to put on a jacket. The robot gets it wrong on purpose when a step is missing.</li>
<li><strong>Draw a “Morning chart”</strong> (7 minutes): the child draws 4–5 boxes, one job per box: get up, brush teeth, get dressed, eat breakfast, pack the school bag.</li>
<li><strong>Choose a job</strong> (3 minutes): the child circles 1 job that a parent usually does for them. This week the child does it alone.</li>
<li>Put the chart where the child sees it every morning.</li></ol>
<h3>Toddler (5–10 minutes)</h3><ol>
<li>Put 3 big toys on the floor with the basket nearby.</li>
<li>Sing slowly: “Toys go home, go home, go home” and put 1 toy away to show how.</li>
<li>Invite the toddler to put the other 2 away. When done, everyone gives a thumbs-up.</li>
<li>If the toddler doesn’t want to, hold their hand and put 1 toy away together, then stop.</li></ol>'''),
 sec(5, 'Questions to talk about', '''<ol>
<li>When the robot got it wrong, how did you feel? Why did it go wrong?</li>
<li>Which job would you like to do alone that nobody has let you try yet?</li>
<li>If you try by yourself and it doesn’t work yet, what will you do next?</li></ol>'''),
 sec(6, 'Safety', '''<ul>
<li>Toddler: use only toys and crayons that do not fit through a toilet-paper tube. Put away pen caps and broken crayon bits.</li>
<li>Robot game: clear a wide space with no sharp table corners nearby.</li></ul>'''),
 sec(7, 'For the parent teaching alone', '''<div class="mom">
<p><em>You only need: 1 sheet of paper, chunky crayons, 1 basket. 20 minutes in total.</em></p><ol>
<li><strong>Minutes 0–2 – Opening.</strong> Thumbs up: “What did you do by yourself this morning?” Everyone gives a thumbs-up for each job.</li>
<li><strong>Minutes 2–5 – “Mum says” / “Dad says”.</strong> Play as above. The older child can give the orders for one round.</li>
<li><strong>Minutes 5–12 – Draw the chart.</strong> Skip the Robot game if you are tired. The child draws 4–5 morning jobs.</li>
<li><strong>Minutes 12–15 – Choose a job.</strong> The child circles 1 job to do alone this week. Put the chart on the fridge.</li>
<li><strong>Minutes 15–20 – Toddler tidies up.</strong> Sing “Toys go home”, put 1 toy away to show, the toddler puts away 2.</li></ol>
<p><strong>When the child manages:</strong> “You worked hard at that yourself!” Praise the effort, not “you’re so clever”.</p>
<p><strong>When it doesn’t work yet:</strong> “Not yet. Do you want to try again, or shall I show you one step?”</p>
<p><strong>When the child is tired or fussy:</strong> stop at the current step. A half-drawn chart can still go on the fridge.</p>
<p><strong>Send the other parent one line:</strong> which job the child chose to do alone.</p></div>'''),
 sec(8, 'Review', '''<ul>
<li><strong>After 1 day:</strong> next morning, point to the chart: “Which job will you do yourself today?” The child ticks it.</li>
<li><strong>After 1 week:</strong> count the days the child did the chosen job alone. Pick a second job if the child wants.</li></ul>
<div class="box"><h3>From our trial session (28 October 2026)</h3><ul>
<li>The older child (7) did 3 of 5 morning jobs alone: brushing teeth, getting dressed, eating breakfast.</li>
<li>The child chose to move “putting toys away” from “parent helps” to “I do it” next week.</li>
<li>The child loved the “Dad says” and Robot games.</li></ul>
<p class="small muted">Notes from the author’s own family, with identifying details removed. One family is not enough to judge whether the lesson works.</p></div>'''),
 sec(9, 'After-session journal', JOURNAL_EN),
 sec(10, 'Sources and labels', f'''<ul>
<li>{V} “Simon says”-type games appear in the activity ideas for ages 5–7 from the <a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Harvard Center on the Developing Child</a>.</li>
<li>{E} The morning chart and the Robot game were designed by daynentang.com; there is no study of them.</li>
<li>{I} Praise effort rather than “clever”. “Growth mindset” interventions have only very small effects, so we pair the praise with concrete actions such as trying again or changing the approach.</li>
<li>{E} The toilet-paper-tube tip is a quick home check, not a replacement for toy safety standards.</li></ul>'''),
 ], prev=None, nxt=(K1, 'K1 – Float or sink?'))

# ---------- K1 ----------
lesson(K1, 'K1', 'Float or sink?',
 'Hands-on science: the child guesses, then tests which objects float or sink in a tub of water. Includes water safety and a plan for one parent.',
 ['Strand B – Hands-on science', 'Week 1, session 2', '25–30 minutes'],
 [
 sec(1, 'Goals', '''<ul>
<li><strong>Older child:</strong> guesses and then tests 8 objects, records the results, and can say “heavy things don’t always sink”.</li>
<li><strong>Toddler:</strong> drops objects into the water and says or points to “float” or “sink”.</li></ul>'''),
 sec(2, 'Get ready (5 minutes)', '''<ul>
<li>1 large plastic tub with water about 10–15 cm deep. Put it on an old bath towel on the floor.</li>
<li>8 big objects (all bigger than a toilet-paper tube): large metal spoon, empty plastic bottle with the cap on, full plastic bottle with the cap on, unpeeled orange, wooden toy block, plastic bowl, fist-sized stone, big Lego/Duplo brick.</li>
<li>1 sheet of paper with 3 columns: Object · My guess · Result.</li>
<li>1 plastic basket or colander to scoop things out.</li></ul>'''),
 sec(3, 'Opening (2 minutes)', '<p>Hold up the metal spoon and the empty bottle: “Which one is heavier? Which one will sink?” Let the child guess. Don’t give the answer yet.</p>'),
 sec(4, 'Main activity – Look → Guess → Try → Tell', '''<h3>Older child (20–25 minutes)</h3><ol>
<li><strong>Look:</strong> the child holds each object and says if it is heavy or light, hard or soft, hollow or solid.</li>
<li><strong>Guess:</strong> the child writes “F” (float) or “S” (sink) in the “My guess” column for all 8 objects.</li>
<li><strong>Try:</strong> the child drops each object in and records the result. A wrong guess gets a question mark, not a cross.</li>
<li><strong>Surprise comparison:</strong> put the empty bottle and the full bottle side by side. They look the same – why does the full bottle sit so much lower?</li>
<li><strong>Extra test:</strong> float the plastic bowl like a boat. The child adds Lego bricks one at a time. Count how many bricks it takes to sink the bowl.</li>
<li><strong>Tell:</strong> the child tells you the one thing that surprised them most.</li></ol>
<h3>Toddler (5–10 minutes)</h3><ol>
<li>Sit right next to the tub; the adult sits beside the toddler, hands within reach.</li>
<li>Hand over one object at a time: “Drop it!” Then say: “It floats!” or “It sinks, down to the bottom!”</li>
<li>Let the toddler scoop things out with the plastic basket.</li>
<li>Repeat the objects the toddler likes. Two-year-olds love repetition; that is how they learn.</li></ol>'''),
 sec(5, 'Questions to talk about', '''<ol>
<li>Which object did you guess wrong? What will you look at next time before you guess?</li>
<li>How are the empty bottle and the full bottle different?</li>
<li>What else at home would you like to test next time?</li></ol>'''),
 sec(6, 'Safety', '''<ul>
<li>An adult sits close, with the toddler always within arm’s reach. If the doorbell or phone rings, take the toddler with you.</li>
<li>Never let the older child watch the toddler at the tub.</li>
<li>When you finish: empty all the water straight away, turn the tub upside down and store it out of reach.</li>
<li>Wipe up spilled water at once so nobody slips.</li>
<li>Every object must be bigger than a toilet-paper tube. No marbles, bottle caps, batteries or small magnets.</li></ul>'''),
 sec(7, 'For the parent teaching alone', '''<div class="mom">
<p><em>You only need: a tub of water, an old towel, 5 objects (metal spoon, empty bottle, full bottle, orange, wooden block), paper and a pen. 20 minutes in total.</em></p>
<p><strong>Before you start:</strong> put your phone away and sit right by the tub. If you have to leave, stop the session and take the toddler with you.</p><ol>
<li><strong>Minutes 0–2 – Opening.</strong> Hold up the spoon and the empty bottle: “Which one will sink?” The child guesses; you don’t answer yet.</li>
<li><strong>Minutes 2–6 – Guess.</strong> The older child writes F or S for 5 objects. The toddler watches and holds each object.</li>
<li><strong>Minutes 6–12 – Try.</strong> The children take turns. The toddler drops, the older child records.</li>
<li><strong>Minutes 12–15 – Surprise.</strong> Float the empty and full bottles side by side. Ask: “Why are the two bottles different?”</li>
<li><strong>Minutes 15–18 – Tell.</strong> The older child shares one surprise. Photograph the record sheet for the other parent (never the children’s faces).</li>
<li><strong>Minutes 18–20 – Tidy up.</strong> Empty the water at once, turn the tub over, wipe the floor. The older child helps wipe.</li></ol>
<p><strong>If the child asks “why” and you’re not sure:</strong> “I don’t know yet either. Let’s write it down and ask later.” You don’t need the right answer straight away.</p>
<p><strong>A simple idea to share with the older child:</strong> things with a lot of air inside often float more easily. Big or heavy doesn’t always mean it sinks.</p>
<p><strong>Skip the “Extra test”</strong> (Lego in the bowl) if you are on your own. Save it for when both parents are home.</p></div>'''),
 sec(8, 'Review', '''<ul>
<li><strong>After 1 day:</strong> at bath time, hand the child one new (safe) object and ask “Float or sink?” before dropping it.</li>
<li><strong>After 1 week:</strong> look at the record sheet again. How many guesses were right? Test 3 new objects the child chooses.</li></ul>'''),
 sec(9, 'After-session journal', JOURNAL_EN),
 sec(10, 'Sources and labels', f'''<ul>
<li>{V} Young children can drown in just a few inches of water; keep them within arm’s reach, empty water after use, and don’t let older children supervise younger ones at bath time (<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">US Consumer Product Safety Commission</a>).</li>
<li>{E} We don’t predict the result for each object (for example, the orange). That is for the child to test.</li>
<li>{E} “Lots of air inside means it floats more easily” is a simple way of saying it for children, not a full definition of buoyancy.</li></ul>'''),
 ], prev=(T1, 'T1 – I can do it myself'), nxt=(G1, 'G1 – Honest and light'))

# ---------- G1 ----------
lesson(G1, 'G1', 'Honest and light',
 'A values lesson on honesty with the story “Ti the Dinosaur” and the Stop – Breathe – Tell skill. The story praises truth-telling and does not threaten.',
 ['Strand C – Values and mindfulness', 'Week 1, session 3', '20–30 minutes'],
 [
 sec(1, 'Goals', '''<ul>
<li><strong>Older child:</strong> retells the story of Ti the Dinosaur and practises owning up in 3 steps: stop – breathe – tell.</li>
<li><strong>Toddler:</strong> points or says “me” when asked who knocked down the block tower.</li></ul>'''),
 sec(2, 'Get ready (5 minutes)', '''<ul>
<li>The story below (printed or read from paper).</li>
<li>6–8 big wooden blocks or Duplo bricks, 1 cuddly cushion.</li>
<li>A quiet place to sit, TV off.</li></ul>'''),
 sec(3, 'Opening (2 minutes)', '<p>“Have you ever knocked something over or broken something? How did your tummy feel?” Listen to your child without comment.</p>'),
 sec(4, 'Main activity', '''<h3>Story: Ti the Dinosaur and Grandma’s flower pot</h3>
<blockquote class="story">
<p>Ti the Dinosaur loved running round and round Grandma’s garden. One day, Ti swished that big tail too hard. Grandma’s flower pot fell over and broke in two.</p>
<p>Ti stood very still. Ti’s tummy felt heavy, as if Ti had swallowed a stone. Ti thought: “Maybe I could run behind the house. Nobody would know.”</p>
<p>But Ti stopped. Ti took a big, deep breath, and let it out very slowly. Then Ti went inside and said quietly: “Grandma, my tail broke your flower pot. I’m sorry.”</p>
<p>Grandma gave Ti a hug: “Thank you for telling me the truth. A broken pot can be replaced. I’m so glad you told me.”</p>
<p>Together they moved the soil into a new pot. The flowers were still fresh. Ti’s tummy felt light again, as if Ti had just put the stone down.</p>
</blockquote>
<p class="small muted">A new story written for daynentang.com.</p>
<h3>Older child (15–20 minutes)</h3><ol>
<li><strong>Listen</strong> (4 minutes): read slowly. Pause where Ti thinks about running away and ask: “What do you think Ti will do?”</li>
<li><strong>Retell</strong> (4 minutes): the child retells the story in their own words. The cushion can be Ti.</li>
<li><strong>Practise Stop – Breathe – Tell</strong> (5 minutes): you give a situation, the child does the 3 steps. Example: “You spilled water on the table.” Child: stops, takes one breath, says “Dad, I spilled the water.”</li>
<li><strong>Swap roles</strong> (4 minutes): you “accidentally” knock something over and own up; the child plays Grandma and says: “Thank you for telling me the truth.”</li>
<li><strong>Our family rule</strong> (2 minutes): say it out loud together: “When we tell the truth, we say thank you. Then we fix it together.”</li></ol>
<h3>Toddler (5–10 minutes)</h3><ol>
<li>Build a 6-block tower together.</li>
<li>Let the toddler knock it down. Ask playfully: “Who knocked the tower down?”</li>
<li>The toddler points or says “me”. Smile: “Thank you for telling me! Let’s build it again.”</li>
<li>Repeat 3–4 times. The toddler learns “thank you for telling me” through play.</li></ol>'''),
 sec(5, 'Questions to talk about', '''<ol>
<li>When Ti thought about running away, how did Ti’s tummy feel? And after telling the truth?</li>
<li>What did Grandma do when Ti told the truth?</li>
<li>If you break something, what would you like us to say to you?</li></ol>'''),
 sec(6, 'Safety', '''<ul>
<li>Blocks must be bigger than a toilet-paper tube. Build on a rug, never taller than the toddler’s head.</li>
<li>This lesson uses no threats or punishment. If your child owns up to a real mistake during the session, say thank you first and fix it after.</li></ul>'''),
 sec(7, 'For the parent teaching alone', '''<div class="mom">
<p><em>You only need: the printed story, 6 blocks, 1 cushion. 20 minutes in total. Evening, before bedtime, works well.</em></p><ol>
<li><strong>Minutes 0–2 – Opening.</strong> Ask: “Have you ever broken something?” Just listen; don’t bring up your child’s old mistakes.</li>
<li><strong>Minutes 2–6 – Read the story.</strong> Read slowly. Where Ti thinks about running away, pause and ask: “What do you think Ti will do?”</li>
<li><strong>Minutes 6–10 – Toddler tower game.</strong> You build, the toddler knocks it down. Ask “Who knocked it down?”; the toddler points; you say thank you. The older child helps rebuild.</li>
<li><strong>Minutes 10–15 – Practise the 3 steps.</strong> Give 2 situations: “You dropped a bowl”, “You tore your sibling’s book”. The older child does: stop – breathe – tell.</li>
<li><strong>Minutes 15–18 – Swap roles.</strong> You pretend to knock something over; the older child plays Grandma and says: “Thank you for telling me the truth.”</li>
<li><strong>Minutes 18–20 – Our family rule.</strong> Everyone says: “When we tell the truth, we say thank you. Then we fix it together.”</li></ol>
<p><strong>The most important part:</strong> this week, whenever your child owns up to a real mistake, say “thank you for telling me the truth” first. Then fix it together.</p>
<p><strong>Avoid:</strong> threats like “your nose will grow if you lie” or “liars get punished”. Threatening stories don’t make children more honest (see sources).</p>
<p><strong>If the older child asks “Have you ever lied?”:</strong> answer honestly and briefly. For example: “Sometimes I was scared too. But after telling the truth, I felt lighter.”</p>
<p><strong>Send the other parent one line:</strong> which part of the story the child liked.</p></div>'''),
 sec(8, 'Review', '''<ul>
<li><strong>After 1 day:</strong> at bedtime, ask the child to retell one sentence from the Ti the Dinosaur story.</li>
<li><strong>After 1 week:</strong> ask “Was there a time this week you told the truth even though you were a bit scared?” If yes, thank them again.</li></ul>'''),
 sec(9, 'After-session journal', JOURNAL_EN),
 sec(10, 'Sources and labels', f'''<ul>
<li>{V} A study of 268 children aged 3–7: only the story in which the character was praised for telling the truth increased confessions; stories threatening the consequences of lying worked no better than an unrelated story (Lee, Talwar et al., <em>Psychological Science</em>, 2014; <a href="https://www.psychologicalscience.org/news/releases/moral-tales-with-positive-outcomes-motivate-kids-to-be-honest.html">APS summary</a>).</li>
<li>{V} When the story’s ending was changed to a negative one, the effect disappeared; long-term effects have not been tested (same source).</li>
<li>{I} “Thank first, fix after” applies this finding to family life; the study did not test this exact approach.</li>
<li>{E} “Ti the Dinosaur” is a completely new story; it borrows only the idea of praising the truth-teller.</li></ul>'''),
 ], prev=(K1, 'K1 – Float or sink?'),
 nxt=('/khoa-hoc/gia-dinh-2-8/tuan-2/t2-thu-sai-thu-lai/', 'Week 2: T2 – Try, fail, try again (Vietnamese)', ' hreflang="vi"'))

print('EN pages built')
