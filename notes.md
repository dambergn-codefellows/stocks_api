### Don't create a folder for the project, just navigate to the folder you want to project to live.
```
#if already installed
  sudo pip install cookiecutter --user
cookiecutter gh:Pylons/pyramid-cookiecutter-alchemy
cd "project_folder"
pipenv --three
pipenv shell
pipenv install -e ".[testing]"
pip install pyramid-restful-framework
```
- Delete templates directory from nested project demo
- Create tests directory, move tests to directory
- Important file,[__init__.py], [routes.py], [views*]
- Comment __init__.py > config.inclues('.models')
- Delete __init__.py > config.include('pyramid_jinja2')
- Delete contents of views > default.py
- Delete contents of views > notfound.py
- https://pyramid-restful-framework.readthedocs.io/en/docs/user/quickstart.html

- add to __init__.py > config.include('pyramid_restful')
- in views > default.py
```
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
  """
  """
  message = 'Hello World'
  return Response(body=message, status=200)
```
- to start
```
pserve development.ini --reload
```
- create 'application_name'.py in views folder
```
#weather.py

from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class WeatherAPIView(APIViewSet):
    def list(self, request):
        return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request): #will require resourses to test
        return Response(json={'message': 'Listing one record'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request): #will require resourses to test
        return Response(json={'message': 'Deleted the record'}, status=204)
```

- in routes.py add
```
from pyramid_restful.routers import ViewSetRouter
from .views.weather import WeatherAPIView
# from .views.auth import AuthAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('/api/v1/weather', WeatherAPIView, 'weather')
    # router.register('/api/v1/auth', AuthAPIView, 'auth')
```
- to start
```
pserve development.ini --reload
```