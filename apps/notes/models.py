from django.db import models
from apps.users.models import User
from django.http import HttpResponse
from author.decorators import with_author
from tinymce.models import HTMLField
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from django_bookmark_base.models import BookmarkModel

# class SharedBox(models.Model):
#     " Keeps track of who shares what to whom, and when "
#     when = models.DateTimeField(auto_now_add=True)
#     note = models.ForeignKey("Note", on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



class Collection(models.Model):
    bookmarks_count = models.IntegerField(default=0) # use triggers

    def get_bookmark_url(self):
        return 'bookmark/collection/%s' % self.pk

    def __str__(self):
        return f"{self.bookmarks_count}"


class NoteShares(MPTTModel):
     owner = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=255)
     shared_with = models.ManyToManyField(User, related_name='notes_sharedwithme', through="SharedBox")
     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


     def __str__(self):
        return self.title


     def get_shared_with(self):
        return ",".join([str(p) for p in self.shared_with.all()])


@with_author
class Note(BookmarkModel):
    obj = models.ForeignKey(
        'Collection', related_name="bookmark_set", on_delete=models.CASCADE)
    box = models.ForeignKey(NoteShares, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    content = HTMLField()

    createAt = models.DateTimeField(_("Create At"), auto_now_add=True)
    updateAt = models.DateTimeField(_("Create At"), auto_now=True)

    class Meta:
        unique_together = [('obj', 'created_by')]

    def __str__(self):
        return self.title
    



class SharedBox(models.Model):
    " Keeps track of who shares what to whom, and when "
    when = models.DateTimeField(auto_now_add=True)
    box = models.ForeignKey(NoteShares, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   






# def share_item(request, note_id, user_id, **kwargs):
   
#     user   = request.user
   
#     note      = Note.objects.get(
#         id=note_id, owner=user)

#     SharedBox.objects.create_or_update(
#         note=note, user=user)
#     return HttpResponse("OK") 