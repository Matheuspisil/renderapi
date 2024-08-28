from django import forms
from GPC.models.gestor import PageConfiguration

class PageConfigurationForm(forms.ModelForm):
    class Meta:
        model = PageConfiguration
        fields = ['background_color', 'text_color', 'icon']