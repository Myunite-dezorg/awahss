# import uuid
# import os
# import datetime
# from django.utils.text import slugify

# from django.db import models
# from django.urls import reverse
# from tinymce.models import HTMLField
# from django.utils.translation import gettext as _
# from apps.users.models import User
# from apps.directory.models import Register, Station
# from apps.payload.models import Payload
# from django.conf import settings
# from django.utils.text import slugify
# from django.utils.html import mark_safe
# from mptt.models import MPTTModel, TreeForeignKey


# class DocsCategory(MPTTModel):
#   name = models.CharField(max_length=50, unique=True)
#   parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.PROTECT)
#   slug = models.SlugField()

#   class MPTTMeta:
#     order_insertion_by = ['name']

#   class Meta:
#     unique_together = (('parent', 'slug',))
#     verbose_name_plural = 'categories'

#   def get_slug_list(self):
#     try:
#       ancestors = self.get_ancestors(include_self=True)
#     except:
#       ancestors = []
#     else:
#       ancestors = [ i.slug for i in ancestors]
#     slugs = []
#     for i in range(len(ancestors)):
#       slugs.append('/'.join(ancestors[:i+1]))
#     return slugs

#   def __str__(self):
#     return self.name


# class UUID(models.Model):
#     pkid = models.BigAutoField(primary_key=True, editable=False)
#     id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

#     class Meta:
#         abstract = True


# class Abstract(UUID):
#     create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
#     update_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         abstract = True

# class Tag(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name}"



# class TaskAttachments(models.Model):
#     def file_upload_to(self, instance=None):
#         if instance:
#             return os.path.join('Airlines/Tasks/Docs_attachments', slugify(self.slug), instance)
#         return None

#     def task_attachments_directory_path(instance, filename):

#         category_name = slugify(instance.category)
#         _, extension = os.path.splitext(filename)
#         return f"airline_task_docs/{category_name}{extension}"

#     category = TreeForeignKey(DocsCategory, null=True, blank=True, on_delete=models.PROTECT)
#     file = models.FileField(upload_to=task_attachments_directory_path, max_length=100, null=True)
#     description = models.CharField(max_length=155)
#     content = HTMLField(blank=True, default="")
#     tags = models.ManyToManyField(Tag, blank=True, null=True)
#     createAt = models.DateTimeField(auto_now=True)
#     updateAt = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"{self.category}"

# class FlightTask(Abstract):

#     class PostObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset() .filter(status='standBy')
#         def get_by_slug(self, slug):
#             return self.get(id=slug.rsplit('-', 1)[1])

#     STATUS = (
#         ('draft', 'Draft'),
#         ('completed', 'Completed'),
#         ('inprogress', 'InProgress'),
#         ('canceled', 'Canceled'),
#         ('standBy', 'StandBy')
#     )
#     tech_route = (
#         ('arrival', 'Arrival'),
#         ('departure', 'Departure')
#     )

#     user = models.ForeignKey(User, related_name='user_entries', on_delete=models.PROTECT) 
#     task_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
#     technology = models.CharField(_("Tech"), choices=tech_route, max_length=15, default="")
#     airline = models.ForeignKey(Airline, related_name='flight_airline', on_delete=models.PROTECT)
#     registration = models.ForeignKey(Register, related_name='flight_register', on_delete=models.PROTECT)
#     flight = models.CharField(_("Flight"), max_length=6, default="")
#     sched_time =models.TimeField(_("Schedule time"), auto_now=False, auto_now_add=False, null=True, blank=True)
#     route = models.ForeignKey(Station, related_name='flight_station', on_delete=models.PROTECT)
#     payload = models.CharField(_("Payload(kg)"), max_length=50, default="")
#     description = models.TextField(_("Description"), default="")
#     payload_item = models.ForeignKey(Payload, on_delete=models.CASCADE, blank=True, null=True)
#     status = models.CharField(_("Status"), choices=STATUS, max_length=15, default="draft")
#     slug = models.SlugField(unique=True, editable=False)
#     tags = models.ManyToManyField(Tag, blank=True, null=True)
#     docs = models.ForeignKey(TaskAttachments, on_delete=models.PROTECT, null=True)
#     objects = models.Manager()
#     postObjects = PostObjects()
 
#     def save(self, *args, **kwargs):
#         self.slug = slugify(f'{self.task_date}-{self.id}-flight:{self.flight}')
#         super(FlightTask, self).save(*args, **kwargs)


#     class Meta:
#         verbose_name = _("FlightTask")
#         verbose_name_plural = _("FlightTasks")
#         ordering = ('-status',)


#     def __str__(self):
#         return f"{self.task_date} - {self.technology.upper()} - {self.flight.upper()} "
    
#     def get_model_fields(register):
#        return register._meta.get_field('ac_type')

#     def get_absolute_url(self):
#         return reverse("FlightTask_detail", kwargs={"pk": self.pk})
