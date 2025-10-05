from apps.snippets.models import Tag, Snippet
from apps.snippets.serializers.snippet_serializer import (
    SnippetListSerializer,
    SnippetDetailSerializer,
    SnippetCreateUpdateSerializer,
    TagSerializer
)
from django.db.models import Q



class SnippetActions:
    @staticmethod
    def snippet_list(request):
        try:
            snippets = Snippet.objects.filter(user=request.user)
            serializer = SnippetListSerializer(snippets,context={'request':request}, many=True)
            return snippets.count(),serializer.data
        except Exception:
            raise


    @staticmethod
    def snippet_detail(request, snippet):
        try:
            serializer = SnippetDetailSerializer(snippet,context={'request':request})
            return serializer.data
        except Snippet.DoesNotExist:
            return None
        except Exception:
            raise
    