from django.shortcuts import render , redirect
from .models import Newspaper
from .forms import NewspaperForm
from .models import  Articles
from .forms import ArticlesForm
# Create your views here.
def news_home(request):

    news=Articles.objects.order_by('date')[:10]
    newspaper_news=Newspaper.objects.order_by('name')[:10]

    return render(request, 'news/news_home.html',{'news':news,'newspaper_news':newspaper_news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error='Форма была неверной'


    form = ArticlesForm
    data={
        'form':form,
        'error':error
    }
    return render(request, 'news/create.html', data)

def news_create(request):
    error = ''
    if request.method == 'POST':
        form = NewspaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    form=NewspaperForm
    data={
        'form':form,
        'error':error
    }

    return render(request,'news/news_create.html',data)