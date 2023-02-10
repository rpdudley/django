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
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log" ),
    path("polls/", views.polls, name="polls"),
    path("questions/", views.questions, name="questions"),
    path('create/', views.create, name='create'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

