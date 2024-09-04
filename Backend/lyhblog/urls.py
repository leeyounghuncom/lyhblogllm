from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from docs.views import LyhDocDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", include("docs.urls")),
    path('<slug:doc_name>/', LyhDocDetailAPIView.as_view(), name='doc-detail'),  # 'slug'를 'doc_name'으로 변경

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]