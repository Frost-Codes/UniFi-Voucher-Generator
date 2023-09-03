from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home),
    path('twenty_four', views.twenty_four, name='twenty_four'),
    path('seventy_two', views.seventy_two, name='seventy_two'),
    path('ninety_six', views.ninety_six, name='ninety_six'),
    path('search', views.search, name='search'),


    path('markused/', views.mark_used),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
