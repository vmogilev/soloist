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
    portal_list = PortalsAll.objects.all()
    client_list = portal.portalclientsall_set.all().order_by('created_at')
    template = 'portals/clients.html'
    context = {
        'client_list': client_list,
        'portal_list': portal_list,
        'portal': portal,
    }
    return render(request, template, context)
