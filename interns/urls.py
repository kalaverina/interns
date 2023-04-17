from django.contrib import admin
from django.urls import path, include
from interns import views

urlpatterns = [
    path('', views.authorization),
    path('admin/', admin.site.urls),
    path('payments/', views.payments),
    path('account/', views.account),
    path("authorization/", views.authorization),
    path('edit_account/', views.edit_account),
    path("login/", include("django.contrib.auth.urls")),  # new

]
