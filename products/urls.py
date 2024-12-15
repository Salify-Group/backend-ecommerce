from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("test/", test, name="test"),
    path("test-CBV/", CategoryListAPIView.as_view(), name="test-CBV"),
    path("add-category/", CategoryAddAPIView.as_view(), name="add-category"),
    path("all-categories/", CategoryListAPIView.as_view(), name="all-categories"),
    path("upload-image/", UploadImageAPIView.as_view(), name="upload-image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)