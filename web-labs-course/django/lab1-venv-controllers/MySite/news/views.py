from django.http import HttpResponse


def index(request):
    """Контроллер главной страницы приложения news — /news/"""
    # Для отладки (как в методичке):
    # print(dir(request))
    # print(request.method, request.path)

    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Новости — index</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 720px; margin: 40px auto; padding: 20px; }
            h1 { color: #1a73e8; }
            a { color: #1a73e8; }
            .card { background: #f5f5f5; padding: 16px; border-radius: 8px; margin-top: 16px; }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на новостной сайт!</h1>
        <div class="card">
            <p>Это страница <strong>index</strong> приложения <code>news</code>.</p>
            <p>Маршрут: <code>/news/</code></p>
            <p>Метод: <code>""" + request.method + """</code></p>
            <p><a href="/news/test/">Перейти на test →</a></p>
        </div>
        <hr>
        <p><small>ЛР №1 — Django. Виртуальное окружение. Контроллеры и маршруты.</small></p>
    </body>
    </html>
    """
    return HttpResponse(html)


def test(request):
    """Контроллер тестовой страницы — /news/test/"""
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Новости — test</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 720px; margin: 40px auto; padding: 20px; }
            h1 { color: #0d904f; }
            a { color: #1a73e8; }
            .card { background: #e8f5e9; padding: 16px; border-radius: 8px; margin-top: 16px; }
        </style>
    </head>
    <body>
        <h1>Страница test</h1>
        <div class="card">
            <p>Это страница <strong>test</strong> приложения <code>news</code>.</p>
            <p>Маршрут: <code>/news/test/</code></p>
            <p>Метод: <code>""" + request.method + """</code></p>
            <p>Путь: <code>""" + request.path + """</code></p>
            <p><a href="/news/">← На главную</a></p>
        </div>
        <hr>
        <p><small>ЛР №1 — Django. Контроллеры и маршруты.</small></p>
    </body>
    </html>
    """
    return HttpResponse(html)
