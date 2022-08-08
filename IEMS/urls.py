from django.contrib import admin
from django.urls import path, include
from iems_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iems_api/', views.LCSEnchroachmentAPI.as_view()),
    path('iems_api/<int:pk>/', views.RUDEnchroachmentAPI.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
    