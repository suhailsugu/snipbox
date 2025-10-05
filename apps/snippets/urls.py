from django.urls import path

from .views import (
    SnippetOverviewAPIView,
    SnippetCreateAPIView,
    SnippetDetailAPIView,
    SnippetUpdateAPIView,
    SnippetDeleteAPIView,
    TagListAPIView,
    TagDetailAPIView,
)

urlpatterns = [
    # Snippet endpoints
    path('overview/', SnippetOverviewAPIView.as_view(), name='snippet-overview'),
    path('create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
    path('<int:snippet_id>/', SnippetDetailAPIView.as_view(), name='snippet-detail'),
    path('<int:snippet_id>/update/', SnippetUpdateAPIView.as_view(), name='snippet-update'),
    path('<int:snippet_id>/delete/', SnippetDeleteAPIView.as_view(), name='snippet-delete'),
    
    # Tag endpoints
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/<int:tags_id>/', TagDetailAPIView.as_view(), name='tag-detail'),
]