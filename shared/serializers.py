from rest_framework import serializers
from .models import Settings, ContactUs, Category, Brand

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    subbrands = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'
