# flask-learning-movie-rest-api
Flask movie API w/ mongoDB
A learning project originally developed by paurakhsharma.

Start up docker environment with:
```docker
docker-compose up
```

Once Docker's up and running, you can access the api via `http://localhost:5000/api`

Accessible routes:

* `GET - /movies` - List movies
* `POST - /movies` - Create movie **(Bearer token required)**
* `GET - /movies/<id>` - Get movie
* `PUT - /movies/<id>` - Update movie **(Bearer token required, must match user who originally added movie)**
* `DELETE - /movies/<id>` - Delete movie **(Bearer token required, must match user who originally added movie)**
* `POST - /auth/sign` - Sign up user
* `POST - /auth/login` - Log user in
