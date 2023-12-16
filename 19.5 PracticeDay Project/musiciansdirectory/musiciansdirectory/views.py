from django.shortcuts import render,redirect
from album.models import album_model
from musician.models import musician_model
from album.forms import AlbumForm
from musician.forms import MusicainForm
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Class based ListView
class HomeClassView(generic.ListView):
    model = album_model
    template_name = 'home.html'
    context_object_name = 'data'

# Class based UpdateView
@method_decorator(login_required, name= 'dispatch')
class EditPostView(generic.UpdateView):
    model = album_model
    form_class = AlbumForm
    template_name = 'edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


@method_decorator(login_required, name= 'dispatch')
class MusicianClassView(generic.UpdateView):
    model = musician_model
    form_class = MusicainForm
    template_name = 'edit.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('homepage')



# Class based DeleteView
@method_decorator(login_required, name= 'dispatch')
class DeletePostView(generic.DeleteView):
    model = album_model
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
