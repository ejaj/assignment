from django.db import models
from django.utils.translation import gettext_lazy as _
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

