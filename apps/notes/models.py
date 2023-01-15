from django.db import models
from apps.users.models import User
from django.http import HttpResponse
from author.decorators import with_author
from tinymce.models import HTMLField
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from django_bookmark_base.models import BookmarkModel
from pytils.translit import slugify

# class SharedBox(models.Model):
#     " Keeps track of who shares what to whom, and when "
#     when = models.DateTimeField(auto_now_add=True)
#     note = models.ForeignKey("Note", on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

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
    category = TreeForeignKey('Category',null=True,blank=True, on_delete=models.CASCADE)
    obj = models.ForeignKey(
        'Collection', related_name="bookmark_set", on_delete=models.CASCADE)
    box = models.ForeignKey(NoteShares, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    content = HTMLField()
    share_to = models.ManyToManyField(User, related_name="share_to_user")
    tags = models.ManyToManyField(Tag, blank=True, null=True, default="")
    createAt = models.DateTimeField(_("Create At"), auto_now_add=True)
    updateAt = models.DateTimeField(_("Create At"), auto_now=True)

    class Meta:
        unique_together = [('obj', 'created_by')]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    
    def get_tags(self):
        return ",".join([str(p) for p in self.tags.all()])



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