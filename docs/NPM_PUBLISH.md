# Публикация в NPM

## Требования
- Node.js 18+
- NPM аккаунт (создать на [npmjs.com](https://www.npmjs.com/signup))
- Доступ к scoped package `@mikey-semy` (или создать свой scope)

## Шаги публикации

### 1. Логин в NPM

```bash
npm login
```

Введите username, password, email.

### 2. Проверка package.json

Убедитесь что версия обновлена:

```json
{
  "name": "@mikey-semy/plane-mcp",
  "version": "0.1.0",  // обновите перед публикацией
  ...
}
```

### 3. Тестирование локально

```bash
# Упаковка
npm pack

# Это создаст файл mikey-semy-plane-mcp-0.1.0.tgz

# Тестирование установки
npm install -g ./mikey-semy-plane-mcp-0.1.0.tgz

# Проверка работы
export PLANE_API_KEY="your-key"
export PLANE_WORKSPACE_SLUG="your-workspace"
plane-mcp

# Удаление тестовой установки
npm uninstall -g @mikey-semy/plane-mcp
```

### 4. Публикация

```bash
# Публикация (первый раз - нужен --access public для scoped пакетов)
npm publish --access public

# Последующие публикации
npm publish
```

### 5. Проверка публикации

```bash
# Установка из NPM
npx @mikey-semy/plane-mcp --version

# Или
npm view @mikey-semy/plane-mcp
```

## Обновление версии

```bash
# Patch версия (0.1.0 -> 0.1.1)
npm version patch

# Minor версия (0.1.0 -> 0.2.0)
npm version minor

# Major версия (0.1.0 -> 1.0.0)
npm version major

# Публикация новой версии
npm publish
```

## Unpublish (только в течение 72 часов)

```bash
# Удалить конкретную версию
npm unpublish @mikey-semy/plane-mcp@0.1.0

# Удалить весь пакет (только в течение 72 часов после публикации)
npm unpublish @mikey-semy/plane-mcp --force
```

## Важные замечания

1. **Никогда не публикуйте секреты**: убедитесь что `.env` в `.npmignore`
2. **Проверьте .npmignore**: только необходимые файлы должны попасть в пакет
3. **Тестируйте перед публикацией**: используйте `npm pack` и локальную установку
4. **Semantic Versioning**: следуйте [semver](https://semver.org/)
   - PATCH (0.0.x) - bug fixes
   - MINOR (0.x.0) - новые фичи (backward compatible)
   - MAJOR (x.0.0) - breaking changes

## После публикации

Пакет будет доступен по адресу:
- **NPM**: https://www.npmjs.com/package/@mikey-semy/plane-mcp
- **Использование**: `npx @mikey-semy/plane-mcp`
- **GitHub**: https://github.com/mikey-semy/plane-mcp

Обновите README с правильным именем пакета если используете другой scope.
