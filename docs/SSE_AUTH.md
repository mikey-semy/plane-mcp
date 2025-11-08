# 🔒 Защищённый SSE Endpoint - Basic Auth

## 📋 Учётные данные по умолчанию

- **Username**: `admin`
- **Password**: `SecurePassword123`

⚠️ **ВАЖНО**: Измените пароль перед продакшен развёртыванием!

## 🔧 Как изменить пароль

### 1. Генерация нового хеша

```bash
docker run --rm httpd:2.4-alpine htpasswd -nbB admin "YourNewPassword"
```

Вывод будет примерно таким:
```
admin:$2y$05$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 2. Обновление .env или .env.production

```bash
# Username
BASIC_AUTH_USER=admin

# Пароль в открытом виде (для документации и подключения)
BASIC_AUTH_PASSWORD=YourNewPassword

# Bcrypt хеш (для Traefik)
# ⚠️ Важно: используйте $$ вместо $ в .env файле
BASIC_AUTH_PASSWORD_HASH=$$2y$$05$$xxxxx...
```

### 3. Перезапуск контейнера

```bash
docker-compose down
docker-compose up -d
```

Traefik автоматически подхватит новые значения из переменных окружения!

## 📱 Подключение с Basic Auth

### VSCode mcp.json

```json
{
  "servers": {
    "plane": {
      "url": "https://admin:SecurePassword123@mcp.plane.equiply.ru:9000/sse"
    }
  }
}
```

### Claude Desktop config

```json
{
  "mcpServers": {
    "plane": {
      "url": "https://admin:SecurePassword123@mcp.plane.equiply.ru:9000/sse"
    }
  }
}
```

**Формат**: `https://username:password@domain:port/sse`

## 🧪 Тестирование доступа

### С авторизацией (должно работать):
```bash
curl -u admin:SecurePassword123 https://mcp.plane.equiply.ru:9000/sse
```

### Без авторизации (должно вернуть 401):
```bash
curl https://mcp.plane.equiply.ru:9000/sse
```

Ответ:
```
401 Unauthorized
```

## 🔐 Дополнительная защита (опционально)

### 1. IP Whitelist

Добавьте в docker-compose.yml:

```yaml
labels:
  # Basic Auth
  - "traefik.http.middlewares.mcp-auth.basicauth.users=admin:$$2y$$05$$..."

  # IP Whitelist - разрешить только определённые IP
  - "traefik.http.middlewares.mcp-ipwhitelist.ipwhitelist.sourcerange=1.2.3.4/32,5.6.7.8/32"

  # Применить оба middleware
  - "traefik.http.routers.mcp.middlewares=mcp-auth,mcp-ipwhitelist"
```

Замените `1.2.3.4` и `5.6.7.8` на ваши IP адреса.

### 2. Rate Limiting

Ограничить количество запросов:

```yaml
labels:
  - "traefik.http.middlewares.mcp-ratelimit.ratelimit.average=100"
  - "traefik.http.middlewares.mcp-ratelimit.ratelimit.burst=50"
  - "traefik.http.routers.mcp.middlewares=mcp-auth,mcp-ratelimit"
```

## 🚨 Безопасность

### Лучшие практики:

1. ✅ **Используйте HTTPS** - всегда, не HTTP
2. ✅ **Сложный пароль** - минимум 16 символов
3. ✅ **Уникальные учётные данные** - не переиспользуйте
4. ✅ **Регулярная ротация** - меняйте пароль раз в 3-6 месяцев
5. ✅ **Мониторинг** - следите за логами доступа
6. ✅ **IP Whitelist** - если возможно, ограничьте доступ по IP

### Что НЕ делать:

- ❌ Не коммитьте пароли в git
- ❌ Не используйте простые пароли (password123)
- ❌ Не оставляйте дефолтные учётные данные
- ❌ Не публикуйте URL с паролем в README

## 📊 Проверка логов

### Dokploy/Docker logs:

```bash
docker logs plane-mcp-server
```

Успешные запросы:
```
INFO: 195.46.162.203:51229 - "GET /sse HTTP/1.1" 200 OK
```

Неудачные (без авторизации):
```
INFO: 205.210.31.221:64272 - "GET / HTTP/1.1" 401 Unauthorized
```

## 🔄 Миграция существующих клиентов

Если у вас уже есть клиенты подключённые к незащищённому endpoint:

1. Уведомите всех пользователей о изменениях
2. Предоставьте новые учётные данные
3. Примеры конфигурации с Basic Auth
4. Дедлайн миграции
5. После дедлайна - включите Basic Auth

## 💡 Альтернативы Basic Auth

Если нужна более сложная авторизация:

1. **OAuth2** - через Traefik ForwardAuth
2. **JWT Token** - кастомная middleware
3. **Mutual TLS** - клиентские сертификаты
4. **VPN** - Tailscale/WireGuard (самое безопасное)

Для большинства случаев **Basic Auth + HTTPS** достаточно.

## 📚 Дополнительная информация

- [Traefik Basic Auth](https://doc.traefik.io/traefik/middlewares/http/basicauth/)
- [Traefik IP Whitelist](https://doc.traefik.io/traefik/middlewares/http/ipwhitelist/)
- [htpasswd Generator](https://hostingcanada.org/htpasswd-generator/)
