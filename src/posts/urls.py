from django.urls import path

from .views import PostsView, PostView
from .views import DropRatingView, RaiseRatingView, RestoreRatingView
from .views import AddToBookmarksView, RemoveFromBookmarksView


urlpatterns = [
	path('', PostsView.as_view(), name='posts_view'),
	path('<int:id>/', PostView.as_view(), name='post_view'),
	path('<int:id>/drop_rating/', DropRatingView.as_view(), name='drop_rating'),
	path('<int:id>/raise_rating/', RaiseRatingView.as_view(), name='raise_rating'),
	path('<int:id>/restore_rating/', RestoreRatingView.as_view(), name='restore_rating'),
	path('<int:id>/add_to_bookmarks/', AddToBookmarksView.as_view(), name='add_to_bookmarks'),
	path('<int:id>/remove_from_bookmarks/', RemoveFromBookmarksView.as_view(), name='remove_from_bookmarks'),
]