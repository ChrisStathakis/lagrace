from django.shortcuts import render

from .models import Category, Banner


def homepage(request):
    context = dict()
    context['categories'] = Category.objects.filter(active=True, parent__isnull=True)
    banners = Banner.objects.filter(active=True)
    context['main_banners'] = banners.filter(category='a')
    context['small_banners'] = banners.filter(category='b')[:4]
    context['banner'] = banners.filter(category='c').first() if banners.filter(category='c').exists() else None
    return render(request, 'index.html', context)
