from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField('Название книги', max_length=30)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата')
    

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

