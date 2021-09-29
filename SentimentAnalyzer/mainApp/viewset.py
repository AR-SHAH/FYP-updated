from re import I
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from mainApp.models import Product, ProductReview
from mainApp.serializers import CreateSerializer, GroupedSerializer


class ProductViewSet(viewsets.ViewSet):
    # queryset = Product.objects.all()
    # serializer_class = GroupedSerializer
    # queryset = Product.objects.all()
    # serializer_class = GroupedSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = GroupedSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = GroupedSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        queryset = Product.objects.all()
        return super().create(request)
