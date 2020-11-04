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
    book_isbn = models.CharField(max_length=20,default=" ")

    def __str__(self):
        return self.book_name + " By " + self.author_name

    
class Order(models.Model):

    ORDER_STATUS_CHOICES =(
        ("PEN", "Pending"),
        ("ACP", "Accepted"),
        ("SHP", "Shipped"),
        ("OFD", "Out For Delivery"),
        ("DEL", "Delivered"),
        ("CAN", "Cancelled"),
    )

    status = models.CharField(choices=ORDER_STATUS_CHOICES,default="PEN",max_length=30)
    items_json = models.CharField(max_length=5000)
    user_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="Abc")
    order_total = models.CharField(max_length=100)
    order_placed_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user_name + "'s Order Placed On " + str(self.order_placed_date)