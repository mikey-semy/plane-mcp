#!/bin/bash

# Скрипт обновления Plane до v1.1.0 в Dokploy

echo "========================================"
echo "Обновление Plane v0.27.1 → v1.1.0"
echo "========================================"

# 1. Остановить все контейнеры
echo "1. Останавливаем контейнеры..."
docker-compose down

# 2. Удалить старые образы
echo "2. Удаляем старые образы..."
docker images | grep "makeplane/plane" | grep "v0.27.1" | awk '{print $3}' | xargs -r docker rmi

# 3. Скачать новые образы
echo "3. Скачиваем образы v1.1.0..."
docker-compose pull

# 4. Запустить миграции БД
echo "4. Запускаем миграции базы данных..."
docker-compose up migrator

# 5. Запустить все сервисы
echo "5. Запускаем все сервисы..."
docker-compose up -d

# 6. Проверка
echo "6. Ждём 30 секунд для запуска сервисов..."
sleep 30

echo ""
echo "========================================"
echo "Проверка External API..."
echo "========================================"

# Проверка /api/v1/
curl -s https://plane.equiply.ru/api/v1/users/me/ \
  -H "X-API-Key: plane_api_e63e2f6e51ef4192bc817216b2ed8a58" \
  | jq '.' || echo "External API не отвечает или нет jq"

echo ""
echo "========================================"
echo "Обновление завершено!"
echo "========================================"
echo ""
echo "Логи API сервера:"
docker-compose logs api | tail -20

echo ""
echo "Статус контейнеров:"
docker-compose ps
