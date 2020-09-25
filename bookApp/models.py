from django.db import models


class Book(models.Model):
    CATEGORY_CHOICES = (
        ("CRM", "Crime/Mystery"),
        ("ADN", "Adventure"),
        ("EDU", "Educational"),
        ("MOT", "Motivational"),
        ("BGR", "Biography"),
        ("FIC", "Fiction"),
    )
    # book_id = models.AutoField()
    book_name = models.CharField(max_length=100, blank=False, default=" ")
    book_price = models.IntegerField(default=None)
    author_name = models.CharField(max_length=100, blank=False, default=" ")
    book_description = models.TextField(max_length=500, blank=False, null=True)
    available_stock = models.IntegerField(default=0, blank=True, null=False)
    book_frontpage = models.ImageField(default='default.jpg', upload_to='book_frontpages')
    book_category = models.CharField(choices=CATEGORY_CHOICES, default="FIC", max_length=20)

    def __str__(self):
        return self.book_name + " By " + self.author_name


