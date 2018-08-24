- .ssh
```
Host stocks
  Hostname "DNS or IP address"
  User ubuntu
  IdentityFile ~/.ssh/stocks_api.pem
```
save as config
chmod 4000 stock_api.pem

```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install nginx build-essential python-dev python3-pip -y
cd ~
git clone "git repository" src
cd src
which pip3
pip3 install -e . --user
cd ~
# Configureing NGINX
sudo rm /etc/nginx/nginx.conf
sudo nano /etc/nginx/nginx.conf
# paste config settings
user www-data;
    worker_processes 4;
    pid /var/run/nginx.pid;

    events {
        worker_connections 1024;
        # multi_accept on;
    }

    http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        server_names_hash_bucket_size 128;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;
        gzip_disable "msie6";

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }
#CRTL + x
sudo nano /etc/nginx/conf.d/stocks_api.conf
upstream (stocks_api) {
        server 127.0.0.1:8000;
    }

    server {
        listen 80;

        server_name (EC2 public DNS);

        access_log  /home/ubuntu/.local/nginx.access.log;

        location / {
            proxy_set_header        Host $http_host;
            proxy_set_header        X-Real-IP $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header        X-Forwarded-Proto $scheme;

            client_max_body_size    10m;
            client_body_buffer_size 128k;
            proxy_connect_timeout   60s;
            proxy_send_timeout      90s;
            proxy_read_timeout      90s;
            proxy_buffering         off;
            proxy_temp_file_write_size 64k;
            proxy_pass http://(project_name);
            proxy_redirect          off;
        }
    }

# Syntax validation
sudo nginx -t
sudo service nginx status
sudo restart
pip3 install gunicorn
which gunicorn
/home/ubuntu/.local/bin/gunicorn
sudo nano /etc/systemd/system/gunicorn.service
# gunicorn.service
    [Unit]
    Description=(your description)
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/src
    ExecStart=/home/ubuntu/.local/bin/gunicorn --access-logfile - -w 3 --paste production.ini

    [Install]
    WantedBy=multi-user.target
CTRL + x
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```





### Don't create a folder for the project, just navigate to the folder you want to project to live.
```
#if not already installed
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