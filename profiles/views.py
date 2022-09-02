from django.shortcuts import render, HttpResponse
# from django.contrib import messages
from django.views import View
from .forms import MyDetailsForm


class ProfileDashboard(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    MAKE A CLASS BASED VIEW?
    """
    def get(self, request, *args, **kwargs):
        """
        get method for getting the forms to be displayed to the user.
        -gets the
        FINISH ...

        """
        # gets the MyDetailsForm()
        # my_details_form = MyDetailsForm()
        try:
            # profile = User.objects.get(id=request.user.id)
            # profile = User.objects.get(id=self.request.user.id)
            my_details_form = MyDetailsForm(initial={
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email,
            })
        except Exception as e:
            my_details_form = MyDetailsForm()
            print('didnt work:', e)
            return HttpResponse(content=e, status=400)

        context = {
            'my_details_form': my_details_form,
            # data for rendering the projects (user's custom songs)
            # unpurchased custom songs
            # bought but incomplete custom songs
            # completed custom songs
            # and orders
        }

        return render(request, 'profiles/profile_dashboard.html', context)

    
