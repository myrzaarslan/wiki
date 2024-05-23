from django import forms


class CreateNewPage(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 100, "rows": 20}))



    






