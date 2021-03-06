from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from soloist.apps.portals.models import PortalClientsAll, PortalsAll
from soloist.apps.clients.models import ClientCategoriesAll
from soloist.apps.categories.models import CategoryProjectsAll
from .models import ProjectWorklogsAll
# from .forms import WorklogForm


# def save_worklog(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = WorklogForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/p/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = WorklogForm()
#
#
# def edit_worklog(request, pa_code, pca_code, cpa_id, pwa_id):
#     portal = get_object_or_404(PortalsAll, pa_code=pa_code)
#     client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)
#
#     # we are getting project directly by cpa_id so technically above parsers are
#     # not needed, but that's unsafe to ID probing
#     project = get_object_or_404(CategoryProjectsAll, cpa_id=cpa_id)
#     category = get_object_or_404(ClientCategoriesAll, cca_id=project.cca_id)
#     worklog = get_object_or_404(ProjectWorklogsAll, pwa_id=pwa_id, cpa_id=project.cpa_id)
#
#     data = {
#         'pwa_note': worklog.pwa_note,
#         'pwa_markdown': worklog.pwa_markdown,
#         'pwa_id': worklog.pwa_id,
#         'cpa_id': worklog.cpa_id,
#     }
#     form = WorklogForm(data)
#
#     template = 'projects/edit_worklog.html'
#     context = {
#         'form': form,
#         'portal': portal,
#         'client': client,
#         'project': project,
#         'category': category,
#         'worklog': worklog,
#     }
#     return render(request, template, context)


def detail_render(request, portal, client, project, category, pwa_id, project_hours):
    worklog = get_object_or_404(ProjectWorklogsAll, pwa_id=pwa_id, cpa_id=project.cpa_id)

    worklog_hours = worklog.workloghoursall_set.all().order_by('created_at')
    worklog_files = worklog.worklogfilesall_set.all().order_by('created_at')

    # do not use only() - it causes a lookup query on client_categories_all
    # by "cca_id" = ID to be executed in the loop!
    #category_list = client.clientcategoriesall_set.only('cca_id', 'cca_code')
    category_list = client.clientcategoriesall_set.all()

    worklog_nav = ProjectWorklogsAll.gall.worklog_nav(p_cpa_id=project.cpa_id, p_pwa_id=pwa_id)

    template = 'projects/detail.html'
    context = {
        'worklog': worklog,
        'worklog_hours': worklog_hours,
        'worklog_files': worklog_files,
        'project_hours': project_hours,
        'worklog_nav': worklog_nav,
        'category_list': category_list,
        'client': client,
        'project': project,
        'category': category,
        'portal': portal,
    }
    return render(request, template, context)


def worklogs(request, pa_code, pca_code, cpa_id):
    portal = get_object_or_404(PortalsAll, pa_code=pa_code)
    client = get_object_or_404(PortalClientsAll, pa_id=portal.pa_id, pca_code=pca_code)

    # we are getting project directly by cpa_id so technically above parsers are
    # not needed, but that's unsafe to ID probing
    project = get_object_or_404(CategoryProjectsAll, cpa_id=cpa_id)
    category = get_object_or_404(ClientCategoriesAll, cca_id=project.cca_id)

    worklog_hours = ProjectWorklogsAll.gall.worklog_hours(p_cpa_id=project.cpa_id)
    project_hours = ProjectWorklogsAll.gall.project_hours(p_cpa_id=project.cpa_id)

    if len(worklog_hours) == 1:
        return detail_render(request, portal, client, project, category, worklog_hours[0].pwa_id, project_hours)

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
    project_hours = ProjectWorklogsAll.gall.project_hours(p_cpa_id=project.cpa_id)

    return detail_render(request, portal, client, project, category, pwa_id, project_hours)
