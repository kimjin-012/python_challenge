from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('authors', views.authors),
    path('addauthors', views.addauthors),
    path('authors/<number>', views.authorinfo),
    path('connectauthor', views.connectauthor),
    path('addbook', views.addbook),
    path('books/<number>', views.books),
    path('connectbook', views.connectbook),
]