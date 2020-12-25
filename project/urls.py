
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('calender/', include('calendarapp.urls'))
]
