from ..products.serializers import ProductSerializers
from products.models import Product
from rest_framework import (
    generics,
    serializers,
    viewsets,
    status
)
from rest_framework import permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response


class ProductViewsets(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers

    def list(self, request, *args, **kwargs):
        instance = Product.objects.all() # [ obj1, obj2, objn]
        serializer = self.serializer_class(instance, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        param = request.data

        param['user_id'] = request.user.id
        product = Product.objects.create(**param)

        serializer = self.serializer_class(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
            product.name = request.data['name']
            product.price = request.data['price']
            product.type_id = request.data['type_id']

            serializer = self.serializer_class(product, many=False)

            return Response(serializer.data)
        except:
            return Response({"error": "Something wrong."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, *args, **kwargs):
        # try:
        #     product = Product.objects.get(id=kwargs['pk'])
        #     product.delete()
        # except:
        #     return Response({'message': "product not found."}, status=status.HTTP_404_NOT_FOUND)

        product = generics.get_object_or_404(Product, id=kwargs['pk'])
        product.delete()
    
        return Response({
            "message": "product deleted."
        })