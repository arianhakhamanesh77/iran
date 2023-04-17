from django.shortcuts import render
from store.models import AdsModel, BestProductModel, HotOfferModel, CategoryModel, ProductModel
# Create your views here.
from datetime import datetime, timezone

def homeView(request):
    ads = AdsModel.objects.filter(is_publish=True)[:]
    bestproduct = BestProductModel.objects.filter(is_publish=True)[:]
    hotoffer = HotOfferModel.objects.filter(is_publish=True)[:]
    category = CategoryModel.objects.all()
    if hotoffer:
        now = datetime.now(timezone.utc)
        duration = hotoffer[0].time - now
        x = duration.total_seconds() // 1
    z = {}




    context = {
        'ads':ads,
        'bests':bestproduct,
        'hot':hotoffer,
        'x':x,
        'categorys':category
    }
    return render(request, 'home.html', context=context)

