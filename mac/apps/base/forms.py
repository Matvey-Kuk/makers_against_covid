import account.forms
from django.forms import ModelForm, CharField
from django.contrib.auth import get_user_model


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]

class SettingsForm(ModelForm):
    organization = CharField(required=False, label="Организация, которую Вы представляете (обязательно для врачей).")

    class Meta:
        model = get_user_model()
        fields = [
            'city',
            'first_name',
            'last_name',
            'address',
            'contact_data',
            'organization',
        ]
