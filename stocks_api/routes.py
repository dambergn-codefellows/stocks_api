from pyramid_restful.routers import ViewSetRouter
from .views.stocks_api import StocksAPIView
from .views.auth import AuthAPIView
from .views.portfolio import PortfolioAPIView
from .views.company import CompanyAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/api/v1/auth/')
    config.add_route('portfolio', '/api/v1/portfolio/')
    config.add_route('stock', '/api/v1/stock/')
    config.add_route('company', '/api/v1/company/')

    router = ViewSetRouter(config)
    # router.register('api/v1/company', CompanyAPIView, 'company')
    # router.register('api/v1/stock', StocksAPIView, 'stock')
    # router.register('/api/v1/auth', AuthAPIView, 'auth')
    # router.register('/api/v1/portfolio', PortfolioAPIView, 'portfolio')
    