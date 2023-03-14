from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.OneToOneField(
        'Attachment', related_name='category',
        on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=25)
    image = models.OneToOneField(
        'Attachment', related_name='sub_category',
        on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=8)
    image = models.OneToOneField(
        'Attachment', related_name='collection',
        on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    to_date = models.DateTimeField()
    offer_percentage = models.IntegerField()
    description = models.TextField()
    image = models.OneToOneField('Attachment', related_name='offer',
                                 on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="offers"
    )
    sub_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="offers"
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    feature_description = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_showcase = models.BooleanField(default=False)
    images = models.OneToOneField('ImageAlbum', related_name='products',
                                  on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, related_name="products", on_delete=models.SET_NULL,
        null=True)
    collection = models.ForeignKey(
        Collection, null=True, blank=True, related_name="products",
        on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    SIZE_TYPE = [
        ("small", "SMALL"),
        ("medium", "MEDIUM"),
        ("large", "LARGE"),
        ("free_size", "FREE_SIZE"),
    ]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_inventory"
    )
    size = models.CharField(max_length=10, choices=SIZE_TYPE)
    quantity = models.IntegerField(default=1)
    size_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
