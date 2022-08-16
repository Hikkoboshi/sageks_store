from django.shortcuts import render, redirect


def home_page(request):
    return redirect('product_list')
    # return render(request, 'sageks_store/main/home.html')



