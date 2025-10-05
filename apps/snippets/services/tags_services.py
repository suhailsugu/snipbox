from apps.snippets.models import Tag
from apps.snippets.serializers.snippet_serializer import (
    TagSerializer
)
from django.db.models import Q



class TagsActions:
    @staticmethod
    def tags_list(request):
        try:
            tags = Tag.objects.all()
            serializer = TagSerializer(tags,context={'request':request}, many=True)
            return serializer.data
        except Exception:
            raise

    @staticmethod
    def tags_detail(request, tags):
        try:
            serializer = TagSerializer(tags,context={'request':request})
            return serializer.data
        except Exception:
            raise