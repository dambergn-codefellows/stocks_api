# Stocks API

# Version 1.0.0

## Features
- [ ]Disable the unnecessary functionality of your scaffold, by commenting out the include() statements in your __init__.py:main() function; we will not be using Jinja2 templating (Delete that line) or Models for the time being
- [ ]Delete the templates/ directory
- [ ]Remove the contents of default.py and notfound.py
- [ ]Ensure that your application can accept requests to the following routes, and returns the appropriate response:
 - NOTE: You do not need to build any controller functionality other than a simple response with a status and JSON encoded message
- [ ]GET / - the base API route
  ```
  Status code: 200 OK
  Response body:
      GET / - the base API route
      POST /api/v1/auth/ - for registering a new account and signing up 
      GET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio
      POST /api/v1/stock/ - for creating a new company record
      GET /api/v1/stock/{id}/ - for retrieving a companies information
      DELETE /api/v1/stock/{id} - for deleting a company record
      GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable
  ```
- [ ]POST /api/v1/auth/ username=user password=seekret email=who@example.com - for registering a new account and signing up
```
Status code: 201 CREATED
Response body:
  {
      "username": "some user",
      //...
  }
```
- [ ]GET /api/v1/portfolio/{id}/ - for a user’s portfolio
```
Status code: 200 OK
Response body:
  {
      "portfolio": "dummy data",
      //...
  }
```
- [ ]POST /api/v1/stock/ name=data symbol=data portfolio_id=int ... - for creating a stock record associated with a user’s portfolio
```
Status code: 201 CREATED
Response body:
  {
      "company": "dummy data",
      //...
  }
```
- [ ]GET /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
```
Status code: 200 OK
Response body:
  {
      "company": "dummy data",
      //...
  }
```
- [ ]DELETE /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
```
Status code: 204 NO CONTENT
```
- [ ]GET /api/v1/company/{symbol}/ - for retrieving company detail from 3rd party API, where {symbol} is variable
```
Status code: 200 OK
Response body:
  {
      "company": "dummy data",
      //...
  }
```

## Change Log

### 2018-08-22
- Set up basic api server, working.
- Populated README.md with features and requirements.