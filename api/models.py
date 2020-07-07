from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "%s %s %s" % (self.first_name,
                             (self.middle_name if self.middle_name is not None else ''),
                             self.last_name)


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, related_name='language')
    publish_date = models.DateTimeField(null=False)
    authors = models.ManyToManyField(Author, related_name='authors')

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=True)
