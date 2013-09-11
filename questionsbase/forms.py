# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from models import Question, Alternative, Template


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Primeiro Nome'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Último Nome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Endereço de email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmação de Senha'})


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})


class SearchForm(forms.Form):
    CHOICES = ((u'Questão', u'Questão'),
               ('Curso', 'Curso'),
               ('Disciplina', 'Disciplina'),
               ('Assunto', 'Assunto'))

    search_bar = forms.CharField()
    category = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search_bar'].widget.attrs.update({'class': 'form-control', 'placeholder': 'O que procura?'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})


class AnswerForm(forms.Form):
    def __init__(self, alternatives, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['alternatives'] = forms.ChoiceField(choices=[(alternative.pk, alternative.text) for alternative in alternatives], widget=forms.RadioSelect())


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'course', 'theme', 'subjects',)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição da Questão'})
        self.fields['course'].widget.attrs.update({'class': 'form-control'})
        self.fields['theme'].widget.attrs.update({'class': 'form-control'})
        self.fields['subjects'].widget.attrs.update({'class': 'form-control'})


class AlternativeForm(forms.ModelForm):
    class Meta:
        model = Alternative
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(AlternativeForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição da Alternativa'})


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ('alternative',)

    def __init__(self, question, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        self.fields['alternative'].widget.attrs.update({'class': 'form-control'})
        self.fields['alternative'].label = 'Alternativa Correta'
        self.fields['alternative'].queryset = Alternative.objects.filter(question=question)