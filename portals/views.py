from django.shortcuts import get_object_or_404, render
from .models import PortalsAll


def index(request):
    portal_list = PortalsAll.objects.all()
    template = 'portals/index.html'
    context = {
        'portal_list': portal_list,
    }
    return render(request, template, context)


def clients(request, pa_code):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client_list = portal.portalclientsall_set.all()
    template = 'portals/clients.html'
    context = {
        'client_list': client_list,
    }
    return render(request, template, context)
