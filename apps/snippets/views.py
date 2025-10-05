from helpers.helper import get_object_or_none
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Snippet, Tag
from django.db.models import Q
from drf_spectacular.utils import extend_schema
from apps.snippets.services.snippet_services import SnippetActions
from apps.snippets.services.tags_services import TagsActions
from apps.snippets.serializers.snippet_serializer import (
    SnippetCreateUpdateSerializer,
)

"""Snippet Views"""
class SnippetOverviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Snippets"],
        operation_id="snippet-overview",
        description="This endpoint provides an overview of all snippets created by the authenticated user, including the total count of snippets and their details.",
    )
    
    def get(self, request):
        try:
            total_count,snippets_data = SnippetActions.snippet_list(request)

            return Response(
                    {
                        "message": "User registration successfull",
                        "status": True,
                        "data": {
                            'total_count': total_count,
                            'snippets': snippets_data
                        }
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )   


class SnippetCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Snippets"],
        operation_id="snippet-create",
        request=SnippetCreateUpdateSerializer,
        description="This endpoint allows authenticated users to create a new snippet by providing the title, note, and optional tags.",
    )

    def post(self, request):
        try:
            serializer = SnippetCreateUpdateSerializer(data=request.data,context={'request': request})
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            serializer.save()
            return Response(
                {
                    "message": "snippet created successfull",
                    "status": True,
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class SnippetDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Snippets"],
        operation_id="snippet-detail",
        description="This endpoint provides an overview of all snippets created by the authenticated user, including the total count of snippets and their details.",
    )
    
    def get(self, request,snippet_id):
        try:
            snippet = Snippet.objects.filter(Q(id=snippet_id) & Q(user=request.user)).last()
            if not snippet:
                return Response(
                        {
                            "message": "Snippet not found",
                            "status": False,
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )
            snippets_data = SnippetActions.snippet_detail(request,snippet)

            return Response(
                    {
                        "message": "successfull",
                        "status": True,
                        "data": snippets_data
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

 
class SnippetUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Snippets"],
        operation_id="snippet-update",
        request=SnippetCreateUpdateSerializer,
        description="This endpoint allows updating an existing snippet by its ID. Users can modify the title, note, and associated tags of the snippet.",
    )

    def put(self, request,snippet_id):
        try:
            snippet_instance = get_object_or_none(Snippet,id=snippet_id)
            serializer = SnippetCreateUpdateSerializer(snippet_instance,data=request.data,context={'request': request})
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            serializer.save()
            return Response(
                {
                    "message": "snippet updated successfull",
                    "status": True,
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
   

class SnippetDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Snippets"],
        operation_id="snippet-delete",
        request=SnippetCreateUpdateSerializer,
        description="This endpoint allows deleting an existing snippet by its ID. Users can remove a snippet they no longer need.",
    )

    def delete(self, request,snippet_id):
        try:
            snippet_instance = get_object_or_none(Snippet,id=snippet_id)
            if not snippet_instance:
                return Response(
                    {
                        "message": "Snippet not found",
                        "status": False,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            snippet_instance.delete()
            return Response(
                {
                    "message": "Snippet deleted successfully",
                    "status": True,
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
 

"""Tag Views"""

class TagListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Tags"],
        operation_id="tag-list",
        description="This endpoint provides a list of all tags",
    )
    
    def get(self, request):
        try:
            tags_data = TagsActions.tags_list(request)

            return Response(
                    {
                        "message": "successfull",
                        "status": True,
                        "data": tags_data
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )   


class TagDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Tags"],
        operation_id="tag-detail",
        description="This endpoint provides details of a specific tag",
    )
    
    def get(self, request,tags_id):
        try:
            tags_instance = get_object_or_none(Tag,id=tags_id)

            tags_data = TagsActions.tags_detail(request,tags_instance)

            return Response(
                    {
                        "message": "successfull",
                        "status": True,
                        "data": tags_data
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )  
