from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('shows/new', views.new),
    path('shows', views.shows),
    path('add', views.add),
    path('shows/<int:num>/edit',views.edit),
    path('editshow', views.editshow),
    path('shows/<int:num>',views.display),
    path('shows/<int:num>/destroy', views.destroy)
]