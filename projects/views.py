from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch
from portals.models import PortalClientsAll, PortalsAll
from clients.models import ClientCategoriesAll
from categories.models import CategoryProjectsAll
from worklogs.models import WorklogHoursAll


def worklogs(request, pa_code, pca_code, cpa_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)

    # we are getting project directly by cpa_id so technically above parsers are
    # not needed, but that's unsafe to ID probing
    project = get_object_or_404(CategoryProjectsAll, cpa_id=cpa_id)
    category = get_object_or_404(ClientCategoriesAll, cca_id=project.cca_id)

    queryset = WorklogHoursAll.objects.order_by('created_at')
    worklog_list = project.projectworklogsall_set.all().order_by('created_at').prefetch_related(
        Prefetch('workloghoursall_set', queryset=queryset, to_attr='hours')
    )

    template = 'projects/worklogs.html'
    context = {
        'worklog_list': worklog_list,
        'client': client,
        'project': project,
        'category': category,
        'portal': portal,
    }
    return render(request, template, context)
