from django.shortcuts import render, redirect
from .models import *
from .forms import BaptismForm, MarriageForm, FuneralForm, BlessingForm, ContactForm, PaymentForm

def home_page(request): return render(request, 'pages/home.html')

def about_page(request): return render(request, 'pages/about.html')

def verification(request): return render(request, 'pages/verification.html')

def lockin(request): return render(request, 'pages/lockin.html')


def marriage_page(request):
 form = MarriageForm()

 if request.method == 'POST':
    form = MarriageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('lockin')

 context = {'form': form}
 return render(request, 'pages/marriage.html', context)

def update2(request, pk):
    marriage = Marriage.objects.get(id=pk)
    form = MarriageForm(instance=marriage)

    if request.method == 'POST':
     form = MarriageForm(request.POST, request.FILES, instance=marriage)
     if form.is_valid():
         form.save()
         return redirect('verification')

    context = {'form':form}
    return render(request, 'pages/marriage.html', context)

def delete22(request, pk):
    marriage = Marriage.objects.get(id=pk)
    context = { 'marriage':marriage}
    if request.method == 'POST':
        marriage.delete()
        return redirect('verification')
    return render(request, 'pages/delete2.html', context)


def birth_page(request):
 form = BaptismForm()

 if request.method == 'POST':
    form = BaptismForm(request.POST, request.FILES)
    if form.is_valid():
       form.save()
       return redirect('lockin')

 context = {'form':form}
 return render(request, 'pages/birth.html', context)


def update(request, pk):
    baptism = Baptism.objects.get(id=pk)
    form = BaptismForm(instance=baptism)

    if request.method == 'POST':
     form = BaptismForm(request.POST, request.FILES, instance=baptism)
     if form.is_valid():
         form.save()
         return redirect('verification')

    context = {'form':form}
    return render(request, 'pages/birth.html', context)

def delete(request, pk):
    baptism = Baptism.objects.get(id=pk)
    context = { 'baptism':baptism}
    if request.method == 'POST':
        baptism.delete()
        return redirect('verification')
    return render(request, 'pages/delete.html', context)

def bless_page(request):
    form = BlessingForm()

    if request.method == 'POST':
        form = BlessingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lockin')

    context = {'form': form}
    return render(request, 'pages/bless.html', context)

def update4(request, pk):
    blessing = Blessing.objects.get(id=pk)
    form = BlessingForm(instance=blessing)

    if request.method == 'POST':
     form = BlessingForm(request.POST, request.FILES, instance=blessing)
     if form.is_valid():
         form.save()
         return redirect('verification')

    context = {'form':form}
    return render(request, 'pages/bless.html', context)

def delete44(request, pk):
    blessing = Blessing.objects.get(id=pk)
    context = { 'blessing':blessing}
    if request.method == 'POST':
        blessing.delete()
        return redirect('verification')
    return render(request, 'pages/delete4.html', context)

def death_page(request):
    form = FuneralForm()

    if request.method == 'POST':
        form = FuneralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lockin')

    context = {'form': form}
    return render(request, 'pages/death.html', context)

def update3(request, pk):
    funeral = Funerals.objects.get(id=pk)
    form = FuneralForm(instance=funeral)

    if request.method == 'POST':
     form = FuneralForm(request.POST, request.FILES, instance=funeral)
     if form.is_valid():
         form.save()
         return redirect('verification')

    context = {'form':form}
    return render(request, 'pages/death.html', context)

def delete33(request, pk):
    funeral = Funerals.objects.get(id=pk)
    context = { 'funeral':funeral}
    if request.method == 'POST':
        funeral.delete()
        return redirect('verification')
    return render(request, 'pages/delete3.html', context)

def contact_page(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {'form': form}
    return render(request, 'pages/contact.html', context)

def status_page(request):
 baptism = Baptism.objects.all()
 total_bookings = baptism.count()

 marriage = Marriage.objects.all()
 total_bookings_mar = marriage.count()

 funeral = Funerals.objects.all()
 total_bookings_fur = funeral.count()

 blessing = Blessing.objects.all()
 total_bookings_ble = blessing.count()


 accepted = SchedStatus.objects.all()
 context = {
  'baptism': baptism,
  'total_bookings': total_bookings,
  'accepted': accepted,
  'marriage': marriage,
  'total_bookings_mar': total_bookings_mar,
  'funeral': funeral,
  'total_bookings_fur': total_bookings_fur,
  'blessing': blessing,
  'total_bookings_ble': total_bookings_ble
 }
 return render(request, 'pages/statuspage.html', context)

def payment(request):
    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {'form': form}
    return render(request, 'pages/payment.html', context)



