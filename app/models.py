from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=52)
    author_bio = models.TextField()
    author_avatar = models.ImageField(upload_to='media/author_avatar')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class News(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=123)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/news_image')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title



