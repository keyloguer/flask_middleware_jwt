# Flask Middleware JWT

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)]()
[![PyPi download](/pypi.svg)](https://pypi.org/project/flask-middleware-jwt/)

<img src="https://miro.medium.com/max/1200/1*2I8mZ4C6C5u0n_LSninJ1A.png" alt="drawing" width="300px"/>

This library was originally developed in a project where it was necessary to make usage of the same package among several smaller services on a microservice archictecture. 
It was needed that a JWT token was validated on requests, checking whether it had the required structure and if it hadn't expired. <br>

Flask Middleware JWT aims to improve a flask micro-framework with a new way of authenticating your services. For further reading on it's functionalities, plase check [our medium article](https://medium.com/@daniel.zitei/flask-middleware-jwt-1ae476a360e6?sk=2e90d6074ac3ebf116fe3024ad62f).


## Instalation

Run the command in shell:

> pip3 install flask-middleware-jwt

## App Configuration

Example on how to set your flask app configuration: 

| app.config | possible values |
|------------|------------------|
|MIDDLEWARE_URL_IDENTITY| http://0.0.0.0:5000 |
|MIDDLEWARE_VERIFY_ENDPOINT | /token/verify |
|MIDDLEWARE_BEARER | True or False |
|MIDDLEWARE_VERIFY_HTTP_VERB | GET or POST |
|JWT_SECRET | your secret |
|JWT_ALGORITHMS| ['HS256']|


## Annotations

### JWT Token
@middleware_jwt_required 

Validates initially if tokens via headers in requests contains "Autorization" before your jwt token and returns an invalid token message otherwise. 

## Example - How to run

To start your app, please follow these instructions: <br>
Navigate to the <strong>'example' directory</strong> and execute either of the following commands on <strong>both</strong> 'identity' and 'your_app' folders: 
>flask run

or 

>python3 app.py 

Once both services are up and running, use your prefered API Client, such as Postman to test your app. 

## Requests

<strong>Login:</strong>

For API Clients, input these parameters: <br>

- Headers:

> <strong>Content-Type:</strong> application/json <br>

- POST
>  <strong>endpoint:</strong> http://127.0.0.1:5000/login

For Curl Commands: 
 
> curl -d '{"username": "test", "password": "test"}' -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/login 

A successful response should return you <br>
{"access_token": "you_token"}

<br>
<strong>Token Verification:</strong>

For API Clients, input these parameters: <br>

- Headers:

> <strong>Key:</strong> Authorization <br>
> <strong>Bearer:</strong> jwt token returned from login request

- GET
>  <strong>endpoint:</strong> http://127.0.0.1:5000/your_path/verify

For Curl Commands: 
 
> curl -X GET -H "Authorization: Bearer you_token" http://127.0.0.1:5000/your_path/verify

Body of the message returned should be either related to your token integrity or in case of sucessful request: <br>

{"message": "Authorization Valid"}

<br>
<strong>Test Response:</strong>

> curl -X GET -H "Authorization: Bearer your_token" http://127.0.0.1:5001

Body of the message returned should be either related to your token integrity or in case of sucessful request: <br>

Hello World!

## License

Apache License, Version 2.0
