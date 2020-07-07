import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Subscriber, Language, Author, Book
from .serializers import SubscriberDetailSerializer


# initialize the APIClient app
client = Client()


# model tests example
class SubscribersTest(TestCase):
    def setUp(self):
        self.subscriber = Subscriber.objects.create(
            name='Project', last_name="Project", email='project@project.com')
        Subscriber.objects.create(
            name='Project 2', last_name="Project", email='project2@project.com')
        Subscriber.objects.create(
            name='Project 3', last_name="Project", email='project3@project.com')
        Subscriber.objects.create(
            name='Project 4', last_name="Project", email='project4@project.com')

        self.update_payload_valid = {
                "name": "Иван",
                "middle_name": "Иваныч",
                "last_name": "Иванов",
                "email": "test@test.com"
            }
        self.update_payload_invalid = {
            "name": "",
            "middle_name": "Иваныч",
            "last_name": "Иванов",
            "email": "test@test.com"
        }

    def test_get_valid_single_subscriber(self):
        response = client.get(
            reverse('api:subscriber-detail', kwargs={'pk': self.subscriber.pk}))
        subscriber = Subscriber.objects.get(pk=self.subscriber.pk)
        serializer = SubscriberDetailSerializer(subscriber)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_subscriber(self):
        response = client.get(
            reverse('api:subscriber-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_subscribrer(self):
        response = client.put(
            reverse('api:subscriber-detail', kwargs={'pk': self.subscriber.pk}),
            data=json.dumps(self.update_payload_valid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_subscribrer(self):
        response = client.put(
            reverse('api:subscriber-detail', kwargs={'pk': self.subscriber.pk}),
            data=json.dumps(self.update_payload_invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_subscribers(self):
        # get API response
        response = client.get(reverse('api:subscriber-list'))
        # get data from db
        experiments = Subscriber.objects.all()
        serializer = SubscriberDetailSerializer(experiments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_delete_subscriber(self):
        response = client.delete(
            reverse('api:subscriber-detail', kwargs={'pk': self.subscriber.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_subscriber(self):
        response = client.delete(
            reverse('api:subscriber-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookTest(TestCase):
    def setUp(self):
        self.subscriber = Subscriber.objects.create(
            name='Иван', last_name="Иванов", email='project@project.com')
        self.author = Author.objects.create(first_name='Федор', middle_name='Михайлович', last_name='Достаевский')
        self.language = Language.objects.create(name='Русский', code='rus')

        self.delete_book = Book.objects.create(
            title="Идиот", publish_date="1887-01-01T00:00:00Z", language=self.language)
        self.delete_book.authors.set([self.author])
        self.payload = {
            "title": "Преступление и наказание",
            "publish_date": "1866-01-01T00:00:00Z",
            "language": self.language.pk,
            "authors": [
                self.author.pk
            ]
        }

    def test_create_book(self):
        response = client.post(
            reverse('api:book-list'),
            data=self.payload,
            content_type='application/json'
        )
        self.book_pk = response.data.get('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_book(self):
        response = client.delete(
            reverse('api:book-detail', kwargs={'pk': self.delete_book.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
