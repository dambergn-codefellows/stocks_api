from pyramid_restful.routers import ViewSetRouter
from .views.stocks_api import stocksAPIView
from .views.auth import AuthAPIView
from .views.portfolio import PortfolioAPIView
from .views.company import CompanyAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('/api/v1/stock', stocksAPIView, 'stock')
    router.register('/api/v1/auth', AuthAPIView, 'auth')
    router.register('/api/v1/portfolio', AuthAPIView, 'portfolio')
    router.register('/api/v1/company', AuthAPIView, 'company')