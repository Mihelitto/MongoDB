# Тестовое задание, работа с MongoDB

Тестовое задание по работе с MongoDB. 
Доступны две функции:
- функция агрегации действий пользователей
```
aggregate_actions(account)
```
Получает коллекцию `account`, возвращает список пользователей с данными о последних действиях. 

- функция сопоставление платежей и начислений
```
match_payments(accrual, payment)
```
Получает коллекции `accrual` и `payment`, возвращает список сопоставленных пар платёж - начисление, и список платежей для которых не нашлось начислений.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Для работы понадобится доступ к серверу с базой данных [MongoDB](https://www.mongodb.com/)
- Создайте файл `.env` с переменными окружения (См. пункт 'переменные окружения')
- При необходимости заполните БД тестовыми данными командой `python3 fill_db.py`
- Запустите скрипт командой `python3 main.py`

## Переменные окружения

Настройки для доступа к БД берутся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следующие переменные:
- `MONGO_HOST` — адрес хоста с MongoDB (по умолчанию `localhost`)
- `MONGO_PORT` — порт (по умолчанию `27017`)
- `MONGO_PASSWORD` — пароль для доступа БД
- `MONGO_LOGIN` — логин для доступа к БД

Логин и пароль можно опустить, если контроль доступа со стороны БД не настроен.