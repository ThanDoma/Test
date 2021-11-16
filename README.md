Каждый работает с веткой, название которой соответсвует с его фамилией
Как только вы написали код - делаете запрос на добавление его в основную ветвь
Прежде чем отправить запрос - проверьте код на работоспособность, чтобы в основной ветке был только рабочий код
#### Сборка flask в docker
    docker build -t . flask-test
Запуск
    docker run -itd -p 8000:5000 --name backend flask-test
Проверим соединение. Откройте новый терминал и выполните следующую команду 
    curl localhost:8000
Выполните несколько раз
Просмотрим логи контейнера, следующей командой
    docker logs backend
В браузере перейдите по адресу localhost:8000 или 127.0.0.1:8000

#### Подключаем mongodb

docker exec -it name-container bash

root@88059d6f1015:/# mongo
MongoDB shell version v5.0.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("3c8c36ad-f1f3-4273-82cc-7730853b8013") }

MongoDB server version: 5.0.3
================
Warning: the "mongo" shell has been superseded by "mongosh",
which delivers improved usability and compatibility.The "mongo" shell has been deprecated and will be removed in
an upcoming release.
We recommend you begin using "mongosh".
For installation instructions, see
https://docs.mongodb.com/mongodb-shell/install/
================
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
        https://community.mongodb.com



команда  db
отобразит текущую db


Если база данных не существует, MongoDB создает базу данных при первом сохранении данных для этой базы данных. Таким образом, вы можете переключиться на несуществующую базу данных и выполнить в mongosh следующую операцию:

> use myDB
switched to db myDB

https://code-maven.com/slides/docker/python-flask-mongodb

https://realpython.com/introduction-to-mongodb-and-python/


https://www.w3schools.com/python/python_mongodb_insert.asp


https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc



https://dev.to/herbzhao/docker-flask-vue-nginx-mongodb-deployment-and-development-in-one-package-3-1l9g
