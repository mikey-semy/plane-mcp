# Plane MCP Server - Python Implementation

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-1.21.0-green.svg)](https://github.com/jlowin/fastmcp)
[![NPM](https://img.shields.io/npm/v/@mikey-semy/plane-mcp)](https://www.npmjs.com/package/@mikey-semy/plane-mcp)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Original](https://img.shields.io/badge/Based%20on-Official%20Plane%20MCP-blue.svg)](https://github.com/makeplane/plane-mcp-server)

Plane's Model Context Protocol Server - Python реализация 🔌 ⌨️ 🔥

Предоставляет **47 инструментов** для работы с проектами, задачами, модулями и циклами в Plane.

> **Оригинальный проект**: [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) (TypeScript)
> **plane.so** | Topics: `model-context-protocol` `mcp-server` `python` `fastmcp`

## 📚 Документация

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Архитектура и сравнение stdio vs SSE
- **[USAGE.md](docs/USAGE.md)** - Подробная инструкция по использованию NPM пакета
- **[COPILOT_USAGE.md](docs/COPILOT_USAGE.md)** - Как использовать с GitHub Copilot в VSCode
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Руководство для контрибьюторов
- **[CHANGELOG.md](CHANGELOG.md)** - История изменений
- **[NPM_PUBLISH.md](docs/NPM_PUBLISH.md)** - Публикация форка в NPM

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

## 🚀 Быстрый старт

### Вариант 1: NPM (рекомендуется для локального использования)

**Требования:** Node.js 18+, [uv](https://docs.astral.sh/uv/getting-started/installation/)

✅ **Пакет опубликован в NPM**: [@mikey-semy/plane-mcp](https://www.npmjs.com/package/@mikey-semy/plane-mcp)

```bash
# Использование без установки (npx)
npx -y @mikey-semy/plane-mcp

# Или глобальная установка
npm install -g @mikey-semy/plane-mcp
plane-mcp
```

**Переменные окружения:**
```bash
# Windows PowerShell
$env:PLANE_API_KEY="plane_xxxxxxxxxxxxxxxxxxxx"
$env:PLANE_WORKSPACE_SLUG="your-workspace-slug"
$env:PLANE_API_HOST_URL="https://api.plane.so/"  # опционально

# Linux/macOS
export PLANE_API_KEY="plane_xxxxxxxxxxxxxxxxxxxx"
export PLANE_WORKSPACE_SLUG="your-workspace-slug"
export PLANE_API_HOST_URL="https://api.plane.so/"  # опционально
```

### Вариант 2: Docker (для продакшена)

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

# Порт на хосте (если 8000 занят, измените на другой)
HOST_PORT=8000
```

**Примечание:** Если порт 8000 уже занят, измените `HOST_PORT` на другой (например, 8001, 9000).

### 2. Запуск с Docker Compose:

```bash
docker-compose up -d
```

Сервер будет доступен на `http://localhost:HOST_PORT/sse` (по умолчанию `http://localhost:8000/sse`)

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
| `MCP_PORT` | Порт контейнера (внутренний) | `8000` | ❌ |
| `HOST_PORT` | Порт хоста (внешний) для Docker | `8000` | ❌ |

**Для продакшена:** используйте `.env.production` с вашими настройками.

## 🌐 Развёртывание

### Публичный NPM пакет

✅ Пакет опубликован и доступен: [@mikey-semy/plane-mcp](https://www.npmjs.com/package/@mikey-semy/plane-mcp)

Любой пользователь может использовать:
```bash
npx -y @mikey-semy/plane-mcp
```

### Docker развёртывание

Используйте Docker Compose для продакшен развёртывания. Сервер будет доступен по HTTP на указанном порту.

**Пример URL после развёртывания:**
```
https://your-domain.com:9000/sse
```

Настройте свой домен в `.env.production` и используйте reverse proxy (Traefik/Nginx) для SSL.

#### ⚠️ Безопасность SSE развёртывания

**ВАЖНО:** SSE endpoint предоставляет полный доступ к вашему Plane API!

**Рекомендуемые меры защиты:**
1. 🔒 **Не публикуйте URL публично** - SSE endpoint содержит ваш API ключ
2. 🛡️ **Используйте VPN** - ограничьте доступ только для вашей сети
3. 🔐 **Basic Auth** - добавьте authentication на уровне Traefik/Nginx
4. 🌐 **IP Whitelist** - разрешите доступ только с определённых IP
5. 📝 **Логирование** - отслеживайте все подключения
6. 🔄 **Регулярно ротируйте** API ключи

**Пример Traefik с Basic Auth:**
```yaml
labels:
  - "traefik.http.middlewares.auth.basicauth.users=user:$$apr1$$..."
  - "traefik.http.routers.mcp.middlewares=auth"
```

**Для личного использования рекомендуем stdio**, а не публичный SSE сервер.

### Использование с MCP клиентами

FastMCP автоматически поддерживает:
- **SSE** (Server-Sent Events) - HTTP транспорт на `http://host:port/sse`
- **stdio** - стандартный ввод/вывод для локальных клиентов

#### 🤔 Какой вариант выбрать?

**stdio (локальный)** - рекомендуется:
- ✅ Можно работать с несколькими workspace одновременно
- ✅ Разные API ключи для разных workspace
- ✅ Полный контроль над конфигурацией
- ⚠️ Требует установку uv локально

**SSE (удалённый)** - для централизованного использования:
- ✅ Не требует Python/uv на клиентской машине
- ✅ Быстрое подключение (сервер уже работает)
- ✅ Единая конфигурация для команды
- ⚠️ Фиксированный workspace на сервере
- ⚠️ Требует сетевое подключение к серверу
- 🔒 **Не публикуйте публичные URL** - используйте VPN или authentication!

📖 **Подробнее**: [COPILOT_USAGE.md](docs/COPILOT_USAGE.md)

#### Подключение через VSCode

Добавьте конфигурацию в `.vscode/mcp.json` или `mcp.json` в корне проекта:

**Вариант 1: NPM пакет (stdio) - для работы с разными workspace**

Позволяет переключаться между workspace просто меняя `env`:

```json
{
  "servers": {
    "plane-profitool": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "YOUR_PLANE_API_KEY",
        "PLANE_API_HOST_URL": "https://plane.equiply.ru/",
        "PLANE_WORKSPACE_SLUG": "profitool-store"
      }
    },
    "plane-another-project": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "YOUR_PLANE_API_KEY",
        "PLANE_API_HOST_URL": "https://plane.equiply.ru/",
        "PLANE_WORKSPACE_SLUG": "another-workspace"
      }
    }
  }
}
```

**Вариант 2: Удалённое подключение (SSE)**

Подключение к вашему развёрнутому серверу. **Внимание:** workspace фиксирован на сервере!

```json
{
  "servers": {
    "plane": {
      "url": "https://your-mcp-server.example.com:9000/sse"
    }
  }
}
```

**Примечание:** Замените `your-mcp-server.example.com` на адрес вашего сервера.

**Для работы с несколькими workspace через SSE:** разверните отдельный сервер для каждого workspace.


#### Подключение через Claude Desktop

Добавьте конфигурацию в `claude_desktop_config.json`:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Вариант 1: NPM пакет (рекомендуется)**

```json
{
  "mcpServers": {
    "plane": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "plane_xxxxxxxxxxxxxxxxxxxx",
        "PLANE_WORKSPACE_SLUG": "your-workspace-slug",
        "PLANE_API_HOST_URL": "https://api.plane.so/"
      }
    }
  }
}
```

**Вариант 2: Локальная установка (uv)**

```json
{
  "mcpServers": {
    "plane": {
      "command": "uv",
      "args": ["run", "plane-mcp"],
      "env": {
        "PLANE_API_KEY": "plane_xxxxxxxxxxxxxxxxxxxx",
        "PLANE_WORKSPACE_SLUG": "your-workspace-slug",
        "PLANE_API_HOST_URL": "https://api.plane.so/"
      }
    }
  }
}
```

После сохранения конфигурации перезапустите VSCode или Claude Desktop.

## Разработка

### Структура проекта
```
plane-mcp/
├── src/
│   └── plane_mcp/
│       ├── __init__.py
│       ├── server.py          # Основной сервер
│       ├── schemas/           # Pydantic модели (новая структура)
│       │   ├── __init__.py
│       │   ├── base.py        # Базовые классы и миксины
│       │   ├── project.py     # Project
│       │   ├── issue.py       # Issue, IssueType
│       │   ├── module.py      # Module, ModuleIssue
│       │   ├── cycle.py       # Cycle, CycleIssue
│       │   ├── metadata.py    # State, Label
│       │   └── worklog.py     # IssueWorkLog
│       ├── common/
│       │   ├── request_helper.py  # HTTP клиент для Plane API
│       │   └── version.py
│       └── tools/
│           ├── cycle_issues.py
│           ├── cycles.py
│           ├── issue_comments.py
│           ├── issues.py
│           ├── metadata.py
│           ├── module_issues.py
│           ├── modules.py
│           ├── projects.py
│           ├── user.py
│           └── worklogs.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

### Архитектура схем

Все Pydantic модели организованы с использованием наследования для DRY-кода:

**Базовые классы (base.py):**
- `PlaneBaseModel` - корневой класс с общими настройками
- `TimestampedModel` - добавляет created_at, updated_at
- `AuditedModel` - добавляет created_by, updated_by
- `WorkspaceOwnedModel` - добавляет workspace
- `ProjectOwnedModel` - добавляет project
- `SoftDeletableModel` - добавляет deleted_at
- `ArchivableModel` - добавляет archived_at
- `ExternallyIdentifiableModel` - добавляет external_id, external_source
- `SortableModel` - добавляет sort_order
- `FullAuditModel` - объединяет все вышеперечисленные + id

**Доменные модели:**
- **project.py** - `Project` (наследуется от FullAuditModel)
- **issue.py** - `Issue`, `IssueType`
- **module.py** - `Module`, `ModuleIssue`
- **cycle.py** - `Cycle`, `CycleIssue`
- **metadata.py** - `State`, `Label`
- **worklog.py** - `IssueWorkLog`

Каждая схема полностью документирована с описанием всех полей, типов и ограничений.

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
4. Скопируйте и сохраните в `.env` или используйте как переменную окружения

## 📦 Публикация в NPM

Если вы хотите опубликовать свой форк пакета, следуйте инструкциям в [NPM_PUBLISH.md](NPM_PUBLISH.md).

## Лицензия

MIT

## Автор

Сгенерировано на основе официального Plane MCP Server
