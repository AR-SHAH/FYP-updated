from rest_framework import generics
from mainApp.models import ProductReview, Product
from mainApp.serializers import GroupedSerializer, CreateSerializer
from mainApp.serializers import ReadSerializer


class DetailView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = GroupedSerializer


class CreateView(generics.CreateAPIView):

    queryset = ProductReview.objects.all()
    serializer_class = CreateSerializer


class ReadView(generics.CreateAPIView):

    queryset = ProductReview.objects.all()
    serializer_class = ReadSerializer
