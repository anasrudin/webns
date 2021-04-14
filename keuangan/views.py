from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

from .forms import KasForm
from .models import Kas

from django.db.models import Sum



from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Keuangan",
		'nbar': 'keuangan',
	}
	return render(request, 'keuangan/index.html', context)


@login_required(login_url='/login/')
def indexKeuangan(request):
	getKeuangan = Keuangan.objects.all()
	context = {
		'page_title':'c',
		'getKeuangan':getKeuangan,
		'nbar': 'keuangan',
	}
	return render(request, 'keuangan/index.html', context)


@login_required(login_url='/login/')
def inputTransaksi(request):
	formInput = KasForm(request.POST or None)

	if request.method == 'POST':
		if formInput.is_valid():
			formInput.save()
			messages.success(request, 'Data Posting berhasil dibuat')
		return redirect('keuangan:daftarTransaksi')


	context = {
		"page_title":"Input Transaksi",
		'nbar': 'inputTransaksi',
		'formInput':formInput,
	}
	return render(request, 'keuangan/inputTransaksi.html', context)

@login_required(login_url='/login/')
def daftarTransaksi(request):
	datatransaksi = Kas.objects.all()
	datauangkeluar = Kas.objects.all().filter(jenistransaksi="Pengeluaran")
	datauanginfaq = Kas.objects.all().filter(jenistransaksi="Infaq")

	# saldototal = Kas.objects.aggregate(Sum('saldo'))
	saldototal = sum(datauangkeluar.values_list('nominal', flat=True))



	context = {
		"page_title":"Daftar Transaksi",
		'nbar': 'daftarTransaksi',
		'datatransaksi':datatransaksi,
		'saldototal':saldototal,
		'datauangkeluar':datauangkeluar,
		'datauanginfaq':datauanginfaq,
	}
	return render(request, 'keuangan/daftarTransaksi.html', context)


@login_required(login_url='/login/')
def daftarInfaq(request):
	datatransaksi = Kas.objects.all()
	datauangkeluar = Kas.objects.all().filter(jenistransaksi="Pengeluaran")
	datauanginfaq = Kas.objects.all().filter(jenistransaksi="Infaq")

	# saldototal = Kas.objects.aggregate(Sum('saldo'))
	saldototal = sum(datauanginfaq.values_list('nominal', flat=True))



	context = {
		"page_title":"Daftar Transaksi",
		'nbar': 'daftarTransaksi',
		'datatransaksi':datatransaksi,
		'saldototal':saldototal,
		'datauangkeluar':datauangkeluar,
		'datauanginfaq':datauanginfaq,
	}
	return render(request, 'keuangan/daftarInfaq.html', context)









@login_required(login_url='/login/')
def deleteTransaksi(request,id):
    Kas.objects.filter(id=id).delete()
    messages.success(request, 'Data Transaksi berhasil didelete')
    return redirect('keuangan:daftarTransaksi')



@login_required(login_url='/login/')
def updateTransaksi(request,id):
	instanceModel1 = get_object_or_404(Kas, id=id)
	formInput = KasForm(request.POST or None, instance=instanceModel1)
	if formInput.is_valid():
		profile1 = formInput.save(commit=False)
		profile1.save()
		messages.success(request, f"Success")
		return redirect('keuangan:daftarTransaksi')

	return render(request, 'keuangan/inputTransaksi.html', {'formInput':formInput})





@login_required(login_url='/login/')
def updateInfaq(request,id):
	instanceModel1 = get_object_or_404(Kas, id=id)
	formInput = KasForm(request.POST or None, instance=instanceModel1)
	if formInput.is_valid():
		profile1 = formInput.save(commit=False)
		profile1.save()
		messages.success(request, f"Success")
		return redirect('keuangan:daftarInfaq')

	return render(request, 'keuangan/inputTransaksi.html', {'formInput':formInput})


