# BetProject

## Описание
BetProject — это микросервисное приложение для управление ставками.

## Стек технологий
- **Backend**: Python, FastAPI
- **База данных**: PostgreSQL
- **Брокер сообщений**: Kafka
- **Контейнеризация**: Docker, Docker Compose
- **Кэширование**: Redis (НЕ ВНЕДРЕННО, НА БУДУЩЕЕ)
  
## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/T11t114/betProject.git
cd betProject
```

### 2. Запуск через Docker
```bash
docker-compose up --build
```

## Описание файлов

data_access/ – Логика взаимодействия с базой данных.

api.py – Определение маршрутов API.

config.py – Конфигурационные параметры приложения.

consumer.py – Обработка событий из Kafka.

producer.py – Отправка событий в Kafka.

crud.py – Реализация операций CRUD.

dependencies.py – Определение зависимостей для маршрутов.

models.py – Определение моделей SQLAlchemy.

run.py – Точка входа в приложение.

schemas.py – Определение Pydantic-схем для валидации данных.

## API
Документация API доступна по адресу:
```
127.0.0.1:8080/docs
127.0.0.1:8081/docs
```

## Тестирование
```bash
pytest
```

