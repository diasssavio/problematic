# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.


class Question(models.Model):
    text = models.TextField(verbose_name=u'Questão')
    datepost = models.DateTimeField(auto_now_add=True, verbose_name='Data de Postagem')

    user = models.ForeignKey(User, verbose_name=u'Usuário')
    course = models.ForeignKey('Course', verbose_name='Curso')
    theme = models.ForeignKey('Theme', verbose_name='Disciplina')
    subjects = models.ManyToManyField('Subjects', verbose_name='Assuntos')

    #right = models.OneToOneField('Alternative', verbose_name='Alternativa Correta')

    view = models.PositiveIntegerField(default=0, verbose_name=u'Visualizações')
    status = models.BooleanField(default=False, verbose_name='Status')

    def __unicode__(self):
        return '%s' % self.text

    class Meta:
        verbose_name = u'Questão'
        verbose_name_plural = u'Questões'


class Alternative(models.Model):
    text = models.TextField(verbose_name='Alternativa')

    question = models.ForeignKey(Question, verbose_name=u'Questão')

    def __unicode__(self):
        return '%s' % self.text

    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

class Template(models.Model):
    question = models.OneToOneField(Question, verbose_name=u'Questão')
    alternative = models.OneToOneField(Alternative, verbose_name='Alternativa')

    def __unicode__(self):
        return '%s' % self.alternative

    class Meta:
        verbose_name = 'Gabarito'
        verbose_name_plural = 'Gabaritos'


class Answer(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Resposta')

    user = models.ForeignKey(User, verbose_name=u'Usuário')
    question = models.OneToOneField(Question, verbose_name=u'Questão')
    alternative = models.OneToOneField(Alternative, verbose_name='Alternativa')

    def __unicode__(self):
        return '%s' % self.alternative

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Nome')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Theme(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Nome')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'


class Subjects(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Nome')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'