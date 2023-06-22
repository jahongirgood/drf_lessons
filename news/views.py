from django.shortcuts import render
from rest_framework.views import APIView
from .models import News, Categry
from .serilizes import NewsSerializer,NewsCategorySerializer
from rest_framework.response import Response
from django.db.models import Count,Sum
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins


# Create your views here.


class NewsViewset(ModelViewSet):
    serializer_class =NewsSerializer
    queryset = News.objects.all()

class NewsGeneric(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class =NewsSerializer
    queryset = News.objects.all()

class NewsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        news = News.objects.all()
        serializer = NewsCategorySerializer(news, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serilizer = NewsSerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)

class OneNews(APIView):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

class NewsCategory(APIView):
    def get(self, request, category_id):
        news = News.objects.filter(category_id=category_id)
        serializer = NewsSerializer(news,many=True )
        return Response(serializer.data)

class NewsByRange(APIView):
    def post(self,request):
        data = request.data
        start_date = data["start_date"]
        end_date = data["end_date"] 
        news = News.objects.filter(
            created_at__date__gte = start_date, created_at__date__lte = end_date
        ).aggregate(total_cost=Sum("price"))
        return Response(news)

class UserRegister(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            username = data["username"],
            email = data["email"],
            password = make_password(data["password"])
        )
        
        token, created = Token.objects.get_or_create(user=user)   
        return Response({"token": token.key})
    
class LoginUser(APIView):
    def post(self, request):
         data = request.data
         user = authenticate(username=data["username"], password = data["password"])
         if user is not None:
             token, created = Token.objects.get_or_create(user=user)
             return Response({"token": token.key})
         else:
             return Response({"error": "username or password incorrect"})
         

