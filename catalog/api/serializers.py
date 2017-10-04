from rest_framework import serializers
from catalog.models import Author


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField(required=False, allow_blank=True)
    date_of_death = serializers.DateField(required=False, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Author` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.date_of_death = validated_data.get('date_of_death', instance.date_of_death)
        instance.save()
        return instance
