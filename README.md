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

Подключаем mongodb

https://code-maven.com/slides/docker/python-flask-mongodb

https://realpython.com/introduction-to-mongodb-and-python/


https://www.w3schools.com/python/python_mongodb_insert.asp