from django.conf import settings
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView

from tasks.models import Task


class StaticPageView(TemplateView):
    """ Static Page Template View """
    def get(self, request, slug=None): 
        if slug:
            self.template_name = 'pytraining/%s.html' % slug
            request.page = slug
        else:
            request.page = 'home'
        result = super(StaticPageView, self).get(request, slug)
        if not settings.DEBUG:
            try:
                result.resolve_template(self.template_name)
            except TemplateDoesNotExist, e:
                raise Http404
        return result


class HomePageView(TemplateView):
    """ Home page tempalte view """
    template_name = 'pytraining/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({'latest_tasks': Task.objects.order_by('-created_at')[:5]})
        return context
