# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from .lists import LISTS


class DraftEmail(models.Model):
    """A draft e-mail announcement to users."""
    list_name = models.CharField(max_length=32)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    edited = models.DateTimeField(auto_now=True, editable=False)
    sent = models.DateTimeField(null=True, editable=False)

    STATUS_DRAFT = 1
    STATUS_SENDING = 2
    STATUS_SENT = 3

    status = models.IntegerField(
        choices=[
            (STATUS_DRAFT, 'Draft'),
            (STATUS_SENDING, 'Sending'),
            (STATUS_SENT, 'Sent'),
        ], editable=False,
        default=STATUS_DRAFT,
    )

    @property
    def list_title(self):
        """Get the title of the recipients list."""
        name, list_func = LISTS[self.list_name]
        return name

    @property
    def recipients(self):
        """Get a QuerySet of recipient EmailAddresses."""
        name, list_func = LISTS[self.list_name]
        return list_func()

    def __str__(self):
        return '<{self.list_name}: "{self.subject}">'.format(self=self)

    def get_absolute_url(self):
        """Get a URL to preview the e-mail."""
        return reverse('preview-email', args=(self.id,))