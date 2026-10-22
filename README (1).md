# web-labs-course

Репозиторий лабораторных работ по веб-разработке.

**Студент:** [ФИО]  
**Группа:** [Группа]  
**Вариант:** 4  

---

## Навигация

### Backend (Node.js + Express)

| Работа | Папка | Тема |
|--------|-------|------|
| [ЛР №1](./backend/lab1-first-http-server/README.md) | `backend/lab1-first-http-server/` | Настройка среды разработки и первый HTTP-сервер |
| [ЛР №2](./backend/lab2-crud/README.md) | `backend/lab2-crud/` | HTTP-методы: обработка GET, POST, PUT, DELETE |
| [ЛР №3](./backend/lab3-routing/README.md) | `backend/lab3-routing/` | Маршрутизация, параметры пути и query-параметры |

### Django (Python)

| Работа | Папка | Тема |
|--------|-------|------|
| [ЛР №1](./django/lab1-venv-controllers/README.md) | `django/lab1-venv-controllers/` | Создание виртуального окружения. Контроллеры и маршруты |
| [ЛР №2](./django/lab2-models-crud/README.md) | `django/lab2-models-crud/` | Модели. CRUD. Миграции |

---

## Структура репозитория

```
web-labs-course/
├── README.md
├── .gitignore
├── backend/
│   ├── lab1-first-http-server/   # Express: GET, nodemon, 404, logging
│   ├── lab2-crud/                # Express: CRUD API (книги)
│   └── lab3-routing/             # Express: params, query, nested routes
└── django/
    ├── lab1-venv-controllers/    # Django: venv, views, urls
    └── lab2-models-crud/         # Django: models, migrations, ORM
```

---

## Быстрый старт

### Backend (Node.js)

```bash
cd backend/lab1-first-http-server   # или lab2-crud / lab3-routing
npm install
npm run dev
# http://localhost:3000
```

### Django

```bash
cd django/lab1-venv-controllers     # или lab2-models-crud
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd MySite
python manage.py migrate
python manage.py runserver
# http://127.0.0.1:8000/news/
```

---

## Вариант 4 (кратко)

| Предмет | Сущность / тема |
|---------|-----------------|
| Backend ЛР1 | Welcome!, `/api/books`, `/api/authors`, `/api/books/:id` |
| Backend ЛР2 | CRUD `/books` + search/sort/pagination/stats |
| Backend ЛР3 | `/books/:id/chapters`, `/authors/:author/books`, query-фильтры |
| Django ЛР1 | Проект MySite, приложение news, index/test |
| Django ЛР2 | Модели News + Task, миграции, ORM, admin |

В каждой папке — свой `README.md` (отчёт), код и `curl_commands.txt` / инструкции по запуску.

---

## Публикация на GitHub

```bash
git init
git add .
git commit -m "Лабораторные работы по web (Backend + Django), вариант 4"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Перед пушем подставьте **ФИО** и **группу** в корневом `README.md` и в README каждой лабы.
