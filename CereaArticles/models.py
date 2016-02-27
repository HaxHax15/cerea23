from django.db import models
from CereaUser.models import User

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name='Статья'
    )
    article_category = models.ForeignKey(
        ArticleCategory,
        blank=False,
        null=False,
        related_name='+',
        verbose_name='Категория статьи'
    )
    article_text = models.TextField(
        max_length=1000,
        blank=True,
        null=False,
        verbose_name='Текст статьи'
    )
    article_meta_keywords = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='Ключевые слова'
    )
    article_meta_description = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    article_author = models.ForeignKey(
        User,
        blank=False,
        related_name='+'
    )

    def __str__(self):
        return self.article_title


class ArticleCategory(models.Model):
    category_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name='Категория'
    )