from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='stock', renderer='json', request_method='GET')
def home_view(request):
    """
    """
    message = 'stock GET route hit\n'

    return Response(body=message, status=200) 

@view_config(route_name='stock', renderer='json', request_method='POST')
def home_view(request):
    """
    """
    message = 'stock POST route hit\n'

    return Response(body=message, status=201) 

@view_config(route_name='stock', renderer='json', request_method='DELETE')
def home_view(request):
    """
    """
    message = 'stock DELETE route hit\n'

    return Response(body=message, status=204) 

class StocksAPIView(APIViewSet):
    def list(self, request):
        return Response(json={'message': 'Provided a list of stocks'}, status=200)

    def retrieve(self, request): #will require resourses to test
        return Response(json={'message': 'Listing one record'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request, id=None): #will require resourses to test
        return Response(json={'message': 'Deleted the record'}, status=204)

