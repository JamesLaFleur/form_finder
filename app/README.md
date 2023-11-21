## Выполнение задания:
Для реализации данного тестового задания используется следующий стек технологий:

-Python
-Django
-MongoDB
-PyMongo

## Запуск приложения
Вы можете запустить данный проект с помощью контейнеров Docker Compose
1.  Для запуска приложения с помощью Docker Compose необходимо создать образы контейнеров выполнив команду в терминале:
```commandline
$ docker compose --build
```
2. Создать и запустить контейнеры выполнив команду в терминале:
```commandline
$ docker compose up
```
3. Приложение будет доступно по URL адресу http://0.0.0.0:8000

Для совершения тестовых запросов необходимо запустить файл query.py после запуска Docker Compose