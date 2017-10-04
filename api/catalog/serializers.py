from rest_framework import serializers
from catalog.models import Author


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')
