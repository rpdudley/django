from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  hello.models import LogMessage
from django.conf import settings
from django.conf.urls.static import static


home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)





urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('log_message/', views.log_message, name='log_message'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

