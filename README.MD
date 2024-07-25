# Tree Menu

Проект Tree Menu представляет собой веб-приложение с древовидным выпадающим меню.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/anxnas/tree_menu.git
    cd tree_menu
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

6. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.

## Использование Docker

1. Убедитесь, что у вас установлен Docker.

2. Соберите Docker-образ:

    ```bash
    docker build -t tree_menu .
    ```

3. Запустите контейнер:

    ```bash
    docker run -p 8000:8000 tree_menu
    ```

4. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.