from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("add-category/", CategoryAddAPIView.as_view(), name="add-category"),
    path("all-categories/", CategoryListAPIView.as_view(), name="all-categories"),
    path("upload-image/", UploadImageAPIView.as_view(), name="upload-image"),
    path("features/", FeatureAPIView.as_view(), name="features"),
    path("colors/", ColorAPIView.as_view(), name="colors"),
    path("sizes/", SizeAPIView.as_view(), name="sizes"),
    path("volumes/", VolumeAPIView.as_view(), name="volumes"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path("product-variaty/", ProductVariationAPIView.as_view(), name="product-variation"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)