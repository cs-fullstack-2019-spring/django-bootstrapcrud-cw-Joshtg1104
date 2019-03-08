from django.shortcuts import render, redirect, get_object_or_404
from .forms import GarageSellForm, GarageSellModel


# Create your views here.
# Isn't being used but allows for every item to be iterated through
def index(request):
    allItems = GarageSellModel.objects.all()
    context = {
        "allItems": allItems
    }

    return render(request, 'BootCRUDApp/index.html', context)

# Allows user to add item
def addItem(request):
    sellform = GarageSellForm(request.POST or None)
    allItems = GarageSellModel.objects.all()
    if request.method == "POST":
        if sellform.is_valid():
            sellform.save()
            return redirect('index')
    context = {
        "sellform": sellform,
        "allItems": allItems
    }
    print(sellform)
    return render(request, 'BootCRUDApp/index.html', context)

# Allows user to edit item
def editItem(request, ID):
    edit = get_object_or_404(GarageSellModel, pk=ID)
    itemEdit = GarageSellForm(request.POST or None, instance=edit)
    if itemEdit.is_valid():
        itemEdit.save()
        return redirect('index')
    context = {
        "sellform": itemEdit,
    }
    print(itemEdit)
    return render(request, 'BootCRUDApp/edit.html', context)
