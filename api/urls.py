from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import AuthorViewSet, BookViewSet, SubscriberViewSet, BooksSearchViewSet, LanguageViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'', BooksSearchViewSet, basename='search')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'book', BookViewSet, basename='book')
router.register(r'subscriber', SubscriberViewSet, basename='subscriber')
router.register(r'Language', LanguageViewSet, basename='language')

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
