from rest_framework import serializers
from .models import Author, Book, Subscriber, Language


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    # тут неплохо бы возвращать не id авторов, а их имена
    # как то так:
    # author_names = serializers.SerializerMethodField()
    # def get_owner_name(self, obj):
    #   найти авторов и вернуть список имен
    class Meta:
        model = Book
        fields = '__all__'
        # fields = (title, language, publish date, authors)


class SubscriberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class LanguageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
