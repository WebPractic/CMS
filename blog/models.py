from django.db import models


class Category(models.Model):
    """Модель категории"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField('Тег', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель постов"""
    title = models.CharField('Заголовок', max_length=100)
    mini_text = models.TextField('Короткий текст', max_length=100)
    text = models.TextField('Полный текст', max_length=1000)
    created_date = models.DateTimeField("Дата публикации")
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    """Модель постов"""
    text = models.TextField('Полный текст', max_length=500)
    created_date = models.DateTimeField("Дата публикации")
    moderation = models.BooleanField("Опубликовать", default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"