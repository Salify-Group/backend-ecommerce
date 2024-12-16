from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from .models import *



class CategoryListAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MainCategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return MainCategory.objects.all()


class CategoryAddAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategoryAddSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class UploadImageAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UploadImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return UploadImage.objects.all()


class FeatureAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeatureSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Feature.objects.all()


class ColorAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ColorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Color.objects.all()


class SizeAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SizeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Size.objects.all()


class VolumeAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VolumeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def ger(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Volume.objects.all()


class ProductAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Product.objects.all()


class ProductVariationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductVarietySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return ProductVariety.objects.all()
