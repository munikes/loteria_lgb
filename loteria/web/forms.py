from django.forms import ModelForm

from .models import LotteryUser
# Create the form class.

class LotteryUserForm (ModelForm):

    class Meta:

        model = LotteryUser
        fields = ['name','number']
