# Использование @mikey-semy/plane-mcp

## 🚀 Быстрый старт

### 1. Установка uv (если ещё не установлен)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Получение Plane API ключа

1. Войдите в Plane (например, https://plane.equiply.ru или https://api.plane.so)
2. Перейдите в **Settings → API Tokens**
3. Нажмите **Generate New Token**
4. Скопируйте токен (формат: `plane_xxxxxxxxxxxxxxxxxxxx`)

### 3. Настройка переменных окружения

**Windows PowerShell:**
```powershell
$env:PLANE_API_KEY="plane_xxxxxxxxxxxxxxxxxxxx"
$env:PLANE_WORKSPACE_SLUG="your-workspace-slug"
$env:PLANE_API_HOST_URL="https://api.plane.so/"  # или ваш URL
```

**Linux/macOS:**
```bash
export PLANE_API_KEY="plane_xxxxxxxxxxxxxxxxxxxx"
export PLANE_WORKSPACE_SLUG="your-workspace-slug"
export PLANE_API_HOST_URL="https://api.plane.so/"  # или ваш URL
```

### 4. Запуск

```bash
# Без установки (рекомендуется)
npx -y @mikey-semy/plane-mcp

# Или глобальная установка
npm install -g @mikey-semy/plane-mcp
plane-mcp
```

## 📝 Использование с VSCode

Создайте файл `mcp.json` в корне проекта или `.vscode/mcp.json`:

```json
{
  "servers": {
    "plane-workspace-1": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "plane_xxxxxxxxxxxxxxxxxxxx",
        "PLANE_WORKSPACE_SLUG": "workspace-1",
        "PLANE_API_HOST_URL": "https://api.plane.so/"
      }
    },
    "plane-workspace-2": {
      "command": "npx",
      "args": ["-y", "@mikey-semy/plane-mcp"],
      "env": {
        "PLANE_API_KEY": "plane_xxxxxxxxxxxxxxxxxxxx",
        "PLANE_WORKSPACE_SLUG": "workspace-2",
        "PLANE_API_HOST_URL": "https://api.plane.so/"
      }
    }
  }
}
```

**Преимущества такого подхода:**
- ✅ Легко переключаться между workspace
- ✅ Каждый workspace может иметь свой API ключ
- ✅ Разные URL для разных инстансов Plane
- ✅ Не нужно ничего устанавливать - npx скачает автоматически

## 📝 Использование с Claude Desktop

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
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

После сохранения конфигурации перезапустите Claude Desktop.

## 🔧 Доступные инструменты

Сервер предоставляет **48 инструментов** для работы с Plane API:

### User (2)
- `get_current_user` - информация о текущем пользователе
- `get_workspace_members` - список участников workspace

### Projects (2)
- `get_projects` - список всех проектов
- `create_project` - создание нового проекта

### Issues (8)
- `list_project_issues`, `get_issue`, `get_issue_using_readable_identifier`
- `create_issue`, `update_issue`, `delete_issue`
- `get_issue_comments`, `add_issue_comment`

### Metadata (15)
- Issue Types: `list_issue_types`, `get_issue_type`, `create_issue_type`, `update_issue_type`, `delete_issue_type`
- States: `list_states`, `get_state`, `create_state`, `update_state`, `delete_state`
- Labels: `list_labels`, `get_label`, `create_label`, `update_label`, `delete_label`

### Modules (5)
- `list_modules`, `get_module`, `create_module`, `update_module`, `delete_module`

### Module Issues (3)
- `list_module_issues`, `add_module_issues`, `delete_module_issue`

### Cycles (6)
- `list_cycles`, `get_cycle`, `create_cycle`, `update_cycle`, `delete_cycle`
- `transfer_cycle_issues`

### Cycle Issues (3)
- `list_cycle_issues`, `add_cycle_issues`, `delete_cycle_issue`

### Worklogs (5)
- `get_issue_worklogs`, `get_total_worklogs`
- `create_worklog`, `update_worklog`, `delete_worklog`

## 🐛 Troubleshooting

### uv не найден

```bash
# Проверьте установку
uv --version

# Переустановите если нужно
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Ошибка "Missing required environment variables"

Убедитесь что установлены переменные окружения:
```bash
# Windows
$env:PLANE_API_KEY
$env:PLANE_WORKSPACE_SLUG

# Linux/macOS
echo $PLANE_API_KEY
echo $PLANE_WORKSPACE_SLUG
```

### Ошибка подключения к API

Проверьте:
1. Правильность API ключа
2. Правильность workspace slug
3. Правильность PLANE_API_HOST_URL (с завершающим `/`)
4. Доступность API (например, `curl https://api.plane.so/api/v1/users/me/`)

## 📚 Дополнительная документация

- **GitHub**: https://github.com/mikey-semy/plane-mcp
- **NPM**: https://www.npmjs.com/package/@mikey-semy/plane-mcp
- **Plane API**: https://docs.plane.so/
- **FastMCP**: https://github.com/jlowin/fastmcp

## 🤝 Поддержка

Если возникли проблемы:
1. Проверьте [Issues](https://github.com/mikey-semy/plane-mcp/issues)
2. Создайте новый issue с описанием проблемы
3. Укажите версию Node.js, Python, uv, и текст ошибки
