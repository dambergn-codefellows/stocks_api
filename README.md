# Stocks API

## To run
```
pipenv shell
pserve development.ini --reload
```
```
pipenv install jupyter
pipenv install numpy
pipenv install pandas
pipenv install scipy
jupyter-notebook
```

# Version 1.2.0

## Version 1.0.0
- [X]Disable the unnecessary functionality of your scaffold, by commenting out the include() statements in your __init__.py:main() function; we will not be using Jinja2 templating (Delete that line) or Models for the time being
- [X]Delete the templates/ directory
- [X]Remove the contents of default.py and notfound.py
- [X]Ensure that your application can accept requests to the following routes, and returns the appropriate response:
 - NOTE: You do not need to build any controller functionality other than a simple response with a status and JSON encoded message
- [X]GET / - the base API route
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
- [X]POST /api/v1/auth/ username=user password=seekret email=who@example.com - for registering a new account and signing up
```
Status code: 201 CREATED
Response body:
  {
      "username": "some user",
      //...
  }
```
- [X]GET /api/v1/portfolio/{id}/ - for a user’s portfolio
```
Status code: 200 OK
Response body:
  {
      "portfolio": "dummy data",
      //...
  }
```
- [X]POST /api/v1/stock/ name=data symbol=data portfolio_id=int ... - for creating a stock record associated with a user’s portfolio
```
Status code: 201 CREATED
Response body:
  {
      "company": "dummy data",
      //...
  }
```
- [X]GET /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
```
Status code: 200 OK
Response body:
  {
      "company": "dummy data",
      //...
  }
```
- [X]DELETE /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
```
Status code: 204 NO CONTENT
```
- [X]GET /api/v1/company/{symbol}/ - for retrieving company detail from 3rd party API, where {symbol} is variable
```
Status code: 200 OK
Response body:
  {
      "company": "dummy data",
      //...
  }
```

### Version 1.1.0 / Deployment
- [X]Deploy your API to AWS!
- [X]It’s important that you complete your deployment in a programmatic way today, so please follow the deployment tutorial or lecture videos closely if you’re unclear on how to proceed.

### Version 1.2.0
- [X]In your models/ directory, create a file called portfolio.py.
- [ ]You will create a Portfolio class with the following attributes:
- [ ]id, name, date_created, date_updated
- [ ]Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
- [ ]Define two class methods on your Portfolio class:
- [ ]one(): Retrieve a single instance from the database by the primary key for that record
- [ ]new(): Create a single new instance of the Portfolio class
- [ ]In your models/ directory, create a file called stock.py.
- [ ]You will create a Stock class with the following attributes, which are being defined to mirror the data that you will retrieve from your 3rd party API:
- [ ]id, symbol, companyName, exchange, industry, website, description, CEO, issueType, sector, date_created, date_updated
- [ ]Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
- [ ]Define three class methods on your Stock class:
- [ ]one(): Retrieve a single instance from the database by the primary key for that record
- [ ]new(): Create a single new instance of the Stock class
- [ ]destroy(): Remove a single instance from the database by the primary key for that record
- [ ]In your models/ directory, create a file called schemas.py for your model serializers.
- [ ]You will define two Marshmallow schemas in this file, one for PortfolioSchema and one for StockSchema.
- [ ]Each of these will simply define the model they require for serialization (we’ll further define these later in the course…)
- [ ]In your views/portfolio.py file, you will further define the following View Class Controllers:
- [ ]PortfolioAPIView - Controller interactions with your Portfolio model/schema
- [ ]StockAPIView - Controller interactions with your Stock model/schema
- [ ]CompanyAPIView - 3rd-party API interactions for requesting company data for your portfolio
You will be using the requests library and a free API from IEX TRADING, which does not require the use of an API key at this point.
- [ ]We are specifically interested in the Company Info and the Time Series info, both of which are accessible via an API call using a companies Stock Symbol.
- [ ]Using your model class methods, formulate an appropriate serialized response for each available endpoint / method that we configured in our last lab for this application. You may want to refer back to the LAB.md specification for each of those endpoints to review the functionality required.

### Version 1.3.0
- [ ]Using the diagram below as a guide update your models/ directory with the new account.py, role.py, and associations.py files, and create each of the tables
- [ ]Ensure that your model relationships are functional
- [ ]Ensure that you’ve taken advantage of the SQLAlchemy relationship method to create additional functionality within your code base for accessing those new relationships
- [ ]Add your new models to the Initialization Script, drop and recreate your DB, and initialize again with your new tables
![example](https://codefellows.github.io/code-401-python-guide/curriculum/class-12-model-relationships/assets/EDR_class_12.png)

### Version 1.4.0
- [ ]Install and configure the use of the pyramid_jwt library in your application, and configure the Pyramid policies and permissions for your views and routes
- [ ]You will need to configure your RootACL class in the project’s __init__.py file before your associated permissions on the routes/views will take effect
- [ ]In models/account.py:
- [ ]Refactor your Account model with a __init__ method, which allows your users password to be hashed by bcrypt before being stored in the database
- [ ]Create a check_credentials class method on your Account model which allows a verification of username and password, and returns None on validation failure or the Account instance on validation success
- [ ]In the views/ directory, create a new file called auth.py
- [ ]Add a new view controller class called AuthAPIView for defining your registration and login functionality
- [ ]You view controller should enable a post for registration and a get for login
- [ ]Each of these methods should construct and return a new JSON Web Token in the response, and Nothing else
- [ ]If the registration or login fails, handle those exceptions correctly with an appropriate status code and JSON response
- [ ]For example, if a user registers with an email that’s already registered in the system you will send a 409 Conflict status code with an appropriate message in the response body

### Version 1.5.0
- [ ] Using the same API (IEXTrading.com) that you consumed in your Stock API application, make an initial API call for 5 years of time series data for any major company that you’d like to work with. Some potential opportunities would be Microsoft, Google, Apple, or Amazon.
- [ ] Whatever company your choose must have at least five years of data available to work with.
- [ ] Load the data you receive into a Pandas DataFrame
- [ ] Show the first five rows of the dataset
- [ ] Show the description and the info of the dataset, utilizing the appropriate Pandas methods
- [ ] Ensure that the date column has been cast into a datetime object in your DataFrame; you will have to write this yourself.

### Version 1.6.0
- [ ] In your Jupyter Notebook:
- [ ] Implement a CandleStick visual (Bokeh) which displays the following data points for each date in the historical time series data, given a ticker symbol for your API to return data related to a single company.
- [ ] open, close, high, low
- [ ] You will also need to calculate the mid-point each ‘tail’ to place your candlestick data.
- [ ] Using resources at your disposal, Google/Bing/etc, make a decision on two additional visualizations that you feel are relevant to the stock’s time series data, which each answers a specific question, and implement those visualizations.
- [ ] You should pose your questions, any supporting data, and your conclusions in the notebook for future reference.
- [ ] In your Stock API:
- [ ] Create a new endpoint in your application, filterable via query-string, including a class-based view, and other configurations which when a request is made will generate a 5 year time series Candlestick visual and save it to the file system of your project under static/.
- [ ] For example:
- [ ] GET /api/v1/visuals/MSFT?type=candle: returns <200 OK>, and creates a new file in the file system for that chart. This should save in html format.

## Change Log

### 2018-09-05
- updated readme with todo features

### 2018-08-29
- created authentication branch
- updated readme with Version 1.4.0 requirements.

### 2018-08-28
- Updated readme with current feature requirements.
- Added requirements for Version 1.3.0
- Created relationship-model branch.
- Finished base API route return.
- Portfolio get route created.
- Stock and Company routes created.
- Version 1.0.0 functionality complete.
- Fixed F strings I thought I fixed already.
- Missed some F strings.
- Fixed deployment issues in code.
- Version 1.1.0 functionality complete.

### 2018-08-27
- Finished configuration of NGNIX for live deployment.

### 2018-08-24
- Created Ubuntu 16.04 VM
- Installed NGNIX and dependencies.
- Setup port forwarding.
- Deployed app to server.
- App is running, T/S issues with NGINX configuration.

### 2018-08-23
- Created new setup-code-review-modifications branch
- git
 - git remote add origin remote repository URL
 - git remove -v

### 2018-08-22
- Set up basic api server, working.
- Populated README.md with features and requirements.
- Added auth, portfolio, and company routes.