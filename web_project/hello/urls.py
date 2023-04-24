from django.urls import path
from hello import views, api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  hello.models import LogMessage
from django.conf import settings
from django.conf.urls.static import static
from .api import LogMessageListCreateAPIView









urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('log_message/', views.log_message, name='log_message'),
    path('contact/', views.contact, name='contact'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('api/log_messages/', LogMessageListCreateAPIView.as_view(), name='log_messages_api'),
    path('api/log_messages/', api.LogMessageListCreateAPIView.as_view(), name='log_messages_api'),
    path('api/log_messages/<int:pk>/', api.LogMessageRetrieveUpdateDestroyAPIView.as_view(), name='log_message_detail_api'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

