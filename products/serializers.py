from rest_framework import serializers
from .models import *





class CategoryShowSerializer(serializers.ModelSerializer):
    main_category = serializers.StringRelatedField(many=False, read_only=True)
    sub_category = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Category
        fields = [
            "main_category",
            "sub_category",
        ]

class CategoryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = [
            "id",
            "name",
            "alt",
            "image",
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    sub_name = serializers.CharField(source='sub_category.sub_name', read_only=True)
    sub_slug = serializers.CharField(source='sub_category.sub_slug', read_only=True)
    class Meta:
        model = SubCategory
        fields = [
            "id",
            "sub_name",
            "sub_slug",
        ]


class MainCategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = MainCategory
        fields = [
            "id",
            "main_name",
            "main_slug",
            "sub_categories",
        ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariety
        fields = '__all__'
