import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:\Users\rauko\Desktop\GIT\SDLC\srs\images"
os.makedirs(output_dir, exist_ok=True)

# Try standard Windows fonts
def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\tahomabd.ttf" if bold else "C:\\Windows\\Fonts\\tahoma.ttf",
    ]
    for path in font_names:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

f_title = get_font(20, True)
f_h1 = get_font(16, True)
f_h2 = get_font(14, True)
f_h3 = get_font(12, True)
f_body = get_font(12, False)
f_body_b = get_font(12, True)
f_small = get_font(10, False)
f_small_b = get_font(10, True)

# ==============================================================================
# 1. UI Mockup: Recipes Catalog (gui_mockup_recipes.png)
# ==============================================================================
W, H = 1200, 750
img = Image.new("RGB", (W, H), "#F1F5F9")
draw = ImageDraw.Draw(img)

# Window Header
draw.rectangle([(0, 0), (W, 42)], fill="#1E293B")
draw.text((20, 11), "Recipe & Meal Planner System v1.0 [C++/Qt] — Управление базой рецептов", fill="#FFFFFF", font=f_h2)
# Window buttons
draw.ellipse([(1160, 14), (1176, 30)], fill="#EF4444")
draw.ellipse([(1135, 14), (1151, 30)], fill="#F59E0B")
draw.ellipse([(1110, 14), (1126, 30)], fill="#10B981")

# Tabs Bar
draw.rectangle([(20, 52), (1180, 95)], fill="#FFFFFF", outline="#CBD5E1", width=1)
# Tab 1: Active
draw.rectangle([(25, 56), (220, 91)], fill="#2563EB")
draw.text((45, 65), "Книга рецептов", fill="#FFFFFF", font=f_h3)
# Tab 2
draw.rectangle([(230, 56), (465, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((250, 65), "План меню на неделю", fill="#475569", font=f_h3)
# Tab 3
draw.rectangle([(475, 56), (690, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((500, 65), "Список покупок", fill="#475569", font=f_h3)

# --- LEFT PANEL: Catalog (Width: 380) ---
draw.rectangle([(20, 105), (400, 705)], fill="#FFFFFF", outline="#CBD5E1", width=1)
draw.text((35, 118), "Каталог рецептов", fill="#0F172A", font=f_h1)

# Search box
draw.rectangle([(35, 150), (385, 182)], fill="#F8FAFC", outline="#94A3B8", width=1)
draw.text((45, 157), "Поиск по названию или ингредиенту...", fill="#94A3B8", font=f_small)

# Filter Pills
cats = [("Все", True), ("Супы", False), ("Вторые", False), ("Салаты", False), ("Десерты", False)]
cx = 35
for cname, active in cats:
    bg = "#2563EB" if active else "#F1F5F9"
    fg = "#FFFFFF" if active else "#475569"
    draw.rectangle([(cx, 192), (cx + 62, 218)], fill=bg, outline="#CBD5E1")
    draw.text((cx + 10, 198), cname, fill=fg, font=f_small_b if active else f_small)
    cx += 70

# Recipes list
recipes = [
    ("Борщ украинский с говядиной", "Супы", "90 мин", True),
    ("Паста Карбонара с беконом", "Вторые блюда", "30 мин", False),
    ("Куриное филе с брокколи", "Вторые блюда", "40 мин", False),
    ("Салат Цезарь с цыпленком", "Салаты", "25 мин", False),
    ("Овсяная каша с яблоками", "Завтраки", "15 мин", False),
    ("Семга запеченная с травами", "Вторые блюда", "35 мин", False),
    ("Греческий салат с фетой", "Салаты", "20 мин", False),
    ("Крем-суп из шампиньонов", "Супы", "40 мин", False)
]

ry = 230
for name, cat, dur, sel in recipes:
    bg = "#EFF6FF" if sel else "#FFFFFF"
    border = "#3B82F6" if sel else "#E2E8F0"
    draw.rectangle([(35, ry), (385, ry + 46)], fill=bg, outline=border, width=1)
    draw.text((45, ry + 6), name, fill="#1E293B" if not sel else "#1D4ED8", font=f_body_b if sel else f_body)
    draw.text((45, ry + 26), f"Категория: {cat}   •   Время: {dur}", fill="#64748B", font=f_small)
    ry += 52

# Buttons at bottom of left panel
draw.rectangle([(35, 655), (195, 693)], fill="#10B981")
draw.text((50, 665), "+ Новый рецепт", fill="#FFFFFF", font=f_h3)

draw.rectangle([(210, 655), (385, 693)], fill="#EF4444")
draw.text((245, 665), "- Удалить блюдо", fill="#FFFFFF", font=f_h3)

# --- RIGHT PANEL: Recipe Details ---
draw.rectangle([(415, 105), (1180, 705)], fill="#FFFFFF", outline="#CBD5E1", width=1)

# Header details
draw.text((440, 120), "Борщ украинский с говядиной", fill="#0F172A", font=f_title)
draw.text((440, 150), "Категория: Первые блюда / Супы   |   Время приготовления: 90 мин   |   Выход: 6 порций", fill="#64748B", font=f_body)

draw.rectangle([(1030, 125), (1160, 158)], fill="#2563EB")
draw.text((1045, 133), "Редактировать", fill="#FFFFFF", font=f_h3)

draw.line([(440, 180), (1160, 180)], fill="#E2E8F0", width=1)

# Left Column in Details: Ingredients
draw.text((440, 195), "Ингредиенты (Состав рецепта):", fill="#1E293B", font=f_h2)
ingredients = [
    ("Говядина на кости (бульон)", "600", "г"),
    ("Картофель свежий", "400", "г"),
    ("Капуста белокочанная", "350", "г"),
    ("Свекла столовая свежая", "250", "г"),
    ("Морковь", "150", "г"),
    ("Лук репчатый", "120", "г"),
    ("Томатная паста", "50", "г"),
    ("Чеснок свежий", "4", "зубч."),
    ("Зелень укропа и петрушки", "30", "г"),
    ("Соль, перец, лавровый лист", "по вкусу", "")
]

iy = 225
for ing, qty, unit in ingredients:
    draw.rectangle([(440, iy), (760, iy + 30)], fill="#F8FAFC", outline="#E2E8F0", width=1)
    draw.text((450, iy + 7), ing, fill="#334155", font=f_body)
    draw.text((700, iy + 7), f"{qty} {unit}", fill="#0F172A", font=f_body_b)
    iy += 36

# Right Column in Details: Cooking Steps
draw.text((790, 195), "Пошаговая инструкция приготовления:", fill="#1E293B", font=f_h2)
steps = [
    "1. Мясо промыть, залить 3 л холодной воды, довести до кипения. Варить бульон на медленном огне 60 минут, снимая пену.",
    "2. Свеклу нарезать соломкой, тушить на сковороде с томатной пастой и ложкой лимонного сока 15 минут.",
    "3. Морковь и лук спассеровать на растительном масле до мягкости и золотистого оттенка.",
    "4. В кипящий бульон выложить нарезанный кубиками картофель, варить 10 минут.",
    "5. Добавить нашинкованную капусту и тушеную свеклу, варить еще 10 минут.",
    "6. Добавить пассеровку, измельченный чеснок, лавровый лист и специи. Варить 5 минут, затем дать настояться 20 минут под крышкой."
]

sy = 225
for step in steps:
    # Wrap step across lines
    words = step.split(' ')
    line1, line2 = "", ""
    for w in words:
        if len(line1 + " " + w) < 48:
            line1 += (" " if line1 else "") + w
        else:
            line2 += (" " if line2 else "") + w
    draw.text((790, sy), line1, fill="#334155", font=f_body)
    if line2:
        draw.text((805, sy + 18), line2, fill="#334155", font=f_body)
    sy += 44

# Status bar at bottom
draw.rectangle([(0, 720), (W, 750)], fill="#E2E8F0")
draw.text((20, 727), "Статус: Файл recipes.json загружен успешно. Рецептов в базе: 24 | Текущий режим: Просмотр", fill="#475569", font=f_small)

img.save(os.path.join(output_dir, "gui_mockup_recipes.png"))
print("Generated clean gui_mockup_recipes.png")


# ==============================================================================
# 2. UI Mockup: Meal Planner (gui_mockup_planner.png)
# ==============================================================================
img = Image.new("RGB", (W, H), "#F1F5F9")
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (W, 42)], fill="#1E293B")
draw.text((20, 11), "Recipe & Meal Planner System v1.0 [C++/Qt] — Календарь планирования меню", fill="#FFFFFF", font=f_h2)
draw.ellipse([(1160, 14), (1176, 30)], fill="#EF4444")
draw.ellipse([(1135, 14), (1151, 30)], fill="#F59E0B")
draw.ellipse([(1110, 14), (1126, 30)], fill="#10B981")

# Tabs Bar
draw.rectangle([(20, 52), (1180, 95)], fill="#FFFFFF", outline="#CBD5E1", width=1)
draw.rectangle([(25, 56), (220, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((45, 65), "Книга рецептов", fill="#475569", font=f_h3)

draw.rectangle([(230, 56), (465, 91)], fill="#2563EB")
draw.text((250, 65), "План меню на неделю", fill="#FFFFFF", font=f_h3)

draw.rectangle([(475, 56), (690, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((500, 65), "Список покупок", fill="#475569", font=f_h3)

# Week Control Bar
draw.text((25, 112), "Рацион питания: Неделя 42 (12 Октября — 18 Октября)", fill="#0F172A", font=f_h1)

draw.rectangle([(750, 105), (920, 138)], fill="#FFFFFF", outline="#CBD5E1")
draw.text((770, 114), "< Предыдущая нед.", fill="#334155", font=f_small_b)

draw.rectangle([(930, 105), (1180, 138)], fill="#10B981")
draw.text((950, 114), "Сформировать покупки >", fill="#FFFFFF", font=f_small_b)

# 7 Columns
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
col_w = 158
sx = 25

plans = [
    ("Овсяная каша", "Борщ украинский", "Паста Карбонара"),
    ("Омлет с сыром", "Борщ (остаток)", "Куриное филе"),
    ("Творог с медом", "Крем-суп грибной", "Семга запеченная"),
    ("Овсяная каша", "Крем-суп (остаток)", "Греческий салат"),
    ("Сырники с джемом", "Уха рыбная", "Паста с томатами"),
    ("Блины домашние", "Солянка сборная", "Стейк говяжий"),
    ("Яичница с беконом", "Солянка (остаток)", "Пицца домашняя")
]

for idx, day_name in enumerate(days):
    dx = sx + idx * (col_w + 8)
    
    # Column Header
    header_col = "#1E293B" if idx < 5 else "#2563EB"
    draw.rectangle([(dx, 150), (dx + col_w, 185)], fill=header_col)
    draw.text((dx + 25, 160), day_name, fill="#FFFFFF", font=f_h3)
    
    # Body Container
    draw.rectangle([(dx, 185), (dx + col_w, 705)], fill="#FFFFFF", outline="#CBD5E1")
    
    # 3 Slots: Breakfast, Lunch, Dinner
    slots = [("ЗАВТРАК", 200, plans[idx][0]), ("ОБЕД", 365, plans[idx][1]), ("УЖИН", 530, plans[idx][2])]
    for slot_name, sy, dish in slots:
        draw.rectangle([(dx + 8, sy), (dx + col_w - 8, sy + 150)], fill="#F8FAFC", outline="#E2E8F0")
        draw.text((dx + 16, sy + 10), slot_name, fill="#64748B", font=f_small_b)
        
        # Dish Card inside
        draw.rectangle([(dx + 14, sy + 32), (dx + col_w - 14, sy + 105)], fill="#EFF6FF", outline="#BFDBFE")
        # Split dish name if long
        draw.text((dx + 20, sy + 45), dish[:18], fill="#1E40AF", font=f_body_b)
        if len(dish) > 18:
            draw.text((dx + 20, sy + 65), dish[18:], fill="#1E40AF", font=f_small)
            
        # Change button
        draw.rectangle([(dx + 14, sy + 115), (dx + col_w - 14, sy + 140)], fill="#E2E8F0")
        draw.text((dx + 42, sy + 122), "Заменить", fill="#334155", font=f_small_b)

# Status bar
draw.rectangle([(0, 720), (W, 750)], fill="#E2E8F0")
draw.text((20, 727), "Статус: Все 21 приёма пищи запланированы (100%). Автосохранение в meal_plan.json активно.", fill="#10B981", font=f_small_b)

img.save(os.path.join(output_dir, "gui_mockup_planner.png"))
print("Generated clean gui_mockup_planner.png")


# ==============================================================================
# 3. UI Mockup: Shopping List (gui_mockup_shopping_list.png)
# ==============================================================================
img = Image.new("RGB", (W, H), "#F1F5F9")
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (W, 42)], fill="#1E293B")
draw.text((20, 11), "Recipe & Meal Planner System v1.0 [C++/Qt] — Автоматический список покупок", fill="#FFFFFF", font=f_h2)
draw.ellipse([(1160, 14), (1176, 30)], fill="#EF4444")
draw.ellipse([(1135, 14), (1151, 30)], fill="#F59E0B")
draw.ellipse([(1110, 14), (1126, 30)], fill="#10B981")

# Tabs Bar
draw.rectangle([(20, 52), (1180, 95)], fill="#FFFFFF", outline="#CBD5E1", width=1)
draw.rectangle([(25, 56), (220, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((45, 65), "Книга рецептов", fill="#475569", font=f_h3)

draw.rectangle([(230, 56), (465, 91)], fill="#F1F5F9", outline="#E2E8F0")
draw.text((250, 65), "План меню на неделю", fill="#475569", font=f_h3)

draw.rectangle([(475, 56), (690, 91)], fill="#2563EB")
draw.text((500, 65), "Список покупок", fill="#FFFFFF", font=f_h3)

# Title & Buttons
draw.text((25, 112), "Сводный расчет продуктов на неделю (12 — 18 Октября)", fill="#0F172A", font=f_h1)

draw.rectangle([(660, 105), (820, 138)], fill="#2563EB")
draw.text((675, 114), "Пересчитать", fill="#FFFFFF", font=f_small_b)

draw.rectangle([(830, 105), (990, 138)], fill="#10B981")
draw.text((845, 114), "Экспорт (TXT)", fill="#FFFFFF", font=f_small_b)

draw.rectangle([(1000, 105), (1180, 138)], fill="#64748B")
draw.text((1035, 114), "Печать списка", fill="#FFFFFF", font=f_small_b)

# Table Box
draw.rectangle([(20, 150), (1180, 705)], fill="#FFFFFF", outline="#CBD5E1")

# Table Header
draw.rectangle([(20, 150), (1180, 185)], fill="#F1F5F9")
draw.text((35, 160), "V", fill="#64748B", font=f_h3)
draw.text((80, 160), "Наименование продукта", fill="#475569", font=f_h3)
draw.text((390, 160), "Категория", fill="#475569", font=f_h3)
draw.text((580, 160), "Суммарный вес / кол-во", fill="#475569", font=f_h3)
draw.text((800, 160), "Основание (блюда из недельного плана)", fill="#475569", font=f_h3)

shop_items = [
    (False, "Картофель свежий", "Овощи и зелень", "1 850 г (1.85 кг)", "Борщ (400г), Солянка (350г), Стейк гарнир (600г), Уха (500г)"),
    (False, "Говядина бескостная (мякоть)", "Мясо и птица", "1 200 г (1.2 кг)", "Борщ украинский (600г), Стейк говяжий (600г)"),
    (False, "Филе куриное охлажденное", "Мясо и птица", "900 г (0.9 кг)", "Куриное филе с рисом (500г), Греческий салат с курицей (400г)"),
    (True,  "Лук репчатый", "Овощи и зелень", "550 г", "Борщ (120г), Солянка (150г), Паста (80г), Уха (200г)"),
    (False, "Морковь столовая", "Овощи и зелень", "450 г", "Борщ (150г), Уха (150г), Солянка (150г)"),
    (True,  "Спагетти / паста твердых сортов", "Бакалея", "500 г (1 пачка)", "Паста Карбонара (250г), Паста с томатами (250г)"),
    (False, "Сыр Пармезан / Грана Падано", "Молочные изделия", "200 г", "Паста Карбонара (120г), Салат (80г)"),
    (False, "Яйца куриные С0", "Бакалея / Яйцо", "10 шт. (1 десяток)", "Карбонара (3 шт), Омлет (3 шт), Яичница (4 шт)"),
    (False, "Капуста белокочанная", "Овощи и зелень", "700 г", "Борщ украинский (350г), Салат свежий (350г)"),
    (False, "Овсяные хлопья Геркулес", "Бакалея", "300 г", "Овсяная каша на завтрак (2 дня по 150г)"),
    (True,  "Чеснок свежий", "Овощи и зелень", "1 головка", "Борщ (4 зубч.), Паста (2 зубч.), Стейк (3 зубч.)"),
    (False, "Семга свежая (стейки)", "Рыба и морепродукты", "600 г", "Семга запеченная с травами на ужин")
]

row_y = 190
for chk, name, cat, qty, reason in shop_items:
    bg = "#F8FAFC" if chk else "#FFFFFF"
    draw.rectangle([(22, row_y), (1178, row_y + 36)], fill=bg, outline="#F1F5F9")
    
    # Checkbox
    cb_col = "#10B981" if chk else "#CBD5E1"
    draw.rectangle([(35, row_y + 8), (55, row_y + 28)], fill=cb_col if chk else "#FFFFFF", outline=cb_col, width=2)
    if chk:
        draw.text((39, row_y + 9), "V", fill="#FFFFFF", font=f_small_b)
        
    draw.text((80, row_y + 9), name, fill="#64748B" if chk else "#0F172A", font=f_body_b if not chk else f_body)
    draw.text((390, row_y + 9), cat, fill="#64748B", font=f_body)
    draw.text((580, row_y + 9), qty, fill="#2563EB" if not chk else "#64748B", font=f_body_b)
    draw.text((800, row_y + 9), reason, fill="#64748B" if chk else "#334155", font=f_small)
    row_y += 39

# Summary inside table
draw.rectangle([(25, 660), (1175, 695)], fill="#EFF6FF", outline="#BFDBFE")
draw.text((40, 670), "ИТОГО К ПОКУПКЕ: 12 позиций (Куплено: 3 позиции  •  Осталось приобрести: 9 позиций). Суммирование выполнено успешно.", fill="#1E40AF", font=f_body_b)

# Status bar
draw.rectangle([(0, 720), (W, 750)], fill="#E2E8F0")
draw.text((20, 727), "Статус: Сформирован экспортный файл 'shopping_list.txt'. Конфликтов единиц измерения не обнаружено.", fill="#10B981", font=f_small_b)

img.save(os.path.join(output_dir, "gui_mockup_shopping_list.png"))
print("Generated clean gui_mockup_shopping_list.png")


# ==============================================================================
# 4. Architecture Diagram: SysML v2 Requirements (sysml_requirements_diagram.png)
# ==============================================================================
img = Image.new("RGB", (1280, 820), "#F8FAFC")
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (1280, 50)], fill="#0F172A")
draw.text((25, 14), "«requirement» Diagram [SysML v2 / Requirements Breakdown & Traceability]", fill="#FFFFFF", font=f_h1)
draw.text((1050, 16), "Recipe & Meal Planner System", fill="#94A3B8", font=f_h3)

# Boundary
draw.rectangle([(220, 70), (1250, 790)], fill="#FFFFFF", outline="#3B82F6", width=2)
draw.text((240, 85), "system RecipeMealPlannerApp (C++ / Desktop Architecture)", fill="#1E40AF", font=f_h2)

# User Actor (stick figure)
draw.ellipse([(70, 240), (120, 290)], fill="#E2E8F0", outline="#0F172A", width=2)
draw.line([(95, 290), (95, 380)], fill="#0F172A", width=2)
draw.line([(95, 320), (50, 360)], fill="#0F172A", width=2)
draw.line([(95, 320), (140, 360)], fill="#0F172A", width=2)
draw.line([(95, 380), (60, 450)], fill="#0F172A", width=2)
draw.line([(95, 380), (130, 450)], fill="#0F172A", width=2)
draw.text((55, 465), "«actor»\nПользователь\n(Кулинар)", fill="#0F172A", font=f_small_b)

# Package 1: Recipe Management
draw.rectangle([(250, 130), (720, 330)], fill="#EFF6FF", outline="#3B82F6", width=2)
draw.text((265, 142), "«requirement» Модуль 1: База рецептов", fill="#1E40AF", font=f_h3)

p1_reqs = [
    ("REQ-FUNC-001 (UC-1.1)", "Добавление блюда, состава ингредиентов и пошаговой инструкции"),
    ("REQ-FUNC-002 (UC-1.2)", "Просмотр каталога, фильтрация по категориям и поиск по имени"),
    ("REQ-FUNC-003 (UC-1.3)", "Редактирование параметров и удаление устаревших рецептов")
]
py = 175
for code, desc in p1_reqs:
    draw.rectangle([(265, py), (705, py + 42)], fill="#FFFFFF", outline="#93C5FD")
    draw.text((275, py + 5), code, fill="#2563EB", font=f_small_b)
    draw.text((275, py + 22), desc, fill="#334155", font=f_small)
    py += 48

# Package 2: Meal Planner
draw.rectangle([(250, 360), (720, 560)], fill="#F0FDF4", outline="#10B981", width=2)
draw.text((265, 372), "«requirement» Модуль 2: Планирование рациона", fill="#065F46", font=f_h3)

p2_reqs = [
    ("REQ-FUNC-004 (UC-2.1)", "Назначение блюд на слоты Завтрак / Обед / Ужин на 7 дней"),
    ("REQ-FUNC-005 (UC-2.2)", "Навигация по календарным неделям и сохранение сетки"),
    ("REQ-FUNC-006 (UC-2.3)", "Копирование удачного рациона на следующую неделю")
]
py = 405
for code, desc in p2_reqs:
    draw.rectangle([(265, py), (705, py + 42)], fill="#FFFFFF", outline="#86EFAC")
    draw.text((275, py + 5), code, fill="#059669", font=f_small_b)
    draw.text((275, py + 22), desc, fill="#334155", font=f_small)
    py += 48

# Package 3: Shopping List
draw.rectangle([(760, 240), (1220, 470)], fill="#FEF3C7", outline="#F59E0B", width=2)
draw.text((775, 252), "«requirement» Модуль 3: Список покупок", fill="#92400E", font=f_h3)

p3_reqs = [
    ("REQ-FUNC-007 (UC-3.1)", "Автоматический сбор и суммирование одноименных продуктов"),
    ("REQ-FUNC-008 (UC-3.2)", "Группировка покупок по отделам магазина (мясо, овощи и др.)"),
    ("REQ-FUNC-009 (UC-3.3)", "Формирование ведомости и экспорт в файл (shopping_list.txt)"),
    ("REQ-FUNC-010 (UC-3.4)", "Интерактивная отметка купленных товаров (чекбокс V)")
]
py = 285
for code, desc in p3_reqs:
    draw.rectangle([(775, py), (1205, py + 40)], fill="#FFFFFF", outline="#FCD34D")
    draw.text((785, py + 4), code, fill="#D97706", font=f_small_b)
    draw.text((785, py + 21), desc, fill="#334155", font=f_small)
    py += 44

# Non-Functional Requirements Block
draw.rectangle([(250, 585), (1220, 770)], fill="#F8FAFC", outline="#64748B", width=2)
draw.text((265, 597), "«non-functional» Системные ограничения и нефункциональные требования (QoS / Constraints)", fill="#334155", font=f_h3)

nfrs = [
    ("REQ-REL-001 (Надежность)", "Персистентность: сохранение базы и расписания в структурированные файлы (JSON/CSV)."),
    ("REQ-PERF-001 (Производительность)", "Время генерации списка покупок из 50+ блюд составляет менее 0.3 секунды."),
    ("REQ-PORT-001 (Переносимость)", "Кроссплатформенная реализация на стандартном C++17/20 для ОС Windows и Linux."),
    ("REQ-SEC-001 (Безопасность)", "Локальная обработка: приложение полностью автономно и не передает данные во внешнюю сеть."),
    ("REQ-INT-001 (Интерфейс)", "Интуитивно понятный графический интерфейс пользователя с навигацией по вкладкам.")
]

ny = 625
for code, desc in nfrs:
    draw.text((275, ny), f"• {code}: ", fill="#0F172A", font=f_small_b)
    draw.text((540, ny), desc, fill="#475569", font=f_small)
    ny += 27

# Connection lines from User
draw.line([(140, 320), (250, 230)], fill="#2563EB", width=2)
draw.line([(140, 350), (250, 460)], fill="#10B981", width=2)

# Relationship between Planner and Shopping List («deriveReqt»)
draw.line([(720, 460), (760, 355)], fill="#D97706", width=2)
draw.text((715, 395), "«deriveReqt»", fill="#B45309", font=f_small_b)

img.save(os.path.join(output_dir, "sysml_requirements_diagram.png"))
print("Generated clean sysml_requirements_diagram.png")
