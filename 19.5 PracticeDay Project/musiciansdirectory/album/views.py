from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView
# Class based CrateView 
class AddAlbumClassView(CreateView):
    model = models.album_model
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        form.instance.album = self.request.user
        return super().form_valid(form)
    