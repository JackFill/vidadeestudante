#-*-coding:utf-8 -*-

from django import forms


class AutorForm(form.Form):
	image = forms.ImageField()
	profissao = models.CharField(max_length=2,widget=forms.select(choices=PF_CHOICES))
	