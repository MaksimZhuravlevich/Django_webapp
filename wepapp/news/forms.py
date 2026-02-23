from .models import Articles
from .models import Newspaper
from django.forms import ModelForm, TextInput , DateTimeInput , Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields = ['title','anons','full_text','date']

        widgets = {
            'title':TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Название статьи'
            }),
            'anons':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс Статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст Статьи'
            })
        }

class NewspaperForm(ModelForm):
    class Meta:
        model=Newspaper
        fields=['name','information']
        widgets={
            'name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название Газесты'
            }),
            'information':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Информационная направленность'
            })
        }