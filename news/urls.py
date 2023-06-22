from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register("news_viewset", views.NewsViewset, basename="news_viewset")

urlpatterns = [
    path("news_list/", views.NewsView.as_view()),
    path("news/<int:pk>/", views.OneNews.as_view()),
    path("category/news/<int:category_id>/", views.NewsCategory.as_view()),
    path("news/range/", views.NewsByRange.as_view()),
    path("register/",views.UserRegister.as_view()),
    path("login/",views.LoginUser.as_view()),
] + router.urls
 