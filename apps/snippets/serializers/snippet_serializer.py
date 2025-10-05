from rest_framework import serializers
from apps.snippets.models import Snippet, Tag
from django.urls import reverse

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'created_at']
        read_only_fields = ['id', 'created_at']


class SnippetListSerializer(serializers.ModelSerializer):
    """Serializer for listing snippets with basic information."""
    
    tags = TagSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'url',
            'tags',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_url(self, obj):
        """Generate URL for snippet detail."""
        request = self.context.get('request')
        if request:

            return request.build_absolute_uri(
                reverse('snippet-detail', kwargs={'snippet_id': obj.pk})
            )
        return None


class SnippetDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'note',
            'user',
            'tags',
            'created_at',
            'updated_at'
        ]


class SnippetCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating snippets."""
    
    tag_titles = serializers.ListField(
        child=serializers.CharField(max_length=50),
        write_only=True,
        required=False,
        allow_empty=True
    )
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'note',
            'tag_titles',
            'tags',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'tags', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user

        tag_titles = validated_data.pop('tag_titles', [])

        snippet = Snippet.objects.create(**validated_data)
        
        for tag_title in tag_titles:
            tag_title = tag_title.strip()
            if tag_title:
                tag, created = Tag.objects.get_or_create(title=tag_title)
                snippet.tags.add(tag)
        
        return snippet
    
    def update(self, instance, validated_data):
        tag_titles = validated_data.pop('tag_titles', None)
        
        instance.title = validated_data.get('title', instance.title)
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        
        if tag_titles is not None:
            instance.tags.clear()
            for tag_title in tag_titles:
                tag_title = tag_title.strip()
                if tag_title:
                    tag, created = Tag.objects.get_or_create(title=tag_title)
                    instance.tags.add(tag)
        
        return instance