# Troubleshooting Guide

## Распространенные ошибки и их решения

### HTTP 404 Not Found для операций с задачами

**Проблема:** 
```
Error executing tool update_issue: HTTP 404 Not Found: {"error":"The requested resource does not exist."}
```

**Причины:**
1. Неверный `issue_id` (UUID устарел или неправильный)
2. Задача была удалена или перемещена
3. Неправильный `project_id`

**Решение:**
1. Используйте `get_issue_details_by_readable_id` для получения актуального UUID:
   ```json
   {
     "issue_readable_id": "PROFI-48"
   }
   ```

2. Проверьте существование задачи через readable identifier:
   ```json
   {
     "project_identifier": "PROFI",
     "issue_identifier": "48"
   }
   ```

3. **Рекомендация:** Всегда используйте readable ID (например, PROFI-48) для поиска задач, а затем получайте актуальные UUID для операций.

### HTTP 400 Bad Request для комментариев

**Проблема:**
```
Error executing tool add_issue_comment: HTTP 400: {"error":"The payload is not valid"}
```

**Причины:**
1. Неверный `issue_id` (задача не существует)
2. Слишком длинный комментарий (>10KB)
3. Неправильное экранирование HTML
4. Отсутствуют обязательные поля

**Решение:**
1. Проверьте существование задачи перед добавлением комментария
2. Ограничьте размер комментария до 5-8KB
3. Используйте простой HTML без сложных тегов
4. Убедитесь, что `comment_html` не пустой

### Анализ логов

**Успешные операции:**
```
HTTP Request: PATCH https://plane.equiply.ru/.../bdbe957a-1c37-480f-948a-c83ccbf985e5/ "HTTP/1.1 200 OK"
HTTP Request: POST https://plane.equiply.ru/.../bdbe957a-1c37-480f-948a-c83ccbf985e5/comments/ "HTTP/1.1 201 Created"
```

**Проблемные операции:**
```
HTTP Request: PATCH https://plane.equiply.ru/.../7e0f17d9-3b3f-44d4-98e4-d2ffb1a929b4/ "HTTP/1.1 404 Not Found"
HTTP Request: POST https://plane.equiply.ru/.../7e0f17d9-3b3f-44d4-98e4-d2ffb1a929b4/comments/ "HTTP/1.1 400 Bad Request"
```

**Вывод:** UUID `7e0f17d9-3b3f-44d4-98e4-d2ffb1a929b4` неактуален, используйте `bdbe957a-1c37-480f-948a-c83ccbf985e5`.

## Рекомендуемый workflow

### 1. Поиск задачи
```python
# Используйте readable ID для поиска
details = await get_issue_details_by_readable_id("PROFI-48")
```

### 2. Операции с задачей
```python
# Извлеките актуальные UUID из результата поиска
issue_data = json.loads(details)
issue_id = issue_data["issue_id"]
project_id = issue_data["project_id"]

# Выполните операции с актуальными ID
await update_issue(project_id, issue_id, state="new_state_id")
await add_issue_comment(project_id, issue_id, "Комментарий")
```

### 3. Проверка результатов
- Всегда проверяйте успешность операций через логи
- В случае 404/400 ошибок - обновите UUID через поиск
- Для длинных комментариев разбивайте на несколько коротких

## Отладка

### Включение подробных логов
Модифицируйте `request_helper.py` для добавления debug информации:

```python
# Добавлено в версии: логирование всех HTTP запросов
print(f"HTTP Request: {method.upper()} {url} \"{response.status_code} {response.reason_phrase}\"")
```

### Проверка данных перед отправкой
```python
# Проверка размера комментария
if len(comment_html) > 8000:
    print(f"Warning: Comment too long ({len(comment_html)} chars), consider splitting")

# Проверка существования issue_id
try:
    await get_issue(project_id, issue_id)
except PlaneAPIError as e:
    if "404" in str(e):
        print(f"Issue {issue_id} not found, refreshing from readable ID")
```

## Типичные сценарии

### Scenario 1: Обновление статуса задачи
1. Найти задачу: `get_issue_details_by_readable_id("PROFI-48")`
2. Получить актуальные UUID и state_id
3. Выполнить обновление: `update_issue(project_id, issue_id, state=new_state)`

### Scenario 2: Добавление развернутого комментария
1. Проверить длину HTML комментария (<8KB)
2. Убедиться в существовании задачи
3. При необходимости разбить на несколько коментариев
4. Добавить комментарий: `add_issue_comment(project_id, issue_id, comment_html)`

## Контрольный список

- [ ] UUID актуальны (получены через readable ID)
- [ ] Размер комментария разумный (<8KB)
- [ ] HTML корректно сформирован
- [ ] Проект и задача существуют
- [ ] API ключ действителен
- [ ] Права доступа достаточны