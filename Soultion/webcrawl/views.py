from django.shortcuts import render
from webcrawl.models import RssDataTbl
from .forms import RssAddressForm

# Create your views here.
def PrintfRssDataTbl(request):
    rssDataTbl = RssDataTbl.objects.all()
    context = {'rssDataTbl':rssDataTbl}
    return render(request, 'PrintfRssDataTbl.html', context)

def FormStripeRss(request):    
    form = RssAddressForm()
    return render(request, 'FormStripeRss.html', {'form':form})

def ExecuteStripeRss(request):    
    form = RssAddressForm(request.POST)
    if form.is_valid():
        rssAddress = form.cleaned_data.get('rss_address')
        return render(request, 'ExecuteStripeRss.html',  {'rssAddress':rssAddress})
