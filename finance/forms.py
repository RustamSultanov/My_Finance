from datetime import date
from django.forms import ModelForm, ValidationError, Form, CharField, widgets
from finance.models import Charge, Account, User


class ChargeForm(ModelForm):

    class Meta:
        model = Charge
        fields = ['date','value']

    def clean(self):
        cleaned_data = super(ChargeForm, self).clean()
        date_charge = cleaned_data.get('date')
        value_charge = cleaned_data.get('value')
        today = date.today()
        if value_charge < 0:
            if date_charge > today:
                self.add_error('date',"Can't write future outcome")
        return cleaned_data

    def save(self, user):
        obj = super(ChargeForm, self).save(commit=False)
        obj.account = user
        return obj.save()


class CreateAccount(ModelForm):

    class Meta:
        model = Account
        fields = ['account_holder']


class UserProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password','phone_number','adress']

    def clean_username(self):
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise ValidationError("A user with that username already exists.")
        else:
            return self.cleaned_data['username']

class LoginForm(Form):

    username = CharField(widget=widgets.TextInput)
    password = CharField(widget=widgets.PasswordInput)

    class Meta:
        fields = ['username', 'password']

