db.createUser(
  {
    user: "one",
    pwd:  12345,   // or cleartext password
    roles: [ { role: "readWrite", db: "mydb" },
             { role: "read", db: "mydb" } ]
  }
)