from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
  """
  """
  message = 'GET / - the base API route\n' \
    'POST /api/v1/auth/ - for registering a new account and signing up\n' \
    'GET /api/v1/portfolio/{id}/ - for retrieving a user\'s portfolio\n' \
    'POST /api/v1/stock/ - for creating a new company record\n' \
    'GET /api/v1/stock/{id}/ - for retrieving a companies information\n' \
    'DELETE /api/v1/stock/{id} - for deleting a company record\n' \
    'GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable\n' \

  return Response(body=message, status=200)

# @view_config(route_name='auth', renderer='json', request_method='GET')
# def home_view(request):
#     """
#     """
#     message = f'POST route hit\n'

#     return Response(body=message, status=200)

# @view_config(route_name='company', renderer='json', request_method='GET')
# def auth_view(request):
#   """
#   """
#   message = 'Authorization route get'
#   return Response(body=message, status=200)