from rest_framework.serializers import ModelSerializer
from articleapp.models import Article

class ArticleSerializer(ModelSerializer):
    class Meata:
        model = Article
        fields = ['title','image','content']