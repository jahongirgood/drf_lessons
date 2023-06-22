from rest_framework import serializers
from .models import News,Categry
import datetime

# Nested serializers

class CategrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categry
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class NewsCategorySerializer(serializers.ModelSerializer):
    category = CategrySerializer()
     
    price_after_tax = serializers.SerializerMethodField()
    days_ago = serializers.SerializerMethodField()

    def get_price_after_tax(self,obj):
        price_after = obj.price * 0.88
        return price_after
    def get_days_ago(self,obj):
        today = datetime.datetime.utcnow()
        news_day = obj.created_at
        news_day = news_day.replace(tzinfo=None)
        today = today.replace(tzinfo=None)
        result = today - news_day
        

        if result.days == 0:
            return f"{round(result.seconds / 60 , 1)} minutes"
        else:
            return f"{result.days} days"
    class Meta:
        model = News
        fields = "__all__"