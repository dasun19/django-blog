from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,PostDeleteView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),

    path('', PostListView.as_view() , name = 'home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'blog-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'blog-new'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'blog-delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)