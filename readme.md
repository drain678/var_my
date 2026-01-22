## команда для миграций внутри докера

```bash
docker compose exec app python manage.py migrate
```
## посмотреть базу
Посмотреть запущенные контейнеры:
```bash
docker ps
```
Зайти ВНУТРЬ контейнера с БД:
```bash
docker exec -it kvali-db-1 bash 
```
Подключиться к PostgreSQL:
```bash
psql -U postgres -d postgres
```
Посмотреть таблицы:
```bash
 \dt
```
Посмотреть структуру таблицы students:
```bash
\d students 
```
Посмотреть что в таблице:
```bash
SELECT * FROM students;
```bash
выйти \q из postgres=# а из root@d2490b5070f6:/#  я нажала контрол D
```