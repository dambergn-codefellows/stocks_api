from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='company', renderer='json', request_method='GET')
def home_view(request):
    """
    """
    message = f'company GET route hit\n'

    return Response(body=message, status=200) 

class CompanyAPIView(APIViewSet):
    def retrieve(self, request, id=None): #will require resourses to test
    # http :6543/api/v1/company/{symbol}
        return Response(json={'message': 'Provided a single resource for {id}'}, status=200)

