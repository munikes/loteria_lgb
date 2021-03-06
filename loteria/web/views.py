from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import LotteryUser

class LotteryUserList(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'number_list'

    def get_queryset(self):
        """Return all numbers"""
        return LotteryUser.objects.all().order_by('number')


class LotteryUserCreate(generic.edit.CreateView):
    model = LotteryUser
    fields = ['name', 'number']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('lotteryuser-list')


class LotteryUserUpdate(generic.edit.UpdateView):
    model = LotteryUser
    fields = ['name', 'number', 'prize']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('lotteryuser-list')


class LotteryUserDelete(generic.edit.DeleteView):
    model = LotteryUser
    success_url = reverse_lazy('lotteryuser-list')
