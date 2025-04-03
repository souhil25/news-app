from django.contrib import admin
from django.urls import path, include 

#removal support for logging out via GET requests
#The ORDER is important in here//

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')), #Views
    path('articles/', include('articles.urls')), # new
    path('', include('pages.urls')), # new
]