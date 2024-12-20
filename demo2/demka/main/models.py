from email.policy import default
from tabnanny import verbose
from tkinter.constants import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey


class CustomUser(AbstractUser):
    third_name = models.CharField(verbose_name='Отчество', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=12)

    def __str__(self):
        return self.username


class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.title

class Ticket(models.Model):
    creator = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Создатель заявки',
                                related_name='ticket_creator')
    number = models.CharField(max_length=50, verbose_name='Номер автомобиля', )
    descr = models.TextField(max_length=400, verbose_name='Описание', )
    status = ForeignKey('Status', verbose_name='', related_name='ticket_status', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator} - {self.number} ({self.status})"
