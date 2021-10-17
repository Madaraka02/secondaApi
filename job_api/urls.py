"""
http://127.0.0.1:8000/posts/ (POST,GET)
http://127.0.0.1:8000/posts/:pk (GET, PUT, DELETE)
its generate similarly for Users the following
http://127.0.0.1:8000/users/ (POST,GET)
http://127.0.0.1:8000/users/:pk (GET, PUT, DELETE)


"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('companyjobs.urls'))
]
