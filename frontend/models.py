from django.db import models
from django.utils.safestring import mark_safe

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.URLField()

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def childrens(self):
        return self.children.filter(active=True)


class Banner(models.Model):
    CHOICES = (
        ('a', 'Big Banner'),
        ('b', 'Small Banner'),
        ('c', 'Medium Banner')
    )
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='banners/', )
    url = models.URLField()
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.title

    def admin_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50px" height="50px">')
        return 'No Photo'


class Shop(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class ShopPhoto(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops/', )

    class Meta:
        verbose_name_plural = 'ΦΩΤΟΓΡΑΦΙΕΣ ΚΑΤΑΣΤΗΜΑΤΩΝ'

    def __str__(self):
        return f'{self.shop.title}- {self.id}'

    def admin_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50px" height="50px">')
        return 'No Photo'

