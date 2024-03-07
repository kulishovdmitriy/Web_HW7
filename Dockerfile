# Указываем базовый образ
FROM postgres:latest

# Устанавливаем переменные окружения
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=123456789
ENV POSTGRES_DB=my_db

# Порт, который будет прослушивать PostgreSQL
EXPOSE 5432