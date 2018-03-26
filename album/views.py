from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def base(request):
    return render(request, 'base.html')

def first_view( request ):
    return HttpResponse( 'Esta es mi primera vista!' )

def category(request):
    category_list = Category.objects.all()
    context = { 'object_list':category_list }
    return render( request, 'album/category_list.html', context )

def category_detail(request, category_id):
    category = Category.objects.get( id=category_id )
    context = { 'object':category }
    return render( request, 'album/category_detail.html', context )

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class PhotoListView(ListView):
    model = Photo

class PhotoDetailView(DetailView):
    model = Photo

class PhotoCreate(CreateView):
    model = Photo

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['category', 'title', 'photo', 'favorite', 'comment']

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')
