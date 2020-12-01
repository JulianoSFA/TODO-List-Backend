from rest_framework import serializers 
from ListApp.models import ListItem

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = (
            'id',
            'status',
            'description',
            'dateTime',
        )