from django.urls import path, include 
from django.contrib.auth.views import LoginView, LogoutView
from posts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()

from posts.views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like,
    login
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/$', views.login, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    path('',PostListView.as_view(), name='list'),
    path('accounts/', include('allauth.urls')),
  ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)