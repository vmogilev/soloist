from django.shortcuts import get_object_or_404, render
from portals.models import PortalClientsAll


def categories(request, pca_code):
    client = get_object_or_404(PortalClientsAll, pca_code=pca_code)
    category_list = client.clientcategoriesall_set.all()
    template = 'clients/categories.html'
    context = {
        'category_list': category_list,
    }
    return render(request, template, context)
