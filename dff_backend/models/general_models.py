from django.db import models


class ImageAlbum(models.Model):

    def default(self):
        return self.images.filter(default=True).first()


class Attachment(models.Model):
    album = models.ForeignKey('ImageAlbum', related_name='images',
                              on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=200)
    url = models.TextField()
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DashBoard(models.Model):
    login_image = models.OneToOneField(
        'Attachment', related_name='dash_board_login_image',
        on_delete=models.SET_NULL, null=True)
    home_page_image = models.OneToOneField(
        'Attachment', related_name='dash_board_home_page_image',
        on_delete=models.SET_NULL, null=True)
    slider_images = models.OneToOneField(
        'ImageAlbum', related_name='dashboard',
        on_delete=models.SET_NULL, null=True)


class Country(models.Model):
    name = models.CharField(max_length=100)


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, related_name='states', on_delete=models.CASCADE)
