from django.shortcuts import render
from django.views import View

from users.forms import RegistrationForm


# Create your views here.
class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request,'users/registration_page.html',{'form':form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'users/registration_page.html',{'is_registration_successful':True})
        else:
            return render(request, 'users/registration_page.html', {'form': form})

