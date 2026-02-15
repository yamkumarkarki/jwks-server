# JWKS Server

This project is a basic JSON Web Key Set (JWKS) server built with Flask in Python. It provides a RESTful API to serve public keys with unique identifiers (kid) for verifying JSON Web Tokens (JWTs). The server also issues JWTs, supports key expiry for enhanced security, and handles the issuance of expired JWTs upon request.

## Features
- RSA Key Pair Generation
- Key Expiry and Rotation
- JWKS Endpoint to Serve Public Keys
- Authentication Endpoint to Issue JWTs (Valid and Expired)
- JWT Header Includes `kid`
- Invalid HTTP Method Handling
- Unit Tests with 90%+ Coverage
- Linted and organized

## Installation

### Prerequisites
- Python 3.9+ and pip installed

### Create/Activate Virtual Environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate


```bash
pip install flask cryptography pyjwt pytest pytest-cov flake8
```
or,
```bash
pip3 install flask cryptography pyjwt pytest pytest-cov flake8
```

## Project Structure
```
-------------- jwks-server-1 --------------
                    |
  --------------------------------------------
  |                 |                        |
 app/             tests/               (root files)
  |                 |                        |
  |                 |              -------------------------
  |                 |              |          |            |
 __init__.py   test_routes.py     run.py    README.md   screenshots/
 key_manager.py                                   (gradebot + coverage SS)
 routes.py

            
```

## Usage

### Run the Server
```bash
python3 run.py
```
or,
```bash
python run.py
```
The server will start on `http://127.0.0.1:8080`

### Endpoints

#### 1. JWKS Endpoint
- `GET /.well-known/jwks.json` – Returns valid public keys in JWKS format.
- Invalid methods (POST, PUT, DELETE, PATCH) – Returns `405 Method Not Allowed`.

#### 2. Authentication Endpoint
- `POST /auth` – Returns a valid JWT.
- `POST /auth?expired=true` – Returns an expired JWT.
- Invalid methods (GET, PUT, DELETE, PATCH, HEAD) – Returns `405 Method Not Allowed`.

## Testing

### Run Tests
```bash
PYTHONPATH=$(pwd) pytest tests/
```

### Run Tests with Coverage
```bash
PYTHONPATH=$(pwd) pytest --cov=app tests/
```
or, 
```bash
pytest --cov=app tests/
```

### Test Coverage Result
```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
app/__init__.py          6      0   100%
app/key_manager.py       9      0   100%
app/routes.py           44      6    86%   15-16, 37-46, 77
--------------------------------------------------
TOTAL                   59      6    90%
```

## Linting
Ensure the code follows PEP8 guidelines using flake8:
```bash
flake8 app/
```
## Testing the Server Manually

### 1. Get a Valid JWT:
```bash
curl -X POST http://127.0.0.1:8080/auth
```
Sample output:
```json
{
  "token": "eyJhbGciOiJSUzI1NiIsImtpZCI6I..."
}
```

### 2. Get Public Keys (JWKS):
```bash
curl -X GET http://127.0.0.1:8080/.well-known/jwks.json
```

Sample output:
```json
{
  "keys": [
    {
      "alg": "RS256",
      "e": "AQAB",
      "kid": "58d8b280-66fd-4f6b-b47b-d0c0ebc8b974",
      "kty": "RSA",
      "n": "q6jdjMX6icdCC4JrhDYcF9aINY8ZfgR...",
      "use": "sig"
    }
  ]
}
```

## Run the test client
```bash
cd ~/Downloads/CSCE3550_Darwin_arm64
chmod +x gradebot
./gradebot project-1 --dir="/Users/yamkumarkarki/Documents/jwks-server-1" --run="python3 run.py"
```
## Gradebot output
```
┌────────────────────────────────────────┬────────┬─────────┬────────────────────────────────────────────────────────┐
│                  NAME                  │ POINTS │ AWARDED │                         NOTES                          │
├────────────────────────────────────────┼────────┼─────────┼────────────────────────────────────────────────────────┤
│ /auth valid JWT authN                  │  15.00 │   15.00 │                                                        │
│ /auth?expired=true JWT authN (expired) │   5.00 │    5.00 │                                                        │
│ Proper HTTP methods/Status codes       │  10.00 │   10.00 │                                                        │
│ Valid JWK found in JWKS                │  20.00 │   20.00 │                                                        │
│ Expired JWT is expired                 │   5.00 │    5.00 │                                                        │
│ Expired JWK does not exist in JWKS     │  10.00 │   10.00 │                                                        │
│ Quality                                │  20.00 │    0.00 │ Connect call failed: unauthenticated: 401 Unauthorized │
├────────────────────────────────────────┼────────┼─────────┼────────────────────────────────────────────────────────┤
│                           jolly_snyder │ Grade: │  76.47% │                                                        │
└────────────────────────────────────────┴────────┴─────────┴────────────────────────────────────────────────────────┘  
```


