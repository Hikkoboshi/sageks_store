from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'delivery', 'city', 'address']
        widgets = {
            'delivery': forms.RadioSelect(choices=Order.DELIVERY)
        }

    # def __init__(self, *args, **kwargs):
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         if visible.field.widget.attrs['type'] == 'text':
    #             visible.field.widget.attrs['class'] = 'form-control'


class OrderStatusForm(forms.Form):
    order_id = forms.CharField(label='Номер заказа', widget=forms.TextInput, initial=None)

    def __init__(self, *args, **kwargs):
        super(OrderStatusForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
