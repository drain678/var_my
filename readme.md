## установка джанги
```bash
pip install Django
```
```bash
pip install poetry
```

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

### если (просмотр базы)
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


## если 
Gracefully stopping... (press Ctrl+C again to force) Error response from daemon: driver failed programming external connectivity on endpoint prometheus (eb866954b116f95af9eb3146189e189ece5a1cd7d584b0f4aea2398ad2d5678a): Bind for 0.0.0.0:9090 failed: port is already allocated

Контейнер prometheus_old_two СЕЙЧАС РАБОТАЕТ и он уже занял порт 9090
Поэтому:
Docker пытается создать новый контейнер prometheus
но порт 9090 уже занят другим Prometheus

надо остановить контейнер, который запущен (взять правильное имя)
```bash
docker stop prometheus_old_two
```
удалить
```bash
docker rm prometheus_old_two
```

## если на  http://localhost:8080/
показывается nginx за место индекса, проверить названия файлов и содержимое. еще проверить навсякий на наличие article и k_exam


## на всякий докер
```bash
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)
```
```bash
sudo apt update
```
```bash
sudo apt install ca-certificates curl
```
```bash
sudo install -m 0755 -d /etc/apt/keyrings
```
```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```
```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```
```bash
sudo apt update
```
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```