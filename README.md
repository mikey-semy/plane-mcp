# Plane MCP Server - Python Implementation

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-1.21.0-green.svg)](https://github.com/jlowin/fastmcp)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Original](https://img.shields.io/badge/Based%20on-Official%20Plane%20MCP-blue.svg)](https://github.com/makeplane/plane-mcp-server)

Plane's Model Context Protocol Server - Python реализация 🔌 ⌨️ 🔥

Предоставляет **47 инструментов** для работы с проектами, задачами, модулями и циклами в Plane.

> **Оригинальный проект**: [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) (TypeScript)
> **plane.so** | Topics: `model-context-protocol` `mcp-server` `python` `fastmcp`

## 📚 Документация

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Руководство для контрибьюторов
- **[CHANGELOG.md](CHANGELOG.md)** - История изменений

## ✨ Возможности

- ✅ **47 инструментов** - полное покрытие Plane API
- ✅ **SSE Transport** - HTTP сервер для удалённого доступа
- ✅ **stdio Transport** - для локальной интеграции с Claude Desktop
- ✅ **Полный CRUD** для Issues, Projects, Modules, Cycles
- ✅ **Metadata Management** - полное управление типами задач, метками, статусами
- ✅ **Module/Cycle Issues** - управление задачами в модулях и циклах
- ✅ **Worklogs** - отслеживание времени работы
- ✅ **Issue Comments** - работа с комментариями
- ✅ **Readable Identifiers** - поддержка PROJECT-123 формата
- ✅ **Асинхронная архитектура** - быстрая обработка запросов
- ✅ **Docker Ready** - готовые конфигурации для контейнеризации

## 📊 Краткий обзор инструментов

### User (2 tools)
- `get_current_user` - информация о текущем пользователе
- `get_workspace_members` - список участников workspace

### Metadata (15 tools)
**Issue Types (5):**
- `list_issue_types`, `get_issue_type`, `create_issue_type`, `update_issue_type`, `delete_issue_type`

**States (5):**
- `list_states`, `get_state`, `create_state`, `update_state`, `delete_state`

**Labels (5):**
- `list_labels`, `get_label`, `create_label`, `update_label`, `delete_label`
- `get_state` - детали статуса
- `create_state` - создание статуса
- `update_state` - обновление статуса
- `delete_state` - удаление статуса

**Labels:**
- `list_labels` - список меток
- `get_label` - детали метки
- `create_label` - создание метки
- `update_label` - обновление метки
- `delete_label` - удаление метки

### Projects (2 tools)
- `get_projects` - список всех проектов
- `create_project` - создание нового проекта

### Issues (8 tools)
- `list_project_issues` - список задач проекта
- `get_issue` - детали конкретной задачи
- `get_issue_using_readable_identifier` - получить задачу по читаемому ID (FIRST-123)
- `create_issue` - создание задачи
- `update_issue` - обновление задачи
- `delete_issue` - удаление задачи
- `get_issue_comments` - получить комментарии к задаче
- `add_issue_comment` - добавить комментарий к задаче

### Modules (5 tools)
- `list_modules` - список модулей проекта
- `get_module` - детали модуля
- `create_module` - создание модуля
- `update_module` - обновление модуля
- `delete_module` - удаление модуля

### Module Issues (3 tools)
- `list_module_issues` - список задач в модуле
- `add_module_issues` - добавить задачи в модуль
- `delete_module_issue` - удалить задачу из модуля

### Cycles (6 tools)
- `list_cycles` - список циклов проекта
- `get_cycle` - детали цикла
- `create_cycle` - создание цикла
- `update_cycle` - обновление цикла
- `delete_cycle` - удаление цикла
- `transfer_cycle_issues` - перенести задачи из одного цикла в другой

### Cycle Issues (3 tools)
- `list_cycle_issues` - список задач в цикле
- `add_cycle_issues` - добавить задачи в цикл
- `delete_cycle_issue` - удалить задачу из цикла

### Worklogs (5 tools)
- `get_issue_worklogs` - список рабочих логов задачи
- `get_total_worklogs` - общее время логов проекта
- `create_worklog` - создать рабочий лог
- `update_worklog` - обновить рабочий лог
- `delete_worklog` - удалить рабочий лог

**Всего: 47 инструментов**

## Быстрый старт с Docker

### 1. Создайте `.env` файл:

```bash
cp .env.example .env
```

Отредактируйте `.env` и добавьте свои данные:

```env
# Обязательные переменные
PLANE_API_KEY=plane_xxxxxxxxxxxxxxxxxxxx
PLANE_WORKSPACE_SLUG=your-workspace-slug

# Опциональные (значения по умолчанию)
PLANE_API_HOST_URL=https://api.plane.so/
MCP_HOST=0.0.0.0
MCP_PORT=8000
```

### 2. Запуск с Docker Compose:

```bash
docker-compose up -d
```

Сервер будет доступен на `http://localhost:8000/sse`

### 3. Проверка работы:

```bash
# Проверка здоровья контейнера
docker-compose ps

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down
```

## Локальная установка (для разработки)

### Требования
- Python 3.12+
- uv (для управления пакетами)

### Установка

```bash
# Установка uv (если ещё не установлен)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Клонирование и установка зависимостей
cd plane-mcp
uv sync

# Создание .env файла
cp .env.example .env
# Отредактируйте .env, добавьте свои ключи

# Запуск сервера
uv run plane-mcp
```

## Конфигурация

### Переменные окружения

| Переменная | Описание | По умолчанию | Обязательная |
|-----------|----------|--------------|--------------|
| `PLANE_API_KEY` | API ключ Plane | - | ✅ |
| `PLANE_WORKSPACE_SLUG` | Slug вашего workspace | - | ✅ |
| `PLANE_API_HOST_URL` | URL Plane API | `https://api.plane.so/` | ❌ |
| `MCP_HOST` | Хост для HTTP сервера | `0.0.0.0` | ❌ |
| `MCP_PORT` | Порт для HTTP сервера | `8000` | ❌ |

### Использование с MCP клиентами

FastMCP автоматически поддерживает:
- **SSE** (Server-Sent Events) - HTTP транспорт на `http://host:port/sse`
- **stdio** - стандартный ввод/вывод для локальных клиентов

Для подключения к серверу через SSE используйте endpoint:
```
http://localhost:8000/sse
```

## Разработка

### Структура проекта
```
plane-mcp/
├── src/
│   └── plane_mcp/
│       ├── __init__.py
│       ├── server.py          # Основной сервер
│       ├── schemas.py         # Pydantic модели
│       ├── common/
│       │   ├── request_helper.py  # HTTP клиент для Plane API
│       │   └── version.py
│       └── tools/
│           ├── issues.py
│           ├── projects.py
│           ├── cycles.py
│           ├── modules.py
│           ├── metadata.py
│           └── user.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

### Запуск тестов
```bash
uv run pytest
```

### Форматирование кода
```bash
uv run ruff check --fix
uv run ruff format
```

## Получение API ключа Plane

1. Войдите в Plane
2. Перейдите в Settings → API Tokens
3. Создайте новый токен
4. Скопируйте и сохраните в `.env`

## Лицензия

MIT

## Автор

Сгенерировано на основе официального Plane MCP Server
