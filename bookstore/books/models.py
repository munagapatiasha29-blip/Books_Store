from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.book.title