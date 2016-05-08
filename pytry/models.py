from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


class Comment(models.Model):
    # user = models.ForeignKey(User)
    comments = models.TextField()
    # parent = models.ForeignKey("self", related_name='children', null=True)
    left = models.IntegerField(default=0, db_index=True)
    right = models.IntegerField(default=0, db_index=True)

    def get_init_absolute_url(self):
        return reverse("comment_detail")