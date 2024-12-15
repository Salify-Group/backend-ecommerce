from django.db import models




class MainCategory(models.Model):
    main_name = models.CharField(max_length=30, unique=True)
    main_slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.main_name


class SubCategory(models.Model):
    sub_name = models.CharField(max_length=30, unique=True)
    sub_slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.sub_name


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="sub_categories")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.sub_category.sub_name} < {self.main_category.main_name}"


class UploadImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=64, unique=True)
    alt = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Feature(models.Model):
    key = models.CharField(max_length=35)
    value = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return f"{self.key} | {self.value}"


class Color(models.Model):
    color = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.size


class Volume(models.Model):
    volume = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.volume


class Product(models.Model):
    image = models.ForeignKey(UploadImage, on_delete=models.PROTECT)
    images = models.ManyToManyField(UploadImage, related_name="product_images")
    title = models.CharField(max_length=50)
    meta_title = models.CharField(max_length=50)
    slug = models.SlugField()
    short_description = models.TextField()
    full_description = models.TextField()
    meta_description = models.TextField()
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_DEFAULT, default="دسته بندی نشده")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_DEFAULT, default="دسته بندی نشده", null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} / {self.main_category.name} / {self.sub_category.name} "


class ProductVariety(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_variety")
    product_code = models.CharField(max_length=50, null=True, blank=True)
    has_color = models.BooleanField(default=False)
    colors = models.CharField(max_length=30, null=True, blank=True)
    has_size = models.BooleanField(default=False)
    sizes = models.CharField(max_length=30, null=True, blank=True)
    has_volume = models.BooleanField(default=False)
    volumes = models.CharField(max_length=30, null=True, blank=True)
    stock = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    discount = models.BooleanField(default=False)
    off_price = models.CharField(max_length=10, null=True, blank=True)
    discount_percent = models.CharField(max_length=2, null=True, blank=True)
    weight = models.CharField(max_length=50)
    max_order = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.product.title} / {self.colors} / {self.sizes} / {self.volumes} / {self.stock} / {self.price}"

