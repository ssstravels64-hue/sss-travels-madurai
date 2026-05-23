from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)

    distance = models.IntegerField()

    car_type = models.CharField(max_length=100)

    travel_date = models.DateField()

    amount = models.IntegerField(default=0)

    payment_status = models.CharField(
        max_length=50,
        default="Pending"
    )

    def __str__(self):
        return self.name

class CustomerAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Rejected','Rejected'),
        ('Cancelled','Cancelled'),
        ('Finished','Finished')
    ]


    PAYMENT_CHOICES = [
        ('Pending','Pending'),
        ('Paid','Paid')
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    pickup = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)
    car_type = models.CharField(max_length=100)
    travel_date = models.DateField()
    distance = models.FloatField()
    amount = models.FloatField()

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='Pending'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name