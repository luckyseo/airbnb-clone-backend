# from django.shortcuts import render
from .models import Category
from rest_framework.exceptions import NotFound

# from django.http import JsonResponse
# from django.core import serializers
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""
class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):  # name diff from model name and class name
    def get_object(self, pk):  # conventional way
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_category = serializer.save()
            return Response(CategorySerializer(update_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""
