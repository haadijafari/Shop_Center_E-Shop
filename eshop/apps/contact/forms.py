from django import forms
from django.utils.translation import gettext_lazy as _

from apps.contact.models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'full_name', 'email', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'title': _('موضوع'),
                'placeholder': _('موضوع'),
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'title': _('نام و نام خانوادگی'),
                'placeholder': _('نام و نام خانوادگی'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'title': _('ایمیل'),
                'placeholder': _('ایمیل'),
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 8,
                'title': _('متن پیام'),
                'placeholder': _('متن پیام'),
                'id': 'message',
            }),
        }
        labels = {
            'subject': _('موضوع'),
            'full_name': _('نام و نام خانوادگی'),
            'email': ('ایمیل'),
            'message': _('متن پیام'),
        }
        error_messages = {
            'subject': {
                'required': 'لطفا موضوع پیام خود را وارد نمایید',
            },
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد نمایید',
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد نمایید',
            },
            'message': {
                'required': 'لطفا متن پیام خود را وارد نمایید',
            },
        }
