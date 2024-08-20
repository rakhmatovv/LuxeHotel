from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=160, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    img = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, max_length=160, null=True, verbose_name='SLUG')
    description = models.TextField(max_length=100, default='Description')
    beds = models.IntegerField()
    capacity = models.IntegerField()
    status = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds  for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField(blank=True)
    check_out = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
    

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Massage', max_length=5000)
    parent = models.ForeignKey('self', User, blank=True, null=True)
    room = models.ForeignKey(Room, verbose_name='Room', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.room}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'


class Review(models.Model):
    review = models.TextField('Review', null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'