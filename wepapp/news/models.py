from django.db import models

# Create your models here.
class Newspaper(models.Model):
    name = models.CharField('Название газеты',max_length=50)
    information = models.CharField('Информационная направленность',max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/newspaper/{self.id}'
    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/article/{self.id}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

