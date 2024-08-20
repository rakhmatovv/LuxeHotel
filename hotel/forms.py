from django import forms
from hotel.models import Booking, Review
from django.forms import ModelForm, Textarea


# class AvailabilityForm(forms.ModelForm):
#     check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d%H:%M", ])
#     check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d%H:%M", ])


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out']
        widgets = {
            'release_at': forms.DateTimeInput(
                attrs={'class': 'form-control', 'data - target': '  # datetimepicker1'}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']
        widgets = {
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment'
            })
        }