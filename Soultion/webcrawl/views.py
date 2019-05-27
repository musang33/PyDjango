from django.shortcuts import render
from webcrawl.models import LatestInfoTbl, RssDataTbl
from .forms import RssAddressForm
from .SongCrawl import CrawlClass

# Create your views here.
def PrintfRssDataTbl(request):
    rssDataTbl = RssDataTbl.objects.all()
   
    for item in rssDataTbl :
            print( item.no )
            print( item.title ) 
            
    return render(request, 'PrintfRssDataTbl.html', {'rssDataTbl':rssDataTbl})

def FormStripeRss(request):    
    form = RssAddressForm()
    return render(request, 'FormStripeRss.html', {'form':form})

def ExecuteStripeRss(request):    
    form = RssAddressForm(request.POST)
    if form.is_valid():
        rssAddress = form.cleaned_data.get('rss_address')
        crawlClass = CrawlClass()
        crawlClass.ParseRss(LatestInfoTbl, RssDataTbl)
        return PrintfRssDataTbl( request )        
