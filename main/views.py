from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User,Group
from django.http import HttpResponse,JsonResponse
from .models import PartyModel,CategoryModel,DeliveryBoyModel,ProductModel,UserDetails,PurchaseEntryModel,StockModel,NMModel,SalesEntryModel
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Login(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,"login.html")

def Logout(request):
    logout(request)
    return redirect('/')

def is_user(user):
    return User.objects.filter(username=user).exists()

def useremail(email):
    return User.objects.filter(email=email).exists()

def is_admin(user):
    data=User.objects.filter(is_superuser=True)
    for i in data:
        if str(i.username) == str(user):
            return True

@login_required(login_url='Login')
def home(request):
    if is_admin(request.user):
        return render(request,'dashboard.html')
    if is_user(request.user):
        return render(request,'dashboard.html')
    
@login_required(login_url='Login')
def PurchaseEntry(request):
    if is_admin(request.user):
        return render(request,'purchaseentry.html')
    if is_user(request.user):
        return render(request,'purchaseentry.html')

@login_required(login_url='Login')
def AddPurchaseEntry(request):
    try:
        user=str(request.user.username)
        type = 'Purchase'
        cp = NMModel.objects.get(user=user,type=type)
        ProductId = cp.ProductId
    except NMModel.DoesNotExist:
        user = request.user.username
        ProductId = '1'
        type = 'Purchase'
        nm=NMModel.objects.create(ProductId=ProductId,user=user,type=type)
        nm.save()
        cp = NMModel.objects.get(user=user,type=type)
        ProductId = cp.ProductId
    stock = StockModel.objects.filter(ProductId=ProductId,user=user,type=type)
    Category=CategoryModel.objects.filter(user=request.user)
    Product = ProductModel.objects.filter(user=request.user)
    Party = PartyModel.objects.filter(user=request.user)
    tamonut = 0
    for i in stock:
        tamonut += int(i.MRP) * int(i.Quantity)
    data={'Category':Category,'Product':Product,'ProductId':ProductId,'Party':Party,'type':type,'stock':stock,'tamonut':tamonut}
    if request.method=="POST":    
        user=str(request.user.username)
        TypeofPurchase=request.POST.get('TypeofPurchase')
        BillNo=request.POST.get('BillNo')
        InvoiceNo=request.POST.get('InvoiceNo')
        TypeofPayment=request.POST.get('TypeofPayment')
        PartyName=request.POST.get('PartyName')
        ProductId=request.POST.get('ProductId')
        Type='Purchase'
        Amount='0'
        dt=PurchaseEntryModel.objects.create(user=user,TypeofPurchase=TypeofPurchase,BillNo=BillNo,InvoiceNo=InvoiceNo,TypeofPayment=TypeofPayment,PartyName=PartyName,ProductId=ProductId,Type=Type,Amount=Amount)
        dt.save()
        user=str(request.user.username)
        cp = NMModel.objects.get(user=user,type='Purchase')
        cp.ProductId =str(int(cp.ProductId)+1)
        cp.save()
        return redirect('/AddPurchaseEntry')
    return render(request,'addpurchaseentry.html',data)

@login_required(login_url='Login')
def AddPurchaseReturnEntry(request):
    Category=CategoryModel.objects.filter(user=request.user)
    Product = ProductModel.objects.filter(user=request.user)
    data={'Category':Category,'Product':Product}
    return render(request,'addpurchasereturnentry.html',data)

@login_required(login_url='Login')
def SalesEntry(request):
    return render(request,'dashboard.html')

@login_required(login_url='Login')
def AddSalesEntry(request):
    try:
        user=str(request.user.username)
        type = 'Sales'
        cp = NMModel.objects.get(user=user,type=type)
        ProductId = cp.ProductId
    except NMModel.DoesNotExist:
        user = request.user.username
        ProductId = '1'
        type = 'Sales'
        nm=NMModel.objects.create(ProductId=ProductId,user=user,type=type)
        nm.save()
        cp = NMModel.objects.get(user=user,type=type)
        ProductId = cp.ProductId
    stock = StockModel.objects.filter(ProductId=ProductId,user=user,type=type)
    Category=CategoryModel.objects.filter(user=request.user)
    Product = ProductModel.objects.filter(user=request.user)
    Party = PartyModel.objects.filter(user=request.user)
    DB =  DeliveryBoyModel.objects.filter(user=request.user)
    tamonut = 0
    for i in stock:
        tamonut += int(i.MRP) * int(i.Quantity)
    data={'Category':Category,'Product':Product,'ProductId':ProductId,'Party':Party,'type':type,'stock':stock,'tamonut':tamonut,'DB':DB}
    if request.method=="POST":    
        user=str(request.user)
        DeliveryBoyName=request.POST.get('DeliveryBoyName')
        TypeOfBusiness=request.POST.get('TypeOfBusiness')
        DeliveryTime=request.POST.get('DeliveryTime')
        InvoiceNo=request.POST.get('InvoiceNo')
        PartyName=request.POST.get('PartyName')
        ProductId=request.POST.get('ProductId')
        Type='Sales'
        Amount='0'
        dt=SalesEntryModel.objects.create(user=user,DeliveryBoyName=DeliveryBoyName,TypeOfBusiness=TypeOfBusiness,InvoiceNo=InvoiceNo,DeliveryTime=DeliveryTime,PartyName=PartyName,ProductId=ProductId,Type=Type,Amount=Amount)
        dt.save()
        user=str(request.user)
        cp = NMModel.objects.get(user=user,type = 'Sales')
        cp.ProductId =str(int(cp.ProductId)+1)
        cp.save()
        return redirect('/AddPurchaseEntry')
    return render(request,'addsalesentry.html',data)

@login_required(login_url='Login')
def AddSalesReturnEntry(request):
    Category=CategoryModel.objects.filter(user=request.user)
    Product = ProductModel.objects.filter(user=request.user)
    data={'Category':Category,'Product':Product}
    return render(request,'addsalesreturnentry.html',data)

@login_required(login_url='Login')
def Party(request):
    if is_admin(request.user):
        data=PartyModel.objects.all()
        return render(request,'party.html',{'data':data})
    if is_user(request.user):
        data=PartyModel.objects.filter(user=request.user)
        return render(request,'party.html',{'data':data})

@login_required(login_url='Login')
def AddParty(request):
    if request.method=="POST":    
        user=str(request.user)
        PartyName=request.POST.get('PartyName')
        Number=request.POST.get('Number')
        Address=request.POST.get('Address')
        GSTNo=request.POST.get('GSTNo')
        Email=request.POST.get('Email')
        City=request.POST.get('City')
        dt=PartyModel.objects.create(user=user,PartyName=PartyName,Number=Number,Address=Address,GSTNo=GSTNo,Email=Email,City=City)
        dt.save()
        return redirect('/AddParty')
    return render(request,'addparty.html')

@login_required(login_url='Login')
def Product(request):
    if is_admin(request.user):
        data=ProductModel.objects.all()
        return render(request,'product.html',{'data':data})
    if is_user(request.user):
        data=ProductModel.objects.filter(user=request.user)
        return render(request,'product.html',{'data':data})
    

@login_required(login_url='Login')
def AddProduct(request):
    Category = CategoryModel.objects.filter(user=request.user)
    data={"Category":Category}
    if request.method=="POST":    
        user=str(request.user)
        ProductName=request.POST.get('ProductName')
        Tax=request.POST.get('Tax')
        Category=request.POST.get('Category')
        Unit=request.POST.get('Unit')
        PurchasePrice=request.POST.get('PurchasePrice')
        MRP=request.POST.get('MRP')
        SalsePrice=request.POST.get('SalsePrice')
        MinQty=request.POST.get('MinQty')
        MaxQty=request.POST.get('MaxQty')
        BarcodeNo=request.POST.get('Barcode')
        dt=ProductModel.objects.create(user=user,ProductName=ProductName,Tax=Tax,Category=Category,Unit=Unit,PurchasePrice=PurchasePrice,MRP=MRP,SalsePrice=SalsePrice,MinQty=MinQty,MaxQty=MaxQty,BarcodeNo=BarcodeNo)
        dt.save()
        return redirect('/AddProduct')
    return render(request,'addproduct.html',data)

@login_required(login_url='Login')
@csrf_exempt
def SProducts(request,PN,id,type):
    prd = ProductModel.objects.get(id=id)
    user = str(request.user.username)
    val= NMModel.objects.get(user=user,type=type)
    stockproduct = StockModel.objects.create(ProductId=val.ProductId,user=user,type=type,ProductName=prd.ProductName,Category=prd.Category,Tax=prd.Tax,Unit=prd.Unit,PurchasePrice=prd.PurchasePrice,MRP=prd.MRP,MinQty=prd.MinQty,MaxQty=prd.MaxQty,BarcodeNo=prd.BarcodeNo,Quantity='1',Amount='0')
    stockproduct.save()
    get = StockModel.objects.filter(ProductId=val.ProductId,user=user,type=type).values()
    Sc = list(get)
    stock = StockModel.objects.filter(ProductId=val.ProductId,user=user,type=type)
    tamonut = 0
    for i in stock:
        tamonut += int(i.MRP) * int(i.Quantity)
    tamonut = str(tamonut)
    return JsonResponse({'Sc':Sc,'tamonut':tamonut})

@login_required(login_url='Login')
@csrf_exempt
def EditProducts(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        Quantity = str(request.POST['Quantity'])
        MRP = str(request.POST['MRP'])
        type = str(request.POST['type'])
        data=StockModel.objects.get(id=sid,type=type)
        data.Quantity = Quantity
        data.MRP = MRP
        data.save()
    val= NMModel.objects.get(user=request.user,type=type)
    stock = StockModel.objects.filter(ProductId=val.ProductId,user=request.user,type=type)
    tamonut = 0
    for i in stock:
        tamonut += int(i.MRP) * int(i.Quantity)
    tamonut = str(tamonut)
    return JsonResponse({'tamonut':tamonut})

@login_required(login_url='Login')
@csrf_exempt
def ProductsDelete(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        type = request.POST.get('type')
        data=StockModel.objects.get(id=id,type=type)
        data.delete()
        val= NMModel.objects.get(user=request.user,type=type)
        stock = StockModel.objects.filter(ProductId=val.ProductId,user=request.user,type=type)
        tamonut = 0
        for i in stock:
            tamonut += int(i.MRP) * int(i.Quantity)
            tamonut = str(tamonut)
        return JsonResponse({'status':1,'tamonut':tamonut})
    else:
        return JsonResponse({'status':0})

@login_required(login_url='Login')
def Unit(request):
    if is_admin(request.user):
        return render(request,'unit.html')
    if is_user(request.user):
        return render(request,'unit.html')
    
@login_required(login_url='Login')
def DeliveryBoy(request):
    if is_admin(request.user):
        data=DeliveryBoyModel.objects.all()
        return render(request,'deliveryboy.html',{'data':data})
    if is_user(request.user):
        data=DeliveryBoyModel.objects.filter(user=request.user)
        return render(request,'deliveryboy.html',{'data':data})

@login_required(login_url='Login')
def AddDeliveryBoy(request):
    if request.method=="POST":  
        user=str(request.user)
        Name=request.POST.get('Name')
        Number=request.POST.get('Number')
        Address=request.POST.get('Address')
        Licence=request.FILES.get('Licence')
        AdharCard=request.FILES.get('AdharCard')
        PanCard=request.FILES.get('PanCard')
        Email=request.POST.get('Email')
        PassWord=request.POST.get('Password')
        dt=DeliveryBoyModel.objects.create(user=user,Name=Name,Number=Number,Address=Address,Licence=Licence,AdharCard=AdharCard,PanCard=PanCard,Email=Email,PassWord=PassWord)
        dt.save()
        return redirect('/AddDeliveryBoy')
    return render(request,'adddeliveryboy.html')

@login_required(login_url='Login')
def DeliveryBoyDetails(request,pk):
    data=DeliveryBoyModel.objects.get(id=pk)
    return render(request,'deliveryboydetails.html',{'data':data})

@login_required(login_url='Login')
def EditDeliveryBoy(request,pk):
    if is_admin(request.user):
        data=DeliveryBoyModel.objects.get(id=pk)
        if request.method=="POST":    
            data.Name=request.POST.get('Name')
            data.Number=request.POST.get('Number')
            data.Address=request.POST.get('Address')
            data.Email=request.POST.get('Email')
            data.PassWord=request.POST.get('Password')
            if request.FILES.get('Licence'):
                os.remove(data.Licence.path)
                data.Licence=request.FILES.get('Licence')
            if request.FILES.get('AdharCard'):
                os.remove(data.AdharCard.path)
                data.AdharCard=request.FILES.get('AdharCard')
            if request.FILES.get('PanCard'):
                os.remove(data.PanCard.path)
                data.PanCard=request.FILES.get('PanCard')
            data.save()
            return redirect('/DeliveryBoy')
        return render(request,'editdeliveryboy.html',{'data':data})
    return redirect('/')

@login_required(login_url='Login')
def DeleteDeliveryBoy(request,pk):
    if is_admin(request.user):
        data=DeliveryBoyModel.objects.get(id=pk)
        data.delete()
        return redirect('/DeliveryBoy')
    return redirect('/')

@login_required(login_url='Login')
def UserAccount(request):
    if is_admin(request.user):
        data=UserDetails.objects.all()
        return render(request,'useraccount.html',{'data':data})
    return redirect('/')

@login_required(login_url='Login')
def AddUserAccount(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        emailaddress=request.POST.get('emailaddress')
        password=request.POST.get('Password')
        phone=request.POST.get('Number')
        Address=request.POST.get('Address')
        if is_user(username):
            return redirect('/AddUserAccount')
        if useremail(emailaddress):
            return redirect('/AddUserAccount')
        new_user= User.objects.create_user(username,emailaddress,password)
        new_user.save()
        dg=User.objects.get(username=username)
        userd=UserDetails.objects.create(user_id=dg.id,phone=phone,Address=Address)
        userd.save()
        my_customer_group = Group.objects.get_or_create(name='USER')
        my_customer_group[0].user_set.add(new_user)
        return redirect('/AddUserAccount')
    return render(request,'adduseraccount.html')

@login_required(login_url='Login')
def Category(request):
    if is_admin(request.user):
        data=CategoryModel.objects.all()
        return render(request,'category.html',{'data':data})
    if is_user(request.user):
        data=CategoryModel.objects.filter(user=request.user)
        return render(request,'category.html',{'data':data})

    
@login_required(login_url='Login')
def AddCategory(request):
    if request.method=="POST": 
        user=str(request.user)   
        Category=request.POST.get('Category')
        dt=CategoryModel.objects.create(user=user,Category=Category)
        dt.save()
        return redirect('/AddCategory')
    return render(request,'addcategory.html')

def Expanse(request):
    return render(request,'expanse.html')

# def UserAccount(request):
#     return render(request,'useraccount.html')

@login_required(login_url='Login')
def AllDelete(request):
    data=PartyModel.objects.all()
    data.delete()
    data2=CategoryModel.objects.all()
    data2.delete()
    data4=DeliveryBoyModel.objects.all()
    data4.delete()
    data1=ProductModel.objects.all()
    data1.delete()
    data5=StockModel.objects.all()
    data5.delete()
    data6=NMModel.objects.all()
    data6.delete()
    data7=PurchaseEntryModel.objects.all()
    data7.delete()
    data8=SalesEntryModel.objects.all()
    data8.delete()
    # datad=NMModel.objects.get(user=request.user)
    # datad.ProductId='1'
    # datad.save()
    return redirect('/')