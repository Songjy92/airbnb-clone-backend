from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .serializers import CategorySerializer  # custom serializer


# Create your views here.

class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            # serializer.save 는 serializers 안에 create 함수를 호출한다.
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)

class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,  # required 인 데이터를 모두 보내지 않고 특정 필드만 업데이트 한다는 것
        )

        if serializer.is_valid():
            updated_category = serializer.save()
            # serializer 가 어떤 형태이냐에 따라서 생성인지 업데이트 인지를 구분해서 보내주는 기능
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)



"""
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            # serializer.save 는 serializers 안에 create 함수를 호출한다.
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)
"""
"""    
@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,  # required 인 데이터를 모두 보내지 않고 특정 필드만 업데이트 한다는 것
        )

        if serializer.is_valid():
            updated_category = serializer.save()
            # serializer 가 어떤 형태이냐에 따라서 생성인지 업데이트 인지를 구분해서 보내주는 기능
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""
