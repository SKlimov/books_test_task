from celery import shared_task
from django.core.mail import send_mail
from .models import Book, Subscriber


@shared_task
def send_email_task(book_id):
    subscribers = Subscriber.objects.all()
    book = Book.objects.get(id=book_id)

    for subscriber in subscribers:
        # from_email = None means that will be used DEFAULT_FROM_EMAIL
        authors = ""
        for author in book.authors.all():
            authors += "%s %s" % (author.first_name, author.last_name)
            authors += ' '
        send_mail(
            '%s добавлена в  библиотеку' % book.title,
            'Здравствуйте. У нас есть хорошие новости для Вас: %s (%s) добавлена в библиотеку' % (book.title, authors),
            None, [subscriber.email], fail_silently=False)
