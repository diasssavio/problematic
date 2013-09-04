# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from forms import UserForm, AuthForm, SearchForm
from models import Question, Course, Theme, Subjects

# Create your views here.

def index(request):
    saved = False
    error_login = False

    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        auth = AuthForm(data=request.POST)
        searchForm = SearchForm(data=request.POST)
        if userForm.is_valid():
            userForm.save()
            saved = True
            
        if auth.is_valid():
            user = authenticate(username=auth.cleaned_data['username'], password=auth.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
            else:
                error_login = True

        if searchForm.is_valid():
            if searchForm.cleaned_data['category'] == u'Questão':
                return HttpResponseRedirect('/qb/search/question/' + searchForm.cleaned_data['search_bar'])
            elif searchForm.cleaned_data['category'] == 'Curso':
                return HttpResponseRedirect('/qb/search/course/' + searchForm.cleaned_data['search_bar'])
            elif searchForm.cleaned_data['category'] == 'Disciplina':
                return HttpResponseRedirect('/qb/search/theme/' + searchForm.cleaned_data['search_bar'])
            elif searchForm.cleaned_data['category'] == 'Assunto':
                return HttpResponseRedirect('/qb/search/subjects/' + searchForm.cleaned_data['search_bar'])
    else:
        userForm = UserForm()
        auth = AuthForm()
        searchForm = SearchForm()

    recent_questions = Question.objects.filter(status=True).order_by('-datepost')[:10]
    viewed_questions = Question.objects.filter(status=True).order_by('-view')[:10]

    data = {'userForm': userForm, 'authForm': auth, 'searchForm': searchForm, 'saved': saved,
            'error_login': error_login, 'recent_questions': recent_questions, 'viewed_questions': viewed_questions}

    return render_to_response('problematic/index.html', data, context_instance=RequestContext(request))


def question(request, id):
    question = get_object_or_404(Question, pk=id)
    question.view += 1
    question.save()

    return render_to_response('questionsbase/question.html', {'question': question}, context_instance=RequestContext(request))


def listCourse(request):
    courses = Course.objects.all()

    return render_to_response('questionsbase/courses.html', {'courses': courses}, context_instance=RequestContext(request))


def listTheme(request):
    themes = Theme.objects.all()

    return render_to_response('questionsbase/themes.html', {'themes': themes}, context_instance=RequestContext(request))


def listSubjects(request):
    subjects = Subjects.objects.all()

    return render_to_response('questionsbase/subjects.html', {'subjects': subjects}, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def search(request, choice, word):
    is_question = False
    choice_name = None
    data_row = None
    if choice == 'question':
        data_row = Question.objects.filter(text__contains=word)
        choice_name = u'Questões'
        is_question = True
    elif choice == 'course':
        data_row = Course.objects.filter(name__contains=word)
        choice_name = 'Cursos'
    elif choice == 'theme':
        data_row = Theme.objects.filter(name__contains=word)
        choice_name = 'Disciplinas'
    elif choice == 'subjects':
        data_row = Subjects.objects.filter(name__contains=word)
        choice_name = 'Assuntos'

    return render_to_response('questionsbase/search.html', {'choice': choice, 'choice_name': choice_name, 'is_question': is_question,
                              'data_row': data_row}, context_instance=RequestContext(request))