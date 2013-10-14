#_*_coding:utf-8_*_ 

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

class ProUser(models.Model):
	user = models.OneToOneField(User, related_name=u'prouser')
	headimg = models.CharField(max_length=200,blank=True, null=True, verbose_name=u'headimg')
	attention = models.ManyToManyField(User, related_name=u'attention')

	def __unicode__(self):
		return self.user.username

class Letter(models.Model):
	letter = models.CharField(max_length=400, verbose_name=u'letter')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'xiexinshijian')
	invite_id = models.IntegerField(blank=True, null=True, verbose_name=r'yaoqing')
	read = models.BooleanField(default=False, verbose_name=u'read')
	post_user = models.ForeignKey(User, related_name=u'post')
	recv_user = models.ForeignKey(User, related_name=u'recv')

class Group(models.Model):
	groupname = models.CharField(max_length=50, unique=True, verbose_name=u'groupname')
	master = models.ForeignKey(User)
	isPublic = models.BooleanField(default=False, verbose_name=u'xiaozuzhuangtai')
	# slug = models.SlugField(unique=True, verbose_name=u'slug')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'createtime')
	description = models.TextField(verbose_name=u'description')

	members = models.ManyToManyField(User, related_name=u'members')

	@permalink
	def get_absolute_url(self):
		return ('blog_group',None, {'slug': self.slug})

	def __unicode__(self):
		return self.groupname