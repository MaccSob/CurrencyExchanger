import requests
from django.shortcuts import render

def change_currency(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        
        rate = data['rates'][to_currency]
        changed_amount = amount * rate
        
        return render(request, 'exchanger/homepage.html', {
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'changed_amount': round(changed_amount, 2)
        })
    
    return render(request, 'exchanger/exchange.html')