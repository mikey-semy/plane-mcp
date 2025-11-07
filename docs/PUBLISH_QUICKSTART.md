# Быстрая публикация в NPM

## Перед публикацией

1. **Проверьте версию** в `package.json`:
   ```bash
   npm version patch  # или minor/major
   ```

2. **Тестирование пакета**:
   ```bash
   npm pack
   npm install -g .\mikey-semy-plane-mcp-0.1.0.tgz
   # Тест (нужен uv и переменные окружения)
   plane-mcp
   npm uninstall -g @mikey-semy/plane-mcp
   ```

3. **Логин в NPM** (если ещё не залогинены):
   ```bash
   npm login
   ```

## Публикация

```bash
# Первая публикация (нужен --access public для scoped пакетов)
npm publish --access public

# Последующие обновления
npm publish
```

## После публикации

Пакет будет доступен:
```bash
# Использование без установки
npx @mikey-semy/plane-mcp

# Глобальная установка
npm install -g @mikey-semy/plane-mcp
plane-mcp
```

## Проверка публикации

```bash
npm view @mikey-semy/plane-mcp
```

Пакет появится на: https://www.npmjs.com/package/@mikey-semy/plane-mcp

---

Подробные инструкции: [NPM_PUBLISH.md](NPM_PUBLISH.md)
