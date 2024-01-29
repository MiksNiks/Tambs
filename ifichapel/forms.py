from django.forms import ModelForm
from .models import Baptism, Funerals, Marriage, Blessing, Contact, paying

class BaptismForm(ModelForm):
    class Meta:
        model = Baptism
        fields = '__all__'

class MarriageForm(ModelForm):
    class Meta:
        model = Marriage
        fields = '__all__'

class FuneralForm(ModelForm):
    class Meta:
        model = Funerals
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = paying
        fields = '__all__'

class BlessingForm(ModelForm):
    class Meta:
        model = Blessing
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
