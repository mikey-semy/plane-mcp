# Обновление Plane с v0.27.1 до v1.1.0

## Проблема
Текущая версия v0.27.1 **не поддерживает External API** (`/api/v1/`).
Последняя версия v1.1.0 включает External API с X-API-Key аутентификацией.

## Решение

### 1. Обновить docker-compose.yml

Измени `APP_RELEASE` в docker-compose.yml или .env:

```yaml
# Было
APP_RELEASE=v0.27.1

# Стало
APP_RELEASE=v1.1.0
```

### 2. Команды для обновления в Dokploy

```bash
# 1. Остановить контейнеры
docker-compose down

# 2. Обновить образы
docker-compose pull

# 3. Запустить миграции
docker-compose up migrator

# 4. Запустить все сервисы
docker-compose up -d
```

### 3. Проверка после обновления

```bash
# Проверить версию
curl https://plane.equiply.ru/api/v1/users/me/ \
  -H "X-API-Key: plane_api_e63e2f6e51ef4192bc817216b2ed8a58"

# Должно вернуть данные пользователя, а не 404
```

## Альтернатива (без обновления)

Если обновление невозможно, нужно переделать MCP на Web App API (`/api/`) с session authentication.
**НО** это сложнее и менее безопасно для API интеграций.

## Рекомендация

✅ **ОБНОВИТЬ до v1.1.0** - это проще и даст доступ к External API.
