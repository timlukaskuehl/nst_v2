from django import forms
from nst.models import UserInput

class IntroForm(forms.ModelForm):
    # creates the form displayed on the home page. There is only one field, the paintings name, for the user to input into the database
    # a model form is just a model that is connected to a form
    paintings_name = forms.CharField(label='How do you want to name the painting?')

    class Meta:
        # used to link the model to the class created in the form, the input field is defined as "fields"
        model = UserInput
        fields = ("paintings_name",)

