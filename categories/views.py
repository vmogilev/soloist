from django.shortcuts import get_object_or_404, render
from portals.models import PortalClientsAll, PortalsAll
from clients.models import ClientCategoriesAll


def projects(request, pa_code, pca_code, cca_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)
    # we can get category directly by cca_id, but that's unsafe to ID probing
    category = get_object_or_404(ClientCategoriesAll, pca_id=client.pca_id, cca_id=cca_id)
    project_list = category.categoryprojectsall_set.all().order_by('-modified_at')
    template = 'categories/projects.html'
    context = {
        'project_list': project_list,
        'pa_code': pa_code,
        'pca_code': pca_code,
        'category': category,
    }
    return render(request, template, context)
