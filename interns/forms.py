from django import forms
import interns.models as models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"


class PaymentsForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = "__all__"
