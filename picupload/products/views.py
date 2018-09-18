from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import products
from django.utils import timezone

def home(request):
    product=products.objects
    return render(request,'products/home.html',{'products':product})

@login_required(login_url="/accounts/signup")
def create(request):
    if(request.method=='POST'):
        if request.POST['title'] and request.POST['body'] and request.FILES['icone'] and request.FILES['image']:
            product=products()
            product.title=request.POST['title']
            product.body=request.POST['body']
            product.icone = request.FILES['icone']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

        else:
            return render(request, 'products/create.html',{'error':'All Filds are requred'})


    else:
        return render(request,'products/create.html')

def details(request,product_id):
    product=get_object_or_404(products , pk = product_id)
    return render(request,'products/details.html',{'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if (request.method == 'POST'):
        product = get_object_or_404(products, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))








