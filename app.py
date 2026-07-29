<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مفكرة النتائج - Live Scores</title>
    <!-- استخدام Tailwind CSS للتصميم -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- شريط التنقل العلوي -->
    <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-2 space-x-reverse">
                <span class="bg-emerald-500 text-slate-950 font-bold p-2 rounded-lg text-lg"><i class="fa-solid fa-futbol"></i></span>
                <h1 class="text-xl font-bold tracking-wider text-white">Goal<span class="text-emerald-500">Live</span></h1>
            </div>
            <div class="flex items-center space-x-4 space-x-reverse">
                <button class="text-slate-400 hover:text-white"><i class="fa-solid fa-bell text-xl"></i></button>
                <button class="text-slate-400 hover:text-white"><i class="fa-solid fa-magnifying-glass text-xl"></i></button>
            </div>
        </div>
    </header>

    <!-- شريط الأيام (التواريخ) -->
    <nav class="bg-slate-900/50 border-b border-slate-800 py-3">
        <div class="container mx-auto px-4 flex space-x-3 space-x-reverse overflow-x-auto no-scrollbar">
            <button class="px-4 py-2 bg-slate-800 rounded-xl text-sm font-semibold hover:bg-slate-700 whitespace-nowrap">أمس</button>
            <button class="px-4 py-2 bg-emerald-600 text-white rounded-xl text-sm font-semibold whitespace-nowrap shadow-lg shadow-emerald-900/50">اليوم</button>
            <button class="px-4 py-2 bg-slate-800 rounded-xl text-sm font-semibold hover:bg-slate-700 whitespace-nowrap">غداً</button>
            <button class="px-4 py-2 bg-slate-800 rounded-xl text-sm font-semibold hover:bg-slate-700 whitespace-nowrap">الخميس، 30 يوليو</button>
            <button class="px-4 py-2 bg-slate-800 rounded-xl text-sm font-semibold hover:bg-slate-700 whitespace-nowrap">الجمعة، 31 يوليو</button>
        </div>
    </nav>

    <!-- المحتوى الرئيسي: المباريات -->
    <main class="container mx-auto px-4 py-6 flex-grow max-w-3xl">
        
        <!-- قسم البطولة -->
        <div class="mb-6">
            <div class="flex items-center space-x-2 space-x-reverse mb-3">
                <i class="fa-solid fa-trophy text-amber-400"></i>
                <h2 class="font-bold text-slate-200">الدوري الإنجليزي الممتاز</h2>
            </div>

            <!-- بطاقة المباراة الأولى -->
            <div class="bg-slate-800/60 rounded-2xl p-4 mb-3 border border-slate-700/50 hover:border-slate-600 transition shadow-sm">
                <div class="flex justify-between items-center text-xs text-slate-400 mb-2">
                    <span class="bg-red-500/10 text-red-400 px-2 py-0.5 rounded-full font-semibold animate-pulse">مباشر 78'</span>
                    <span>الدوري الإنجليزي</span>
                </div>
                <div class="flex justify-between items-center">
                    <!-- الفريق الأول -->
                    <div class="flex items-center space-x-3 space-x-reverse w-1/3">
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">ARS</span>
                        <span class="font-semibold text-sm truncate">آرسنال</span>
                    </div>
                    <!-- النتيجة -->
                    <div class="flex items-center space-x-3 space-x-reverse bg-slate-900/80 px-4 py-2 rounded-xl">
                        <span class="text-lg font-bold text-emerald-400">2</span>
                        <span class="text-slate-500">-</span>
                        <span class="text-lg font-bold text-slate-200">1</span>
                    </div>
                    <!-- الفريق الثاني -->
                    <div class="flex items-center justify-end space-x-3 space-x-reverse w-1/3 text-left">
                        <span class="font-semibold text-sm truncate">تشيلسي</span>
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">CHE</span>
                    </div>
                </div>
            </div>

            <!-- بطاقة المباراة الثانية -->
            <div class="bg-slate-800/60 rounded-2xl p-4 mb-3 border border-slate-700/50 hover:border-slate-600 transition shadow-sm">
                <div class="flex justify-between items-center text-xs text-slate-400 mb-2">
                    <span class="text-slate-400">22:00</span>
                    <span>الدوري الإنجليزي</span>
                </div>
                <div class="flex justify-between items-center">
                    <div class="flex items-center space-x-3 space-x-reverse w-1/3">
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">MCI</span>
                        <span class="font-semibold text-sm truncate">مانشستر سيتي</span>
                    </div>
                    <div class="flex items-center space-x-3 space-x-reverse bg-slate-900/80 px-4 py-2 rounded-xl">
                        <span class="text-sm font-bold text-slate-400">VS</span>
                    </div>
                    <div class="flex items-center justify-end space-x-3 space-x-reverse w-1/3 text-left">
                        <span class="font-semibold text-sm truncate">ليفربول</span>
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">LIV</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- قسم بطولة أخرى -->
        <div class="mb-6">
            <div class="flex items-center space-x-2 space-x-reverse mb-3">
                <i class="fa-solid fa-trophy text-amber-400"></i>
                <h2 class="font-bold text-slate-200">دوري أبطال أوروبا</h2>
            </div>

            <!-- بطاقة مباراة انتهت -->
            <div class="bg-slate-800/60 rounded-2xl p-4 mb-3 border border-slate-700/50 hover:border-slate-600 transition shadow-sm">
                <div class="flex justify-between items-center text-xs text-slate-400 mb-2">
                    <span class="text-slate-500 font-semibold">انتهت</span>
                    <span>دور المجموعات</span>
                </div>
                <div class="flex justify-between items-center">
                    <div class="flex items-center space-x-3 space-x-reverse w-1/3">
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">RMA</span>
                        <span class="font-semibold text-sm truncate">ريال مدريد</span>
                    </div>
                    <div class="flex items-center space-x-3 space-x-reverse bg-slate-900/80 px-4 py-2 rounded-xl">
                        <span class="text-lg font-bold text-slate-200">3</span>
                        <span class="text-slate-500">-</span>
                        <span class="text-lg font-bold text-slate-200">1</span>
                    </div>
                    <div class="flex items-center justify-end space-x-3 space-x-reverse w-1/3 text-left">
                        <span class="font-semibold text-sm truncate">بايرن ميونخ</span>
                        <span class="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center font-bold text-xs">BAY</span>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- شريط التنقل السفلي (التطبيقات الشبيهة بـ Sofascore) -->
    <footer class="bg-slate-900 border-t border-slate-800 sticky bottom-0 z-50">
        <div class="container mx-auto px-4 py-2 flex justify-around items-center">
            <button class="flex flex-col items-center text-emerald-500">
                <i class="fa-solid fa-futbol text-lg"></i>
                <span class="text-xs mt-1">المباريات</span>
            </button>
            <button class="flex flex-col items-center text-slate-400 hover:text-white">
                <i class="fa-solid fa-chart-line text-lg"></i>
                <span class="text-xs mt-1">الإحصائيات</span>
            </button>
            <button class="flex flex-col items-center text-slate-400 hover:text-white">
                <i class="fa-solid fa-star text-lg"></i>
                <span class="text-xs mt-1">المفضلة</span>
            </button>
            <button class="flex flex-col items-center text-slate-400 hover:text-white">
                <i class="fa-solid fa-user text-lg"></i>
                <span class="text-xs mt-1">حسابي</span>
            </button>
        </div>
    </footer>

</body>
</html>

