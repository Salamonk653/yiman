from django.urls import path

from gallery import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/ajax-upload/', views.AjaxPhotoUploadView.as_view(), name='ajax_photo_upload_view'),
]
