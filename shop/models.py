from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
# from ckeditor.fields import RichTextEditor


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=200, decimal_places=20)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    brand_choices = [
       ('apple','apple'),
        ('samsung','samsung'),
    ]
    brand = models.CharField(max_length=30,null=True, blank=True,choices=brand_choices)
    short_description = models.TextField(blank=True)

    color_choices = [
        ('black', 'black'),
    ]
    colors = models.CharField(max_length=30, null=True,
                              blank=True, choices=color_choices)
    
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    in_stock = models.BooleanField(default=True)
    product_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField()

    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

