from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from mainApp.models import Product, ProductReview
from Predictor import test

fields = ['product', 'review', 'polarity', 'score']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id']


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['review', 'polarity', 'score']


class GroupedSerializer(ModelSerializer):

    reviews = ProductReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_id', 'reviews']


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = ['product', 'review']


class ReadSerializer(serializers.ModelSerializer):
    polarity = serializers.CharField(read_only=True)
    score = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductReview
        fields = ['product', 'review', 'polarity', 'score']

    def create(self, validated_data):
        score_tuple = test.score_calculator(validated_data.get('review'))
        validated_data['polarity'] = score_tuple[0]
        validated_data['score'] = score_tuple[1]

        return super().create(validated_data)
