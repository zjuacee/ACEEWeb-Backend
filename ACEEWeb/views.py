from django.shortcuts import render
from django.http import Http404
from ACEEWeb.models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, "ACEEWeb/article_list.html", {'articles':articles, })

def article_show(request, id=''):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, "ACEEWeb/article_show.html", {'article':article })