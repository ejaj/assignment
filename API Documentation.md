API END POINT:
###User Registration:
url : http://127.0.0.1:8000/api/v1/user/register
Request: POST

Body parameters

name, email, password

Response:

{
    "id": 3,
    "name": "Kazi",
    "email": "ejajd@gmail.com"
}

###User API Token


url: http://127.0.0.1:8000/api/v1/user/api/token/
Request: POST

Body

email, password

Response


{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDgzNTYwMSwiaWF0IjoxNjQ0NzQ5MjAxLCJqdGkiOiI0MTU1OTRkOWUxYjg0NTgwOTFkNDQ5NTI2YzI5Yjg1YyIsInVzZXJfaWQiOjJ9.45ZFaCe1ENU_Wyr1Dgrw1tvFxYOBP1k8z2TZMM3TJ54",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NzQ5NTAxLCJpYXQiOjE2NDQ3NDkyMDEsImp0aSI6IjZjZWUzZWRkZjFhZTQ4ZGFiNDAwMjUyOTFiNjg0Mzc0IiwidXNlcl9pZCI6Mn0.kpI3FdViUB5mL3xDzvhJqJEIB3kI334YIvYVZZB1jlo"
}

### User this token for authenication request

### Refresh Token end point
url: http://127.0.0.1:8000/api/v1/user/api/token/refresh/
Request: POST

### List of currencies

url: http://127.0.0.1:8000/api/v1/currencies/
Request: GET

Authentication: Token

Response

[
    {
        "id": 2,
        "name": "JPY",
        "value": 115.93055,
        "convert_bangla": "এক শত পনের দশমিক নয় তিন  পাঁচ পাঁচ",
        "created_at": "2022-02-13T10:01:20.325600Z",
        "updated_at": "2022-02-13T10:01:20.325646Z"
    },
    {
        "id": 1,
        "name": "PGK",
        "value": 5.93055,
        "convert_bangla": "পাঁচ দশমিক নয় তিন  পাঁচ পাঁচ",
        "created_at": "2022-02-13T10:00:51.545911Z",
        "updated_at": "2022-02-13T10:06:17.459422Z"
    }
]

### Single Currency:

Url: http://127.0.0.1:8000/api/v1/currencies/{id}

Request : GET

Authentication: Token

Response

 {
        "id": 1,
        "name": "PGK",
        "value": 5.93055,
        "convert_bangla": "পাঁচ দশমিক নয় তিন  পাঁচ পাঁচ",
        "created_at": "2022-02-13T10:00:51.545911Z",
        "updated_at": "2022-02-13T10:06:17.459422Z"
 }


###Update Currency :

Url: http://127.0.0.1:8000/api/v1/currencies/{id}

Request POST:
Authentication: Token

Response:

{
        "id": 1,
        "name": "PGK",
        "value": 5.93055,
        "convert_bangla": "পাঁচ দশমিক নয় তিন  পাঁচ পাঁচ",
        "created_at": "2022-02-13T10:00:51.545911Z",
        "updated_at": "2022-02-13T10:06:17.459422Z"
 }


###Create Currency:

Url: http://127.0.0.1:8000/api/v1/currencies/
Request POST:
Authentication: Token

Body
name, value


Response:

{
        "id": 1,
        "name": "PGK",
        "value": 5.93055,
        "convert_bangla": "পাঁচ দশমিক নয় তিন  পাঁচ পাঁচ",
        "created_at": "2022-02-13T10:00:51.545911Z",
        "updated_at": "2022-02-13T10:06:17.459422Z"
 }


###Delete Currency: 

Url: http://127.0.0.1:8000/api/v1/currencies/{id}
Request DELETE:
Authentication: Token



