from rest_framework.decorators import api_view, permission_classes as permision
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from .models import *



@permision([AllowAny])
@api_view(["GET", "POST"])
def test(request):
    if request.method == "GET":
        data = MainCategorySerializer(MainCategory.objects.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = SubCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryListAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MainCategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = MainCategory.objects.all()
        return queryset


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
        queryset = UploadImage.objects.all()
        return queryset

