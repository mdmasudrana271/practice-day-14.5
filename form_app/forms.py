from django import forms

from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label="User name",widget=forms.Textarea(attrs={'id':'name-text','placeholder':'Enter your name'}))
    email = forms.EmailField(label = "User email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'id':'birthday-text','type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id':'appointemnt-text','type':'datetime-local'}))

    CHOICE = [('M','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    MEAL = [('P','pepperoni'),('M','mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)


def checkLen(value):
    if len(value)<5:
        raise forms.ValidationError("text must be at least 5 character long")

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name',widget=forms.TextInput,validators=[validators.MinLengthValidator(5, message='name must be at least 5 characters long')])
    text = forms.CharField(widget=forms.TextInput, validators=[checkLen])
    email = forms.CharField(label='Student Email',widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email address')])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(30,message='age contains at most 30'), validators.MinValueValidator(10,message='age must be at least 10')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="file must be a valid PDF file")])


    # def clean_name(self):
    #     nameval = self.cleaned_data['name']
    #     if len(nameval)<5:
    #         raise forms.ValidationError("Enter your name atleast 5 character")
    #     return nameval
    # def clean_email(self):
    #     emailval = self.cleaned_data['email']
    #     if ".com" not in emailval:
    #         raise forms.ValidationError("Enter valid email your email must contain @ and .com")
    #     return emailval

    # def clean(self):
    #     nameval = self.cleaned_data['name']
    #     emailval = self.cleaned_data['email']
    #     if len(nameval)<5:
    #         raise forms.ValidationError("Enter your name atleast 5 character")
    
    #     if ".com" not in emailval:
    #         raise forms.ValidationError("Enter valid email your email must contain @ and .com")