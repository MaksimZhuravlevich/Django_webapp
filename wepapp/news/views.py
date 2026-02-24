from django.shortcuts import render , redirect
from .models import Newspaper , Articles
from .forms import NewspaperForm , ArticlesForm
from django.views.generic import DetailView , UpdateView , DeleteView


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news'
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDetailView(DetailView):
    model= Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewspaperDetailView(DetailView):
    model=Newspaper
    template_name = 'news/newspaper_detail_view.html'
    context_object_name = 'newspaper'


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