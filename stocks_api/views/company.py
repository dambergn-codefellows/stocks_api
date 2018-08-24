from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response

class CompanyAPIView(APIViewSet):
    def retrieve(self, request, id=None): #will require resourses to test
    # http :6543/api/v1/company/{symbol}
        return Response(json={'message': 'Provided a single resource for {id}'}, status=200)