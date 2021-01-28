from django.shortcuts import render

# Create your views here.
def receiverHomePage(request):
    return render(request, 'ReceiverHomePage.html', {})

def senderHomePage(request):
    return render(request, 'SenderHomePage.html', {})