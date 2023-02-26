from django.db import models
#Apps imports
from apps.users.models import User
from apps.projects.models.abstract import Abstract
#Utility imports
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class FlightProject(Abstract):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='standBy')
        def get_by_slug(self, slug):
            return self.get(id=slug.rsplit('-', 1)[1])

    STATUS = (
        ('draft', 'Draft'),
        ('completed', 'Completed'),
        ('inprogress', 'InProgress'),
        ('canceled', 'Canceled'),
        ('standBy', 'StandBy')
    )
    tech_route = (
        ('arrival', 'Arrival'),
        ('departure', 'Departure'),
        ('connection', 'Connection')
    )

    user = models.ForeignKey(User, related_name='user_projects', on_delete=models.PROTECT) 
    project_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    project_name = models.CharField(_("Project name"), max_length=355, null=False)
    technology = models.CharField(_("Tech"), choices=tech_route, max_length=15, default="")
    description = models.TextField(_("Description"), default="")
    status = models.CharField(_("Status"), choices=STATUS, max_length=15, default="draft")
    slug = models.SlugField(unique=True, editable=False)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    objects = models.Manager()
    postObjects = PostObjects()
 
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.task_date}-{self.id}-flight:{self.flight}')
        super(FlightProject, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("FlightProject")
        verbose_name_plural = _("FlightProjects")
        ordering = ('-status',)


    def __str__(self):
        return f"{self.task_date} - {self.technology.upper()}"
    
    # def get_model_fields(register):
    #    return register._meta.get_field('ac_type')

    def get_absolute_url(self):
        return reverse("FlightProject_detail", kwargs={"pk": self.pk})
