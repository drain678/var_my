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
Посмотреть структуру таблицы student:
```bash
\d student
```
Посмотреть что в таблице:
```bash
SELECT * FROM student;
```
Выйти из postgres=#
```bash
\q    
```
а из root@d2490b5070f6:/#  - я нажала контрол D



## переименовать контейнер prometheus
посмотреть контейнеры 
```bash
docker ps -a
```
переименовать
```bash
docker rename prometheus prometheus_old
```
удалить по имени
```bash
docker rm prometheus
```
удалить по id
```bash
docker rm d76208752437
```


### если
 после docker exec -it kvali-db-1 bash вывелось это - root@d2490b5070f6:/# psql -U user -d dbname psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL: role "user" does not exist root@d2490b5070f6:/#

надо узнать какие пользователи есть в контейнере 
```bash
psql -U postgres
```
узнать имя пользователя
```bash
\du
```
узнать имя базы данных
```bash
\l
```
потом
```bash
\q
```
и зайти здраво
```bash
psql -U <реальный_пользователь> -d <реальная_база>
```