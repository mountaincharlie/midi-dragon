""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('my-details/', login_required(views.MyDetailsView.as_view()), name='my_details'),
    path('project-drafts/', login_required(views.ProjectDraftsView.as_view()), name='project_drafts'),
    path('projects-in-progress/', login_required(views.ProjectsInProgressView.as_view()), name='projects_in_progress'),
    path('completed-projects/', login_required(views.CompletedProjectsView.as_view()), name='completed_projects'),
    path('order-history/', login_required(views.OrderHistoryView.as_view()), name='order_history'),
    path('order-overview/<order_number>/', login_required(views.OrderOverview.as_view()), name='order_overview'),
    path('all-songs/', login_required(views.AllSongsAdminView.as_view()), name='all_songs'),
    path('all-orders/', login_required(views.AllOrdersAdminView.as_view()), name='all_orders'),
]
