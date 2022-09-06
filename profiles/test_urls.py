""" test file for conducting tests on my profiles.urls """

from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestProfilesUrls(TestCase):
    """
    TestProfilesUrls class inherits from Django's TestCase
    Contains all my tests on my profiles.urls
    """

    def test_my_details_url_resolves(self):
        """ tests if the my_details url resolves """

        url = reverse('my_details')
        self.assertEquals(resolve(url).func.view_class, views.MyDetailsView)

    def test_project_drafts_url_resolves(self):
        """ tests if the project_drafts url resolves """

        url = reverse('project_drafts')
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProjectDraftsView
        )

    def test_projects_in_progress_url_resolves(self):
        """ tests if the projects_in_progress url resolves """

        url = reverse('projects_in_progress')
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProjectsInProgressView
        )

    def test_completed_projects_url_resolves(self):
        """ tests if the completed_projects url resolves """

        url = reverse('completed_projects')
        self.assertEquals(
            resolve(url).func.view_class,
            views.CompletedProjectsView
        )

    def test_order_history_url_resolves(self):
        """ tests if the order_history url resolves """

        url = reverse('order_history')
        self.assertEquals(
            resolve(url).func.view_class,
            views.OrderHistoryView
        )

    def test_order_overview_url_resolves(self):
        """ tests if the order_overview url resolves """

        url = reverse('order_overview', args=['123456'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.OrderOverview
        )

    def test_all_songs_url_resolves(self):
        """ tests if the all_songs url resolves """

        url = reverse('all_songs')
        self.assertEquals(
            resolve(url).func.view_class,
            views.AllSongsAdminView
        )

    def test_all_orders_url_resolves(self):
        """ tests if the all_orders url resolves """

        url = reverse('all_orders')
        self.assertEquals(
            resolve(url).func.view_class,
            views.AllOrdersAdminView
        )
