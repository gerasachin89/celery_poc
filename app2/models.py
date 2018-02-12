from django.db import models
from datetime import datetime, timedelta
#from sorl.thumbnail import ImageField
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static/img', default="")

class detail(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE, related_name='det')
    detail = models.CharField(max_length=30, default="detail")

class Office(models.Model):
    person = models.ForeignKey('Person',on_delete=models.CASCADE)
    office_name = models.CharField(max_length=30)
    doj = models.DateTimeField(default=datetime.now)

class Mig(models.Model):
    person = models.ForeignKey('Person',on_delete=models.CASCADE)
    mig_name = models.CharField(max_length=30, default="detail")

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class Bike(models.Model):
    COLOR_OPTIONS = (('yellow', 'Yellow'), ('red', 'Red'), ('black', 'Black'))

    color = models.CharField(max_length=255, null=True, blank=True,
                             choices=COLOR_OPTIONS)
    size = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
