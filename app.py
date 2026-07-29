import streamlit as set_page_config
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(layout="wide")

# ضع كود الـ HTML الكامل بين الثلاث علامات اقتباس أدناه
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>SofaScore Live Clone</title>
    <style>
        /* ... هنا تضع كل كود الـ CSS السابق ... */
    </style>
</head>
<body>
    <!-- ... هنا تضع كل كود الـ HTML والـ JavaScript السابق ... -->
</body>
</html>
"""

# دالة Streamlit لعرض كود الـ HTML والأكواد البرمجية بداخله بشكل آمن
components.html(html_code, height=800, scroller=True)
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SofaScore Live Clone</title>
    <style>
        :root {
            --primary-color: #1a365d;
            --secondary-color: #2b6cb0;
            --bg-color: #f7fafc;
            --card-bg: #ffffff;
            --text-main: #2d3748;
            --text-muted: #718096;
            --live-color: #e53e3e;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); }
        header { background-color: var(--primary-color); color: white; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 24px; font-weight: bold; }
        .logo span { color: #4299e1; }
        
        .container { max-width: 1200px; margin: 20px auto; padding: 0 15px; display: grid; grid-template-columns: 1fr 3fr; gap: 20px; }
        .sidebar { background: var(--card-bg); padding: 15px; border-radius: 8px; height: fit-content; }
        .sidebar h3 { margin-bottom: 15px; font-size: 16px; border-bottom: 2px solid var(--bg-color); padding-bottom: 8px; }
        .league-list { list-style: none; }
        .league-item { padding: 10px 5px; cursor: pointer; border-radius: 4px; }
        .league-item:hover { background: var(--bg-color); }

        .main-content { display: flex; flex-direction: column; gap: 20px; }
        .filter-bar { background: var(--card-bg); padding: 12px; border-radius: 8px; display: flex; gap: 15px; }
        .filter-btn { background: var(--bg-color); border: none; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-weight: 500; }
        .filter-btn.active { background: var(--secondary-color); color: white; }

        .match-section { background: var(--card-bg); border-radius: 8px; overflow: hidden; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        .league-header { background: #edf2f7; padding: 12px 15px; font-weight: bold; font-size: 14px; }
        .match-row { display: grid; grid-template-columns: 90px 1fr 80px; padding: 15px; border-bottom: 1px solid #edf2f7; align-items: center; }
        
        .match-time { font-size: 13px; color: var(--text-muted); }
        .match-time.live { color: var(--live-color); font-weight: bold; animation: blink 1.5s infinite; }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }

        .teams-container { display: flex; flex-direction: column; gap: 8px; }
        .team { font-size: 15px; }
        .scores { display: flex; flex-direction: column; gap: 8px; align-items: center; font-weight: bold; }
        .score-live { color: var(--live-color); }
        
        .loading { padding: 20px; text-align: center; color: var(--text-muted); }

        @media (max-width: 768px) { .container { grid-template-columns: 1fr; } .sidebar { display: none; } }
    </style>
</head>
<body>

    <header>
        <div class="logo">Sofa<span>Score</span></div>
    </header>

    <div class="container">
        <aside class="sidebar">
            <h3>البطولات المدعومة مجاناً</h3>
            <ul class="league-list">
                <li class="league-item">🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي (PL)</li>
                <li class="league-item">🇪🇸 الدوري الإسباني (PD)</li>
                <li class="league-item">🇪🇺 دوري أبطال أوروبا (CL)</li>
                <li class="league-item">🇮🇹 الدوري الإيطالي (SA)</li>
            </ul>
        </aside>

        <main class="main-content">
            <div class="filter-bar">
                <button class="filter-btn active">مباريات اليوم الحقيقية 📅</button>
            </div>

            <!-- الحاوية الديناميكية التي سيتم حقن المباريات بداخلها عبر الجافاسكريبت -->
            <div id="matches-container">
                <div class="loading">جاري جلب المباريات الحية من الخادم...</div>
            </div>
        </main>
    </div>

    <script>
        // ضع كود الـ Token الخاص بك الذي استلمته من الموقع هنا مكان السلسلة النصية الفارغة
        const API_TOKEN = 'YOUR_API_TOKEN_HERE'; 
        const URL = 'https://football-data.org';

        async function fetchLiveScores() {
            try {
                // إرسال الطلب إلى خادم الـ API مع تمرير مفتاح التحقق في الـ Headers
                const response = await fetch(URL, {
                    headers: { 'X-Auth-Token': API_TOKEN }
                });
                
                if (!response.ok) throw new Error('فشل في جلب البيانات');
                
                const data = await response.json();
                renderMatches(data.matches);
            } catch (error) {
                document.getElementById('matches-container').innerHTML = 
                    `<div class="loading" style="color:red;">خطأ: تأكد من إضافة الـ API Token الخاص بك في الكود.</div>`;
            }
        }

        function renderMatches(matches) {
            const container = document.getElementById('matches-container');
            container.innerHTML = ''; // تنظيف شاشة التحميل

            if (matches.length === 0) {
                container.innerHTML = '<div class="loading">لا توجد مباريات مجدولة لليوم.</div>';
                return;
            }

            // تجميع المباريات حسب اسم الدوري لتبدو منظمة كـ Sofascore
            const groupedMatches = {};
            matches.forEach(match => {
                const leagueName = match.competition.name;
                if (!groupedMatches[leagueName]) groupedMatches[leagueName] = [];
                groupedMatches[leagueName].push(match);
            });

            // بناء عناصر الـ HTML وحقنها في الصفحة
            for (const league in groupedMatches) {
                let sectionHtml = `
                    <div class="match-section">
                        <div class="league-header">🏆 ${league}</div>
                `;

                groupedMatches[league].forEach(match => {
                    // معالجة حالة التوقيت والمباراة (مباشر، منتهية، مجدولة)
                    const isLive = match.status === 'IN_PLAY' || match.status === 'PAUSED';
                    const isFinished = match.status === 'FINISHED';
                    
                    let timeDisplay = new Date(match.utcDate).toLocaleTimeString('ar-EG', {hour: '2-digit', minute:'2-digit'});
                    let timeClass = "match-time";
                    
                    if (isLive) {
                        timeDisplay = "مباشر 🔴";
                        timeClass = "match-time live";
                    } else if (isFinished) {
                        timeDisplay = "منتهية";
                    }

                    // جلب الأهداف
                    const homeScore = match.score.fullTime.home !== null ? match.score.fullTime.home : '-';
                    const awayScore = match.score.fullTime.away !== null ? match.score.fullTime.away : '-';

                    sectionHtml += `
                        <div class="match-row">
                            <div class="${timeClass}">${timeDisplay}</div>
                            <div class="teams-container">
                                <div class="team">${match.homeTeam.name}</div>
                                <div class="team">${match.awayTeam.name}</div>
                            </div>
                            <div class="scores">
                                <div class="${isLive ? 'score-live' : ''}">${homeScore}</div>
                                <div class="${isLive ? 'score-live' : ''}">${awayScore}</div>
                            </div>
                        </div>
                    `;
                });

                sectionHtml += `</div>`;
                container.innerHTML += sectionHtml;
            }
        }

        // تشغيل الدالة فور تحميل الصفحة
        fetchLiveScores();

        // تحديث البيانات تلقائياً كل دقيقتين (120000 مللي ثانية) لضمان حيوية النتائج
        setInterval(fetchLiveScores, 120000);
    </script>
</body>
</html>
