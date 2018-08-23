from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
  """
  """
  message = 'Hello World'
  return Response(body=message, status=200)