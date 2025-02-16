from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='названия')
    content = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/',blank=True, null=True, verbose_name='изображение')


    def __str__(self):
        return self.title
