from rest_framework import serializers
from .models import LyhDoc

class LyhDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = LyhDoc
        # doc_name 자동 생성
        fields = ['id', 'doc_title', 'doc_content', 'doc_date', 'doc_name']  # Only serialize id and doc_title
