from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    def list(self, request):
        return Response(json={'message': f'Provided a list of stocks'}, status=200)

    def retrieve(self, request): #will require resourses to test
        return Response(json={'message': 'Listing one record'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request, id=None): #will require resourses to test
        return Response(json={'message': 'Deleted the record'}, status=204)