from django.db import models
from django.db.models import permalink

class Post(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	description = models.TextField()
	comments = models.CharField(max_length=255)
	author =  models.ForeignKey('blog.Author')
	category_id = models.ForeignKey('blog.Category')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })

class Author(models.Model):
    fname = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.fname

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Comments(models.Model):
    txt = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.txt

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.name

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
