from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from soloist.apps.portals.models import PortalClientsAll, PortalsAll
from soloist.apps.clients.models import ClientCategoriesAll


def projects(request, pa_code, pca_code, cca_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)
    # we can get category directly by cca_id, but that's unsafe to ID probing
    category = get_object_or_404(ClientCategoriesAll, pca_id=client.pca_id, cca_id=cca_id)
    project_list_all = category.categoryprojectsall_set.filter(cpa_deleted=False).order_by('-modified_at')

    paginator = Paginator(project_list_all, 50)  # Show 50 projects per page
    page = request.GET.get('page')
    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project_list = paginator.page(paginator.num_pages)

    # do not use only() - it causes a lookup query on client_categories_all
    # by "cca_id" = ID to be executed in the loop!
    # category_list = client.clientcategoriesall_set.only('cca_id', 'cca_code')
    category_list = client.clientcategoriesall_set.all()

    template = 'categories/projects.html'
    context = {
        'project_list': project_list,
        'category_list': category_list,
        'client': client,
        'portal': portal,
        'category': category,
    }
    return render(request, template, context)
