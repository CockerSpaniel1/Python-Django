from django import forms
from order.models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields ="__all__"
        #fields = ['username','password']