from django.shortcuts import render
from django_bookmark_base.views import BookmarkToggleView
from apps.collections.models import Collection, CollectionBookmark



# Create your views here.


# class CollectionDetailView(BookmarkViewMixin):
#     bookmark_model = CollectionBookmark


class CollectionBookmarkToggleView(BookmarkToggleView):
    bookmark_model = CollectionBookmark

    def get_data(self):
        collection = Collection.objects.get(pk=self.kwargs['pk'])
        return {
            'bookmarked': self.bookmarked,
            'bookmarks_count': collection.bookmarks_count
        }