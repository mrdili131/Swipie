from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('upload-content/',views.upload,name='upload'),
    path('image-view/<str:id>',views.image_view,name='image_view'),
    path('download/<str:file_name>/',views.download,name='download')
]