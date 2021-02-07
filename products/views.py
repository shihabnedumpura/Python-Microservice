from rest_framework import viewsets
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serialzers = ProductSerializer(products, many=True)
        print('seri....', serialzers.data)
        return Response(serialzers.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk):
        pass

    def update(self, request, pk):
        pass

    def delete(self, request, pk):
        pass