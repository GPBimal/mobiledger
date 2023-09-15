from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Uzerlist
from .models import Mainledger
from .models import Customer


'''
यो काम html फाईललाई देखाउने मात्र हो ।
'''
def home_view(request):
    return render(request, 'home.html') 

def clientfind_view(request):
    return render(request, 'clientfind.html')

def newclient_view(request):
    return render(request, 'newclient.html')

def ledger_view(request):
    return render(request, 'statement.html')

def newtrans_view(request):
    return render(request, 'newtrans.html')

def daybook_view(request):
    return render(request, 'daybook.html')

def renew_view(request):
    return render(request, 'renewlist.html')

def backup_view(request):
    return render(request, 'backup.html')

'''
यो भन्दा तलको सवै काम Action वाला छ ।
'''
def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Uzerlist.objects.get(uzername=username, uzerpw=password)

            return render(request, 'home.html')

        except Uzerlist.DoesNotExist:
            error_message = 'Invalid username or password.'

    else:
        error_message = ''

    return render(request, 'login.html', {'error_message': error_message})

def do_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        userlevel = int(request.POST['userlevel'])

        if password1 != password2:
            error_message = 'Passwords do not match. Please try again.'
        else:
            try:
                existing_user = Uzerlist.objects.get(uzername=username)
                error_message = 'Username already exists. Please choose a different one.'
            except Uzerlist.DoesNotExist:
                new_user = Uzerlist(uzername=username, uzerpw=password1, uzerlevel=userlevel)
                new_user.save()

                return redirect('login')
    else:
        error_message = ''

    return render(request, 'signup.html', {'error_message': error_message})

def do_combo_rec(request):
    districts = Customer.objects.values('DistName').distinct().order_by('DistName')
    agents = Customer.objects.values('AgentName').distinct().order_by('AgentName')
    softwares = Customer.objects.values('software').distinct().order_by('software')

    context = {
        'districts': districts,
        'agents': agents,
        'softwares': softwares,
    }

    return render(request, 'customer.html', context)

def do_client_find(request):
    full_name_filter = ''
    dist_name_filter = ''

    if request.method == 'POST':
        full_name_filter = request.POST.get('full_name_filter', '')
        dist_name_filter = request.POST.get('dist_name_filter', '')

    customers = Customer.objects.filter(
        FullName__icontains=full_name_filter,
        DistName__icontains=dist_name_filter
    )

    context = {
        'customers': customers,
        'full_name_filter': full_name_filter,
        'dist_name_filter': dist_name_filter
    }

    return render(request, 'clientlist.html', context)

def do_trans_entry(request):
    if request.method == 'POST':
        customer_idno = request.POST['customerIDNO']
        transaction_date = request.POST['transactionDate']
        payment_code = request.POST['paymentCode']
        amount_rs = request.POST['amount']
        payment_narration = request.POST['paymentNarration']
        vat_bill_no = request.POST.get('vatBillNo', 0)
        approved = request.POST['approved']
        approved_value = 1 if approved == 'Yes' else 0

        try:
            new_entry = Mainledger(
                IDNO=customer_idno,
                NepDate=transaction_date,
                EngDate=transaction_date,
                Particular=payment_narration,
                AmtRs=amount_rs,
                AmtCode=payment_code,
                VatBillNo=vat_bill_no,
                Approved=approved_value,
            )
            
            new_entry.save()
            return redirect('home')
        except Exception as e:
            print(str(e))  # Print any exceptions for debugging
    return render(request, 'newtrans.html')