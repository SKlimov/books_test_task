from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Subscriber, Language
from django.db.models import Count
from .serializers import AuthorDetailSerializer, BookDetailSerializer, \
    SubscriberDetailSerializer, BookListSerializer, LanguageDetailSerializer
from .tasks import send_email_task


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def create(self, request, *args, **kwargs):
        response = super(BookViewSet, self).create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            send_email_task.delay(response.data.get('id'))
            return response
        else:
            return response


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberDetailSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer


class BooksSearchViewSet(viewsets.GenericViewSet):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

    @action(detail=False, methods=['get'], url_name='search', url_path='search')
    def search(self, request, *args, **kwargs):
        authors_count = int(request.query_params.get('authors_count', 0))
        books = self.queryset.annotate(count=Count('authors')).filter(count=authors_count)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

