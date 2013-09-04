# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin

from models import Question, Alternative, Template, Answer, Course, Theme, Subjects


class AlternativeInline(admin.StackedInline):
    model = Alternative
    can_delete = True
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = ('text', 'course', 'theme', 'subjects', 'status',)
    list_display = ('text', 'course', 'theme', 'status',)
    list_filter = ('status',)
    inlines = [AlternativeInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Question, QuestionAdmin)


class TemplateAdmin(admin.ModelAdmin):
    fields = ('question', 'alternative',)
    list_display = ('question', 'alternative',)

admin.site.register(Template, TemplateAdmin)


class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'alternative',)
    list_display = ('user', 'question', 'alternative', 'date',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Answer, AnswerAdmin)

class CourseAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(Course, CourseAdmin)


class ThemeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(Theme, ThemeAdmin)


class SubjectsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(Subjects, SubjectsAdmin)