from django.views.generic import ListView, DetailView
from .models import Trivia

class TriviaList(ListView):
    model = Trivia
    template_name = 'list.html'

    def get_queryset(self):
        query = super().get_queryset()
        keyword = self.request.GET.get('keyword', None)
        category = self.request.GET.get('category', None)
        if keyword:
            query = query.filter(japanese__icontains=keyword)
        if category:
            query = query.filter(category=category)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["keyword"] = self.request.GET.get('keyword', '')
        lang = self.request.GET.get('lang', '')
        category = self.request.GET.get('category', '')
        if lang == '1':
            context['japanese'] = True
        elif lang == '2':
            context['english'] = True
        elif lang == '3':
            context['chinese1'] = True
        elif lang == '4':
            context['chinese2'] = True
        elif lang == '5':
            context['korean'] = True
        elif lang == '6':
            context['mongolian'] = True
        
        if category == '地理':
            context['geography'] = True
        elif category == '歴史':
            context['history'] = True
        elif category == '人物':
            context['person'] = True
        elif category == '自然':
            context['nature'] = True
        elif category == '伝統':
            context['tradition'] = True
        elif category == 'スポーツ':
            context['sport'] = True
        elif category == '食文化':
            context['food'] = True
        elif category == '文化':
            context['culture'] = True
        elif category == '芸能':
            context['entertainment'] = True
        elif category == '特産品':
            context['goods'] = True
        elif category == '方言':
            context['dialect'] = True

        return context
    
class TriviaDetail(DetailView):
    model = Trivia
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.request.GET.get('lang', '')
        if lang == '1':
            context['japanese'] = True
        elif lang == '2':
            context['english'] = True
        elif lang == '3':
            context['chinese1'] = True
        elif lang == '4':
            context['chinese2'] = True
        elif lang == '5':
            context['korean'] = True
        elif lang == '6':
            context['mongolian'] = True
        return context