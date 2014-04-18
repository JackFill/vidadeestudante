#-*-coding:utf-8 -*-


#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/
from django.forms import ModelForm
from django import forms
from models import Artigo

#create the form class to add articles
		
class FormAddArtigo(forms.Form):
	titulo = forms.CharField(max_length=100)
	conteudo = forms.CharField(widget=forms.Textarea())
	publicacao = forms.DateTimeField(widget=forms.DateTimeInput(format='%d/%m/%y'))