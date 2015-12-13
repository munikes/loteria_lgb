from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import LotteryUser
from .forms import LotteryUserForm

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'number_list'

    def get_queryset(self):
        """Return all numbers"""
        return LotteryUser.objects.all()

@login_required
def create(request):
    if request.method == "POST":
        form = LotteryUserForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/web/')
    else:
        form = LotteryUserForm()

    return render(request, 'create_number.html', {'form': form})
