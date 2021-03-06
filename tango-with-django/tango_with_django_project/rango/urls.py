from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'), # '^rango/about/' here is '^about/'
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)