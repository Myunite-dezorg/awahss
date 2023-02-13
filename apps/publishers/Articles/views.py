# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.utils import timezone
# from django.views.generic.list import ListView
# from .models import Article


# class ArticleListView(ListView):

#     model = Article
#     paginate_by = 100  # if pagination is desired

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context