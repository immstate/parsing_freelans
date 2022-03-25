from http.client import responses
from tabnanny import verbose
from turtle import title
from urllib import response
from django import views
from django.db import models


class Job(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_lenght=250, verbose_name='заказ')
    price = models.CharField(max_lenght=50, verbose_name='цена')
    views = models.CharField(max_lenght=50, verbose_name='просмотры')
    responses = models.CharField(max_lenght=50, verbose_name='отлики')
    time = models.CharField(max_lenght=50, verbose_name='время')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'