from django.shortcuts import get_object_or_404, render

from portals.models import PortalClientsAll, PortalsAll
from clients.models import ClientCategoriesAll
from categories.models import CategoryProjectsAll
from .models import ProjectWorklogsAll


def worklogs(request, pa_code, pca_code, cpa_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)

    # we are getting project directly by cpa_id so technically above parsers are
    # not needed, but that's unsafe to ID probing
    project = get_object_or_404(CategoryProjectsAll, cpa_id=cpa_id)
    category = get_object_or_404(ClientCategoriesAll, cca_id=project.cca_id)

    worklog_hours = ProjectWorklogsAll.gall.worklog_hours(p_cpa_id=project.cpa_id)
    project_hours = ProjectWorklogsAll.gall.project_hours(p_cpa_id=project.cpa_id)
    category_list = client.clientcategoriesall_set.all()

    template = 'projects/worklogs.html'
    context = {
        'worklog_hours': worklog_hours,
        'project_hours': project_hours,
        'category_list': category_list,
        'client': client,
        'project': project,
        'category': category,
        'portal': portal,
    }
    return render(request, template, context)


def detail(request, pa_code, pca_code, cpa_id, pwa_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)

    # we are getting project directly by cpa_id so technically above parsers are
    # not needed, but that's unsafe to ID probing
    project = get_object_or_404(CategoryProjectsAll, cpa_id=cpa_id)
    category = get_object_or_404(ClientCategoriesAll, cca_id=project.cca_id)
    worklog = get_object_or_404(ProjectWorklogsAll, pwa_id=pwa_id, cpa_id=cpa_id)

    worklog_hours = worklog.workloghoursall_set.all().order_by('created_at')
    worklog_files = worklog.worklogfilesall_set.all().order_by('created_at')

    # do not use only() - it causes a lookup query on client_categories_all
    # by "cca_id" = ID to be executed in the loop!
    #category_list = client.clientcategoriesall_set.only('cca_id', 'cca_code')
    category_list = client.clientcategoriesall_set.all()

    template = 'projects/detail.html'
    context = {
        'worklog': worklog,
        'worklog_hours': worklog_hours,
        'worklog_files': worklog_files,
        'category_list': category_list,
        'client': client,
        'project': project,
        'category': category,
        'portal': portal,
    }
    return render(request, template, context)
