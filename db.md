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