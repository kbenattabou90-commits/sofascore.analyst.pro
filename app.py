<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحليلات كرة القدم الذكية - Sofascore Analyst Style</title>
    <style>
        :root {
            --primary: #1a237e;
            --secondary: #00e676;
            --dark: #0f172a;
            --light: #f8fafc;
            --gray: #64748b;
            --card-bg: #ffffff;
            --border: #e2e8f0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        /* الهيدر وشريط التنقل */
        header {
            background-color: var(--dark);
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--secondary);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-links {
            display: flex;
            gap: 20px;
            list-style: none;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
            cursor: pointer;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--secondary);
        }

        /* الحاويات الأساسية للمراحل */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .section {
            display: none;
        }

        .section.active {
            display: block;
        }

        /* المرحلة الأولى: مرحلة الدخول والترحيب */
        .hero {
            text-align: center;
            padding: 4rem 1rem;
            background: linear-gradient(135deg, var(--dark), var(--primary));
            color: white;
            border-radius: 16px;
            margin-bottom: 2rem;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            color: #cbd5e1;
            max-width: 700px;
            margin: 0 auto 2rem;
        }

        .btn {
            background-color: var(--secondary);
            color: var(--dark);
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
        }

        .btn:hover {
            background-color: #00c853;
            transform: translateY(-2px);
        }

        /* مرحلة المباريات والبطولات */
        .matches-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
        }

        .match-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .match-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 15px rgba(0,0,0,0.1);
        }

        .match-header {
            display: flex;
            justify-content: space-between;
            color: var(--gray);
            font-size: 0.85rem;
            margin-bottom: 1rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.5rem;
        }

        .live-badge {
            background-color: #ef4444;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        .teams-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .team {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 40%;
            text-align: center;
        }

        .team img {
            width: 50px;
            height: 50px;
            object-fit: contain;
            margin-bottom: 0.5rem;
        }

        .team span {
            font-weight: 600;
            font-size: 0.95rem;
        }

        .match-score {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary);
        }

        /* احتمالات الذكاء الاصطناعي */
        .ai-probabilities {
            background-color: #f1f5f9;
            padding: 0.8rem;
            border-radius: 8px;
            font-size: 0.85rem;
        }

        .prob-bar {
            display: flex;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 6px;
            background: #cbd5e1;
        }

        .prob-home { background-color: #3b82f6; }
        .prob-draw { background-color: #94a3b8; }
        .prob-away { background-color: #ef4444; }

        .prob-labels {
            display: flex;
            justify-content: space-between;
            margin-top: 4px;
            color: var(--gray);
            font-size: 0.75rem;
        }

        /* جدول ترتيب الفرق */
        .standings-table {
            width: 100%;
            background: var(--card-bg);
            border-radius: 12px;
            border-collapse: collapse;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-top: 1rem;
        }

        .standings-table th, .standings-table td {
            padding: 1rem;
            text-align: right;
            border-bottom: 1px solid var(--border);
        }

        .standings-table th {
            background-color: var(--dark);
            color: white;
            font-size: 0.9rem;
        }

        .standings-table tr:hover {
            background-color: #f8fafc;
        }

        .team-cell {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .team-cell img {
            width: 24px;
            height: 24px;
        }

        /* مرحلة الكشف العميق والتحليل المفصل */
        .analysis-view {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .back-btn {
            background: none;
            border: 1px solid var(--border);
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 1.5rem;
            font-weight: bold;
        }

        /* الإعدادات والموافقة */
        .settings-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 12px;
            max-width: 600px;
            margin: 0 auto;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        .setting-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            border-bottom: 1px solid var(--border);
        }

        /* التجاوب */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-in {
            animation: fadeIn 0.4s ease forwards;
        }
    </style>
</head>
<body>

    <!-- شريط التنقل العلوي -->
    <header>
        <div class="logo">
            🤖 Sofascore Analyst AI
        </div>
        <ul class="nav-links">
            <li><a onclick="switchSection('home')" class="active">الرئيسية</a></li>
            <li><a onclick="switchSection('matches')">المباريات واللايف</a></li>
            <li><a onclick="switchSection('standings')">ترتيب الفرق</a></li>
            <li><a onclick="switchSection('settings')">الإعدادات</a></li>
        </ul>
    </header>

    <div class="container">

        <!-- 1. مرحلة الدخول (الرئيسية) -->
        <div id="home" class="section active fade-in">
            <div class="hero">
                <h1>رؤى الخبراء في لمحة</h1>
                <p>أداة تحليل متطورة تحول الإحصائيات المعقدة إلى رؤى واضحة باستخدام خوارزميات الذكاء الاصطناعي المتقدمة لتوقع المباريات قبل انطلاقها وحتى بين الشوطين.</p>
                <button class="btn" onclick="switchSection('matches')">استكشف المباريات والتوقعات الآن</button>
            </div>
        </div>

        <!-- 2. مرحلة المباريات واللايف والتوقعات -->
        <div id="matches" class="section fade-in">
            <h2 style="margin-bottom: 1.5rem;">مباريات اليوم والتوقعات الحية</h2>
            <div class="matches-grid">
                
                <!-- مباراة 1 -->
                <div class="match-card" onclick="openAnalysis('ريال مدريد', 'برشلونة', 'https://upload.wikimedia.org/wikipedia/sco/thumb/5/56/Real_Madrid_CF.svg/512px-Real_Madrid_CF.svg.png', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/512px-FC_Barcelona_%28crest%29.svg.png')">
                    <div class="match-header">
                        <span>الدوري الإسباني - الجولة 30</span>
                        <span class="live-badge">مباشر 65'</span>
                    </div>
                    <div class="teams-row">
                        <div class="team">
                            <img src="https://upload.wikimedia.org/wikipedia/sco/thumb/5/56/Real_Madrid_CF.svg/512px-Real_Madrid_CF.svg.png" alt="ريال مدريد">
                            <span>ريال مدريد</span>
                        </div>
                        <div class="match-score">2 - 1</div>
                        <div class="team">
                            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/512px-FC_Barcelona_%28crest%29.svg.png" alt="برشلونة">
                            <span>برشلونة</span>
                        </div>
                    </div>
                    <div class="ai-probabilities">
                        <span>توقع الذكاء الاصطناعي للنتيجة النهائية:</span>
                        <div class="prob-bar">
                            <div class="prob-home" style="width: 58%;"></div>
                            <div class="prob-draw" style="width: 22%;"></div>
                            <div class="prob-away" style="width: 20%;"></div>
                        </div>
                        <div class="prob-labels">
                            <span>فوز (58%)</span>
                            <span>تعادل (22%)</span>
                            <span>خسارة (20%)</span>
                        </div>
                    </div>
                </div>

                <!-- مباراة 2 -->
                <div class="match-card" onclick="openAnalysis('مانشستر سيتي', 'أرسنال', 'https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/512px-Manchester_City_FC_badge.svg.png', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/512px-Arsenal_FC.svg.png')">
                    <div class="match-header">
                        <span>الدوري الإنجليزي - غدًا 21:00</span>
                        <span style="color: var(--primary); font-weight: bold;">تحليل متاح</span>
                    </div>
                    <div class="teams-row">
                        <div class="team">
                            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/512px-Manchester_City_FC_badge.svg.png" alt="مانشستر سيتي">
                            <span>مانشستر سيتي</span>
                        </div>
                        <div class="match-score">VS</div>
                        <div class="team">
                            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/512px-Arsenal_FC.svg.png" alt="أرسنال">
                            <span>أرسنال</span>
                        </div>
                    </div>
                    <div class="ai-probabilities">
                        <span>احتمالات النموذج الذكي (قبل المباراة):</span>
                        <div class="prob-bar">
                            <div class="prob-home" style="width: 45%;"></div>
                            <div class="prob-draw" style="width: 30%;"></div>
                            <div class="prob-away" style="width: 25%;"></div>
                        </div>
                        <div class="prob-labels">
                            <span>فوز (45%)</span>
                            <span>تعادل (30%)</span>
                            <span>خسارة (25%)</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- 3. مرحلة كشف الفريق والتحليل المعمق (تظهر ديناميكياً) -->
        <div id="analysis-view" class="section">
            <button class="back-btn" onclick="switchSection('matches')">← العودة للمباريات</button>
            <div class="analysis-view" id="analysis-content">
                <!-- يتم تعبئتها عبر الجافاسكريبت -->
            </div>
        </div>

        <!-- 4. مرحلة ترتيب الفرق وصور الأندية الواضحة -->
        <div id="standings" class="section fade-in">
            <h2 style="margin-bottom: 1rem;">جدول الترتيب العالمي والأنظمة الذكية</h2>
            <table class="standings-table">
                <thead>
                    <tr>
                        <th>المركز</th>
                        <th>الفريق</th>
                        <th>لعب</th>
                        <th>فاز</th>
                        <th>تعادل</th>
                        <th>خسر</th>
                        <th>النقاط</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>
                            <div class="team-cell">
                                <img src="https://upload.wikimedia.org/wikipedia/sco/thumb/5/56/Real_Madrid_CF.svg/512px-Real_Madrid_CF.svg.png" alt="ريال مدريد">
                                <span>ريال مدريد</span>
                            </div>
                        </td>
                        <td>30</td>
                        <td>23</td>
                        <td>5</td>
                        <td>2</td>
                        <td><strong>74</strong></td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>
                            <div class="team-cell">
                                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/512px-FC_Barcelona_%28crest%29.svg.png" alt="برشلونة">
                                <span>برشلونة</span>
                            </div>
                        </td>
                        <td>30</td>
                        <td>21</td>
                        <td>6</td>
                        <td>3</td>
                        <td><strong>69</strong></td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>
                            <div class="team-cell">
                                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/512px-Manchester_City_FC_badge.svg.png" alt="مانشستر سيتي">
                                <span>مانشستر سيتي</span>
                            </div>
                        </td>
                        <td>29</td>
                        <td>20</td>
                        <td>6</td>
                        <td>3</td>
                        <td><strong>66</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- 5. مرحلة الإعدادات والموافقة -->
        <div id="settings" class="section fade-in">
            <div class="settings-card">
                <h2 style="margin-bottom: 1.5rem;">إعدادات التطبيق والموافقات</h2>
                <div class="setting-item">
                    <span>تنبيهات الذكاء الاصطناعي والتوقعات الحية</span>
                    <input type="checkbox" checked style="width: 20px; height: 20px; accent-color: var(--secondary);">
                </div>
                <div class="setting-item">
                    <span>تحديثات تحليل ما بين الشوطين</span>
                    <input type="checkbox" checked style="width: 20px; height: 20px; accent-color: var(--secondary);">
                </div>
                <div class="setting-item">
                    <span>الوضع الليلي / المظهر الداكن</span>
                    <input type="checkbox" style="width: 20px; height: 20px; accent-color: var(--secondary);">
                </div>
                <button class="btn" style="width: 100%; margin-top: 1.5rem;" onclick="alert('تم حفظ الإعدادات والموافقات بنجاح!')">حفظ التغييرات</button>
            </div>
        </div>

    </div>

    <script>
        // دالة التنقل السلس بين الأقسام والمراحل المختلفة
        function switchSection(sectionId) {
            const sections = document.querySelectorAll('.section');
            sections.forEach(sec => sec.classList.remove('active'));

            const target = document.getElementById(sectionId);
            if (target) {
                target.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            // تحديث الروابط النشطة في الهيدر
            const navLinks = document.querySelectorAll('.nav-links a');
            navLinks.forEach(link => link.classList.remove('active'));
        }

        // دالة فتح مرحلة الكشف العميق عن الفريق وتحليل المباراة بالتفصيل
        function openAnalysis(teamHome, teamAway, logoHome, logoAway) {
            const analysisView = document.getElementById('analysis-view');
            const content = document.getElementById('analysis-content');

            content.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                    <div style="text-align: center; width: 40%;">
                        <img src="${logoHome}" width="80" height="80" style="object-fit: contain; margin-bottom: 10px;">
                        <h3>${teamHome}</h3>
                    </div>
                    <h1 style="color: var(--primary);">VS</h1>
                    <div style="text-align: center; width: 40%;">
                        <img src="${logoAway}" width="80" height="80" style="object-fit: contain; margin-bottom: 10px;">
                        <h3>${teamAway}</h3>
                    </div>
                </div>
                <hr style="border: 0; border-top: 1px solid var(--border); margin: 1.5rem 0;">
                <h3 style="margin-bottom: 1rem; color: var(--primary);">📊 تقرير الذكاء الاصطناعي العميق</h3>
                <p style="margin-bottom: 1rem; color: var(--gray);">تقوم خوارزمياتنا بمحاكاة هذه المباراة آلاف المرات بناءً على الأداء السابق، الإصابات، وأنماط الحكام:</p>
                <ul style="padding-right: 20px; margin-bottom: 1.5rem; line-height: 1.8;">
                    <li><strong>احتمالية الفوز والاستحواذ:</strong> تشير البيانات المتقدمة إلى تفوق طفيف للفريق المستضيف بنسبة ضغط هجومي تصل إلى 64%.</li>
                    <li><strong>أنماط الأهداف المتوقعة:</strong> احتمالية تسجيل أكثر من
