from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch
from django.http import Http404

from portals.models import PortalClientsAll, PortalsAll
from clients.models import ClientCategoriesAll
from categories.models import CategoryProjectsAll
from worklogs.models import WorklogHoursAll, WorklogFilesAll
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

    template = 'projects/worklogs.html'
    context = {
        'worklog_hours': worklog_hours,
        'project_hours': project_hours,
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

    prefetch_hours = Prefetch(
        'workloghoursall_set',
        queryset=WorklogHoursAll.objects.order_by('created_at'),
        to_attr='hours'
    )
    prefetch_files = Prefetch(
        'worklogfilesall_set',
        queryset=WorklogFilesAll.objects.order_by('created_at'),
        to_attr='files'
    )

    worklog_q = ProjectWorklogsAll.objects.\
        filter(pwa_id=pwa_id, cpa_id=cpa_id). \
        prefetch_related(prefetch_hours, prefetch_files)

    try:
        worklog = worklog_q[0]
    except IndexError:
        raise Http404("Worklog does not exist")

    template = 'projects/detail.html'
    context = {
        'worklog': worklog,
        'client': client,
        'project': project,
        'category': category,
        'portal': portal,
    }
    return render(request, template, context)
