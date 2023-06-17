from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'status']


class BookLendSerializer(serializers.Serializer):
    readerId = serializers.IntegerField() 

    def update(self, instance, validated_data):
        instance.reader_id = validated_data['readerId']
        instance.save()
        return instance

    def create(self, validated_data):
        reader_id = validated_data['readerId'] 

        instance = Book.objects.get(id=self.context['view'].kwargs['bookId'])
        if not instance.status:
            raise serializers.ValidationError("Книга недоступна.")
        instance.status = False
        instance.save()

        return validated_data


class BookReturnSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.reader_id = validated_data['readerId']
        instance.save()
        return instance

    def create(self, validated_data):
        instance = Book.objects.get(id=self.context['view'].kwargs['bookId'])
        if instance.status:
            raise serializers.ValidationError("Книга уже есть в библиотеке.")
        instance.status = True
        instance.save()

        return validated_data

