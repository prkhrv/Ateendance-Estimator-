from django.shortcuts import render
from myapp.forms import calculate

# Create your views here.


def index(request):

    new = ' '
    new1 = ' '
    per = 75
    form = calculate()
    if(request.method=='POST'):
        form = calculate(request.POST)
        if(form.is_valid()):
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
            d = form.cleaned_data.get('d')
            e = form.cleaned_data.get('e')
            current = (b/c)*100
            expected = (b+(a*e)-d)/(c+(a*e))*100
            new = round(current,2)
            new1 = round(expected,2)
            return render(request,'index.html',{'new':new,'new1':new1,'per':per,})

    return render(request,'index.html')
