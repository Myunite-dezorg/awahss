import json
import logging
from django.views import View
from django.http import JsonResponse

from core.celery import app
from core.settings import DEBUG


logger = logging.getLogger(__name__)