from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from user.models import User


class Currency(models.Model):
    name = models.CharField(_('Currency Name'), max_length=250, unique=True)
    value = models.FloatField(_('Value'), max_length=100)

    created = models.ForeignKey(User, verbose_name=_('Created User'), related_name='currency_created',
                                on_delete=models.SET_NULL, null=True, blank=True)
    updated = models.ForeignKey(User, verbose_name=_('Updated User'), related_name='currency_updated',
                                on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        db_table = 'currencies'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='content')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Like(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Post(models.Model):
    title = models.CharField(max_length=50)
    likes = GenericRelation(Like)


class Page(models.Model):
    title = models.CharField(max_length=50)
    likes = GenericRelation(Like)


class Comment(models.Model):
    title = models.CharField(max_length=50)
    likes = GenericRelation(Like)
