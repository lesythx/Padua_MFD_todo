from django.shortcuts import render
from .models import List
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            context = {'all items': all_items}
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all()
        context = {'all_items': all_items}
        return render(request, 'home.html', context)

def about(request):
    context = {'myname': 'Peter Parker'}
    return render(request, 'about.html', {})

def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed=true
    item.save()
    return redirected('home')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')