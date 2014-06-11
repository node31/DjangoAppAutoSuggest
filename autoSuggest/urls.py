from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'autoSuggest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^author_book/',include('author_book.urls')),	
    url(r'^admin/', include(admin.site.urls)),
)
