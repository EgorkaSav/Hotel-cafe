from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)



class Room(models.Model):
    room_number = models.CharField(max_length=50, null=True)
    room_type = models.CharField(max_length=50, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    amenities = models.TextField(default='Нет информации')
    image = models.ImageField(upload_to='room_images/', null=True)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    user_name = models.CharField(max_length=100, default='Нет информации')
    contact_info = models.CharField(max_length=100, default='')
    is_paid = models.BooleanField(default=False, verbose_name='Оплата')


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dish_images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class EstablishmentInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100, default='Нет контактной информации')
    opening_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100, default = 'Заголовок')
    plot = models.CharField(max_length=250)
    img = models.ImageField(upload_to='blog_images/', null=True)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Sklad(models.Model):
    prod_name = models.CharField(max_length=100, default = 'Название продукта')
    kol_vo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    edin = models.CharField(max_length=100, default = 'Единицы измерения')
