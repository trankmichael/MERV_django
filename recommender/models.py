from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
	word = models.CharField(max_length=35)
	slug = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add=False)

class Task(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, related_name='tasks',blank=True)

	class Meta:
		ordering = ['-created']
	def __unicode__(self):
		return u'%s' % self.title
	def get_absolute_url(self):
		return reverse('recommender.views.task', args=[self.slug])

