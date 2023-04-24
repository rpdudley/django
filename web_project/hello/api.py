from rest_framework import generics
from .models import LogMessage
from .serializers import LogMessageSerializer

class LogMessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = LogMessage.objects.all()
    serializer_class = LogMessageSerializer

class LogMessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogMessage.objects.all()
    serializer_class = LogMessageSerializer
