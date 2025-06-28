from django import forms


class userClassForm(forms.Form):
    num1 = forms.CharField(
        label="Value 1",
        required=False,
        # widget=forms.Textarea(attrs={"class": "form-control"}),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    num2 = forms.CharField(
        label="Value 2",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    num3 = forms.CharField(
        label="Value 3",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="email",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Enter Email here"}
        ),
    )
