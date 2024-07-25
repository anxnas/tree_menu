# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем зависимости для работы с PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Выполняем миграции базы данных
RUN python manage.py migrate

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер разработки
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]