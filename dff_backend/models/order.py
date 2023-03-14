from django.db import models


class CartItems(models.Model):
    customer = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name="cart_items")
    product_inventory = models.ForeignKey(
        'ProductInventory', on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    PAYMENT_STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ]

    ref_number = models.CharField(max_length=50)
    customer = models.ForeignKey(
        'User', on_delete=models.PROTECT, related_name="orders")
    address = models.TextField()
    payment_status = models.CharField(
        max_length=25, choices=PAYMENT_STATUS_CHOICE)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    """ quantity * selling cost = chargeable amount """

    ORDER_STATUS = [
        ("PENDING", "Pending"),
        ("PLACED", "Placed"),
        ("CONFIRMED", "Confirmed"),
        ("DELIVERED", "Delivered"),
        ("CANCELED", "Canceled"),
    ]

    order = models.ForeignKey(
        'Order', max_length=8, related_name="order_items",
        on_delete=models.CASCADE)
    product_inventory = models.ForeignKey(
        'ProductInventory', max_length=25, related_name="order_items",
        on_delete=models.PROTECT)
    selling_cost = models.DecimalField(max_digits=20, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=12, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    order_id = models.CharField(max_length=25)
    payment_order_id = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
