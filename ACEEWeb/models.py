# coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=True, verbose_name=u'标签名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.tag_name

    class Meta:
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'标签'

class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'作者'


class Article(models.Model):
    caption = models.CharField(max_length=50, verbose_name=u'标题')
    author = models.ForeignKey(Author, verbose_name=u'作者')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    content = models.TextField(verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'文章'