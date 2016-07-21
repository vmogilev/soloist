from django.shortcuts import get_object_or_404, render
from portals.models import PortalClientsAll, PortalsAll


def categories(request, pa_code, pca_code):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)
    category_list = client.clientcategoriesall_set.all()
    template = 'clients/categories.html'
    context = {
        'category_list': category_list,
        'portal': portal,
        'client': client,
    }
    return render(request, template, context)
