from django.forms import ModelForm, DecimalField, CharField

from .models import LotteryUser
# Create the form class.

class LotteryUserForm (ModelForm):

    name = CharField(label="Nombre")
    number = DecimalField(label="Numero", max_digits=5, max_value=99999, min_value=00000)
    class Meta:

        model = LotteryUser
        exclude = ['prize']
