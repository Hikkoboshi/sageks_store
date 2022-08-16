from django import forms


class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(BasketAddProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
