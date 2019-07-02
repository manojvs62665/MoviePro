from django.contrib import admin
from django.conf.urls import url
from curdapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page),
    url(r'^create',views.insert_view),
    url(r'^retrieve',views.retrieve_view),
    url(r'^update',views.update_view),
    url(r'^delete',views.delete_view)
]
