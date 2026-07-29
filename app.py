<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SofaScore Clone - واجهة نتائج المباريات</title>
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

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
        }

        header {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
        }

        .logo span {
            color: #4299e1;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-weight: 500;
        }

        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 15px;
            display: grid;
            grid-template-columns: 1fr 3fr;
            gap: 20px;
        }

        .sidebar {
            background: var(--card-bg);
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            height: fit-content;
        }

        .sidebar h3 {
            margin-bottom: 15px;
            font-size: 16px;
            border-bottom: 2px solid var(--bg-color);
            padding-bottom: 8px;
        }

        .league-list {
            list-style: none;
        }

        .league-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 5px;
            cursor: pointer;
            border-radius: 4px;
            transition: background 0.2s;
        }

        .league-item:hover {
            background: var(--bg-color);
        }

        .main-content {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .filter-bar {
            background: var(--card-bg);
            padding: 12px;
            border-radius: 8px;
            display: flex;
            gap: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .filter-btn {
            background: var(--bg-color);
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: 500;
        }

        .filter-btn.active {
            background: var(--secondary-color);
            color: white;
        }

        .match-section {
            background: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .league-header {
            background: #edf2f7;
            padding: 12px 15px;
            font-weight: bold;
            font-size: 14px;
            display: flex;
            justify-content: space-between;
        }

        .match-row {
            display: grid;
            grid-template-columns: 80px 1fr 80px;
            padding: 15px;
            border-bottom: 1px solid #edf2f7;
            align-items: center;
            cursor: pointer;
        }

        .match-row:hover {
            background: #f7fafc;
        }

        .match-time {
            font-size: 14px;
            color: var(--text-muted);
        }

        .match-time.live {
            color: var(--live-color);
            font-weight: bold;
            animation: blink 1.5s infinite;
        }

        .teams-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .team {
            font-size: 15px;
        }

        .scores {
            display: flex;
            flex-direction: column;
            gap: 8px;
            align-items: center;
            font-weight: bold;
        }

        .score-live {
            color: var(--live-color);
        }

        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        @media (max-width: 768px) {
            .container { grid-template-columns: 1fr; }
            .sidebar { display: none; }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">Sofa<span>Score</span></div>
        <nav>
            <ul>
                <li><a href="#">كرة القدم</a></li>
                <li><a href="#">كرة السلة</a></li>
                <li><a href="#">التنس</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <aside class="sidebar">
            <h3>البطولات المفضلة</h3>
            <ul class="league-list">
                <li class="league-item">🏆 الدوري الإسباني</li>
                <li class="league-item">🏆 الدوري الإنجليزي</li>
                <li class="league-item">🏆 دوري أبطال أوروبا</li>
            </ul>
        </aside>

        <main class="main-content">
            <div class="filter-bar">
                <button class="filter-btn active">الكل</button>
                <button class="filter-btn">مباشر 🔴</button>
                <button class="filter-btn">المنتهية</button>
            </div>

            <div class="match-section">
                <div class="league-header">
                    <span>🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي الممتاز</span>
                </div>
                
                <div class="match-row">
                    <div class="match-time live">'74</div>
                    <div class="teams-container">
                        <div class="team">🔴 مانشستر يونايتد</div>
                        <div class="team">🔵 مانشستر سيتي</div>
                    </div>
                    <div class="scores">
                        <div class="score-live">2</div>
                        <div class="score-live">1</div>
                    </div>
                </div>
            </div>
        </main>
    </div>

</body>
</html>

