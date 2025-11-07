# Contributing to Plane MCP Server

Спасибо за интерес к улучшению Plane MCP Server! 🎉

## 📋 Оглавление

- [Code of Conduct](#code-of-conduct)
- [Как я могу помочь?](#как-я-могу-помочь)
- [Процесс разработки](#процесс-разработки)
- [Структура проекта](#структура-проекта)
- [Добавление нового инструмента](#добавление-нового-инструмента)
- [Стиль кода](#стиль-кода)
- [Тестирование](#тестирование)
- [Документация](#документация)

## Code of Conduct

Мы придерживаемся дружелюбного и профессионального общения. Будьте уважительны к другим участникам проекта.

## Как я могу помочь?

### 🐛 Нашли баг?

1. Проверьте, не был ли этот баг уже [зарегистрирован](../../issues)
2. Если нет, создайте новый issue с:
   - Описанием проблемы
   - Шагами для воспроизведения
   - Ожидаемым и фактическим поведением
   - Версией Python и зависимостей

### 💡 Есть идея для улучшения?

1. Откройте issue с описанием предложения
2. Объясните, какую проблему это решит
3. Опишите предлагаемое решение
4. Дождитесь обратной связи перед началом работы

### 📝 Хотите улучшить документацию?

Отлично! Документация всегда может быть лучше:
- Исправления опечаток
- Дополнительные примеры
- Улучшение объяснений
- Перевод на другие языки

### 🔧 Хотите добавить код?

1. Найдите подходящий issue или создайте новый
2. Сообщите, что хотите над ним работать
3. Следуйте [процессу разработки](#процесс-разработки)

## Процесс разработки

### 1. Fork и клонирование

```bash
# Fork репозитория через GitHub UI
# Затем клонируйте ваш fork
git clone https://github.com/YOUR-USERNAME/plane-mcp.git
cd plane-mcp
```

### 2. Настройка окружения

```bash
# Установите uv (если ещё не установлен)
# https://github.com/astral-sh/uv

# Установите зависимости
uv sync

# Создайте .env файл
cp .env.example .env
# Добавьте ваши Plane API credentials
```

### 3. Создайте ветку

```bash
git checkout -b feature/my-new-feature
# или
git checkout -b fix/bug-description
```

Используйте понятные имена веток:
- `feature/add-search-tool` - новая функциональность
- `fix/authentication-error` - исправление бага
- `docs/improve-readme` - улучшение документации
- `refactor/request-helper` - рефакторинг кода

### 4. Внесите изменения

Следуйте [стилю кода](#стиль-кода) проекта.

### 5. Тестирование

```bash
# Запустите сервер для проверки
uv run python -m plane_mcp.server

# Проверьте, что все инструменты загружаются
uv run python -c "from plane_mcp.server import mcp; print(f'Server: {mcp.name}')"

# TODO: Добавить unit tests когда они будут реализованы
# pytest tests/
```

### 6. Commit изменений

```bash
git add .
git commit -m "feat: add search tool for issues"
```

Используйте [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` - новая функция
- `fix:` - исправление бага
- `docs:` - изменения в документации
- `refactor:` - рефакторинг без изменения функциональности
- `test:` - добавление тестов
- `chore:` - изменения в build процессе, зависимостях

### 7. Push и создание Pull Request

```bash
git push origin feature/my-new-feature
```

Затем создайте Pull Request через GitHub UI.

## Структура проекта

```
plane-mcp/
├── src/plane_mcp/
│   ├── __init__.py              # Версия пакета
│   ├── server.py                # FastMCP сервер
│   ├── schemas.py               # Pydantic модели
│   ├── common/
│   │   ├── request_helper.py    # HTTP клиент
│   │   └── version.py           # Версия
│   └── tools/
│       ├── user.py              # User tools (2)
│       ├── metadata.py          # Metadata tools (15)
│       ├── projects.py          # Project tools (2)
│       ├── issues.py            # Issue tools (8)
│       ├── modules.py           # Module tools (5)
│       ├── module_issues.py     # Module-issue tools (3)
│       ├── cycles.py            # Cycle tools (6)
│       ├── cycle_issues.py      # Cycle-issue tools (3)
│       └── worklogs.py          # Worklog tools (5)
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── docs/                        # Документация
```

## Добавление нового инструмента

### Шаг 1: Определите схему (если нужна)

В `src/plane_mcp/schemas.py`:

```python
class MyEntity(BaseModel):
    """My entity model."""
    id: UUID
    name: str
    description: Optional[str] = None
    created_at: datetime
```

### Шаг 2: Создайте инструмент

В соответствующем файле в `src/plane_mcp/tools/`:

```python
from fastmcp import FastMCP
from plane_mcp.common.request_helper import make_plane_request
import os
import json

def register_my_tools(mcp: FastMCP):
    """Register my tools with the MCP server."""

    @mcp.tool()
    async def my_new_tool(entity_id: str, param: str) -> str:
        """
        Short description of what this tool does.

        Args:
            entity_id: The UUID identifier of the entity
            param: Description of this parameter
        """
        workspace_slug = os.getenv("PLANE_WORKSPACE_SLUG")

        # Для GET запроса
        response = await make_plane_request(
            "GET",
            f"workspaces/{workspace_slug}/my-entities/{entity_id}/"
        )

        # Для POST с телом
        response = await make_plane_request(
            "POST",
            f"workspaces/{workspace_slug}/my-entities/",
            body={"param": param}
        )

        return json.dumps(response, indent=2)
```

### Шаг 3: Зарегистрируйте в сервере

В `src/plane_mcp/server.py`:

```python
from plane_mcp.tools.my_module import register_my_tools

# В функции main():
register_my_tools(mcp)
```

### Шаг 4: Обновите документацию

- Добавьте описание в `TOOLS.md`
- Добавьте примеры в `EXAMPLES.md`
- Обновите счётчик в `README.md`
- Добавьте запись в `CHANGELOG.md`

## Стиль кода

### Python Style Guide

Мы следуем [PEP 8](https://pep8.org/) с некоторыми дополнениями:

#### Type Hints

Всегда используйте type hints:

```python
# ✅ Хорошо
async def create_issue(project_id: str, name: str, priority: str | None = None) -> str:
    pass

# ❌ Плохо
async def create_issue(project_id, name, priority=None):
    pass
```

#### Docstrings

Используйте Google style docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """
    Short description of the function.

    Longer description if needed. Explain what the function does,
    not how it does it.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        PlaneAPIError: When API request fails
    """
    pass
```

#### Naming Conventions

- Functions/methods: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Private variables: `_leading_underscore`

```python
# ✅ Хорошо
class UserManager:
    MAX_RETRIES = 3

    def get_user_by_id(self, user_id: str) -> User:
        pass

    def _internal_helper(self):
        pass

# ❌ Плохо
class user_manager:
    maxRetries = 3

    def GetUserByID(self, UserID):
        pass
```

#### Imports

Группируйте imports в следующем порядке:
1. Standard library
2. Third-party packages
3. Local imports

```python
# Standard library
import os
import json
from datetime import datetime

# Third-party
from fastmcp import FastMCP
import httpx
from pydantic import BaseModel

# Local
from plane_mcp.common.request_helper import make_plane_request
from plane_mcp.schemas import Issue
```

#### Async/Await

Все I/O операции должны быть асинхронными:

```python
# ✅ Хорошо
async def fetch_data() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# ❌ Плохо
def fetch_data() -> dict:
    response = requests.get(url)
    return response.json()
```

### Code Formatting

Рекомендуется использовать:
- `black` для форматирования
- `isort` для сортировки imports
- `mypy` для проверки типов

```bash
# TODO: Добавить в pyproject.toml когда будет готово
# uv run black src/
# uv run isort src/
# uv run mypy src/
```

## Тестирование

### Unit Tests (планируется)

```python
# tests/test_issues.py
import pytest
from plane_mcp.tools.issues import register_issue_tools

@pytest.mark.asyncio
async def test_create_issue():
    # Test implementation
    pass
```

### Integration Tests (планируется)

```python
# tests/integration/test_api.py
import pytest
from plane_mcp.server import mcp

@pytest.mark.asyncio
async def test_full_workflow():
    # Test creating issue, adding to cycle, etc.
    pass
```

### Manual Testing

Всегда тестируйте вручную перед PR:

1. Запустите сервер: `uv run python -m plane_mcp.server`
2. Проверьте, что новый инструмент загружается
3. Протестируйте с реальным Plane API (используйте тестовый workspace)
4. Проверьте edge cases (пустые параметры, неверные ID и т.д.)

## Документация

### Что документировать

- **Код**: Docstrings для всех публичных функций и классов
- **API**: Описание всех tools в TOOLS.md
- **Примеры**: Практические примеры в EXAMPLES.md
- **Изменения**: Записи в CHANGELOG.md

### Стиль документации

- Используйте простой, понятный язык
- Добавляйте примеры кода
- Объясняйте "почему", а не только "как"
- Используйте списки и таблицы для структурирования информации

## Pull Request Guidelines

### Checklist перед созданием PR

- [ ] Код следует стилю проекта
- [ ] Все новые функции покрыты docstrings
- [ ] Обновлена документация (TOOLS.md, EXAMPLES.md)
- [ ] Добавлена запись в CHANGELOG.md
- [ ] Сервер запускается без ошибок
- [ ] Новые инструменты протестированы вручную
- [ ] Commit messages следуют Conventional Commits

### Описание PR

Включите в описание PR:

1. **Что изменилось**: Краткое описание изменений
2. **Зачем**: Какую проблему это решает
3. **Как тестировать**: Шаги для проверки изменений
4. **Скриншоты** (если применимо)
5. **Breaking changes** (если есть)

Пример:

```markdown
## Что изменилось
Добавлен новый инструмент `search_issues` для поиска задач по тексту

## Зачем
Closes #123
Позволяет пользователям искать задачи без знания их ID

## Как тестировать
1. Запустите сервер
2. Вызовите `search_issues` с query="test"
3. Проверьте, что возвращаются релевантные задачи

## Breaking changes
Нет
```

## Вопросы?

Если у вас есть вопросы:
- Создайте issue с меткой `question`
- Напишите в Discussions (если включены)

Спасибо за вклад в проект! 🚀
