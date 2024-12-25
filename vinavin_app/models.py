from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class events(models.Model):
    title = models.CharField("Название события", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите Категорию")
    price = models.CharField("Цена", max_length=150)
    date = models.CharField("Дата и время", max_length=200)
    address = models.CharField("Адрес", max_length=400)
    description = models.TextField("Описание")
    dress_code = models.CharField("Требования к одежде", max_length=600)
    created_at = models.DateTimeField("Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Название события"
        verbose_name_plural = "Название события"

    def __str__(self):
        return self.title
