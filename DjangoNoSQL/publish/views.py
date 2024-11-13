from rest_framework import generics, status
from rest_framework.response import Response

from publish.serializers import ProductsSerializer
from publish.models import Product

class ProductActions(generics.GenericAPIView):

    """Endpoint for Product CRUD"""

    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        
        if self.kwargs.get('pk'):

            try:

                product = self.queryset.get(pk=self.kwargs.get('pk'))

                serializer = self.get_serializer(product)

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Product.DoesNotExist:

                return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        product_list = self.queryset.all()

        serializer = self.get_serializer(product_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
            

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        errors = serializer.errors

        formatted_errors = {}

        for field, error in errors.items():

            formatted_errors[field] = error[0]

        return Response({"errors": formatted_errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')

        try:

            product = self.queryset.get(pk=pk)

        except Product.DoesNotExist:

            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(product, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        errors = serializer.errors

        formatted_errors = {}

        for field, error in errors.items():

            formatted_errors[field] = error[0]

        return Response({"errors": formatted_errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')

        try:

            product = self.queryset.get(pk)

        except:

            return Response({"errors": formatted_errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(product, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        formatted_errors = {field: error[0] for field, error in serializer.errors.items()}

        return Response({"errors": formatted_errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')

        try:

            product = self.queryset.get(pk=pk)

        except:

            return Response({"error": "Product does not exist."})

        product.delete()

        return Response({"message": "Product was deleted."}, status=status.HTTP_200_OK)