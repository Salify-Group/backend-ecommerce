from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/products/", include("products.urls")),
    # path("api/payments/", include("payments.urls")),
] + debug_toolbar_urls()
