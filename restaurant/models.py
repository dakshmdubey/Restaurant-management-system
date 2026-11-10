from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    table = models.ForeignKey(
        'Table',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    order_date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.customer_name} - {self.food_item.name}"

    @property
    def total_price(self):
        return self.quantity * self.food_item.price


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return f"Table {self.table_number}"
