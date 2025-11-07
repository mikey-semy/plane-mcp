# 🎉 plane-mcp v0.1.0

## NPM Package Released!

**Package**: [@mikey-semy/plane-mcp](https://www.npmjs.com/package/@mikey-semy/plane-mcp)

Теперь вы можете использовать Plane MCP Server через NPM, точно так же как оригинальный `@makeplane/plane-mcp-server`, но с Python реализацией!

## 🚀 Быстрый старт

```bash
npx -y @mikey-semy/plane-mcp
```

**Требования:**
- Node.js 18+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- Plane API key и workspace slug

## 📦 Что нового

### NPM обёртка
- ✅ Автоматическая установка Python зависимостей через uv
- ✅ Простой запуск через npx без глобальной установки
- ✅ Работа с переменными окружения
- ✅ Поддержка множественных workspace через разные конфигурации

### Python реализация (47 инструментов)
- ✅ Полное покрытие Plane API
- ✅ Асинхронная архитектура на FastMCP
- ✅ SSE и stdio транспорты
- ✅ OOP структура схем с наследованием
- ✅ Docker ready для продакшена

## 💡 Использование

### Локально (stdio)

```json
{
  "servers": {
    "plane": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "plane_xxxxxxxxxxxxxxxxxxxx",
        "PLANE_WORKSPACE_SLUG": "your-workspace",
        "PLANE_API_HOST_URL": "https://api.plane.so/"
      }
    }
  }
}
```

### Удалённо (SSE)

Docker развёртывание с доступом по HTTP:

```bash
docker-compose up -d
```

Сервер доступен на `http://your-domain:port/sse`

## 📝 Документация

- [USAGE.md](USAGE.md) - Подробная инструкция
- [NPM_PUBLISH.md](NPM_PUBLISH.md) - Публикация форка
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guide
- [CHANGELOG.md](CHANGELOG.md) - История изменений

## 🔗 Ссылки

- **NPM**: https://www.npmjs.com/package/@mikey-semy/plane-mcp
- **GitHub**: https://github.com/mikey-semy/plane-mcp
- **Plane**: https://plane.so
- **FastMCP**: https://github.com/jlowin/fastmcp

## 🙏 Credits

Based on official [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) (TypeScript)

Python implementation with NPM wrapper for maximum compatibility and ease of use.
