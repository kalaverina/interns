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


class TagsForm(forms.ModelForm):
    class Meta:
        model = models.Tags
        fields = "__all__"


class UserTagsForm(forms.ModelForm):
    class Meta:
        model = models.UserTags
        fields = "__all__"
