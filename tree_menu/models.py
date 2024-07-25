from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name="Меню")
    name = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name="URL")
    named_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Named URL")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский пункт")

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.name