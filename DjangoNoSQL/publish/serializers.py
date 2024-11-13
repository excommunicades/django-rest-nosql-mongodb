from rest_framework import serializers

from publish.models import Product

class ProductsSerializer(serializers.ModelSerializer):

    """Serialize data to json"""

    class Meta:

        model = Product

        fields = [
            'pk',
            'title',
            'price',
            'description',
        ]