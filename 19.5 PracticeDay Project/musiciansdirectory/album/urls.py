from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.AddAlbumClassView.as_view(),name='add_album')
]
