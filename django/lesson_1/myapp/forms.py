
import datetime
from django import forms


# очень простая форма
class ImageForm(forms.Form):
    name = forms.CharField(max_length=50)
    image_l = forms.ImageField(required = True)
