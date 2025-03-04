Запуск:
"docker-compose up"

Сброс всех действий:
"docker-compose down -v --remove-orphans", 
"docker rmi $(docker images -q)"

После запуска желательно создать суперпользователя:
"docker exec -it merch_store_web python manage.py createsuperuser",
затем нужно ввести имя пользователя, e-mail (можно пропустить) и два раза пароль
