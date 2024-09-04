from rest_framework import generics
from .models import LyhDoc
from .serializers import LyhDocSerializer

class LyhDocListCreateAPIView(generics.ListCreateAPIView):
    queryset = LyhDoc.objects.all()
    serializer_class = LyhDocSerializer

class LyhDocEditDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LyhDoc.objects.all()
    serializer_class = LyhDocSerializer
    lookup_field = 'pk'  # Primary key를 사용해 문서를 식별


class LyhDocDetailAPIView(generics.RetrieveAPIView):
    queryset = LyhDoc.objects.all()
    serializer_class = LyhDocSerializer
    lookup_field = 'doc_name'  # 'slug'를 'doc_name'으로 변경
