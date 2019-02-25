from django.shortcuts import render
import datetime
# dict(APC=, PDP=)

# Create your views here.
def index(request):
    now = datetime.datetime.now().strftime('%H:%M')
    party_dict = { 'now': now,

                    'parties': {'Ekiti': dict(APC=219231, PDP=154032), 'Osun': dict(APC=347634, PDP=337377), 'FCT': dict(APC=152224, PDP=259997), 'Kwara': dict(APC=308984, PDP=138184), 'Nassarawa': dict(APC=289903, PDP=283847), 'Ondo': dict(APC=241769, PDP=275901), 'Kogi': dict(APC=285894, PDP=218207), 'Gombe': dict(APC=402961, PDP=138484), 'Abia': dict(APC=85058, PDP=219698), 'Yobe': dict(APC=497914, PDP=50763),
                                'Enugu': dict(APC=54423, PDP=355553)}

                    }

    sapc = 0; spdp = 0; bias=[]
    for k, v in party_dict['parties'].items():
        v['bias'] = v['APC'] - v['PDP']
        sapc += v['APC']
        spdp += v['PDP']


    party_dict.update({'bias': bias})
    party_dict.update({'sapc': sapc})
    party_dict.update({'spdp': spdp})
    party_dict.update({'tbias': sapc-spdp})





    return render(request, 'index.html', context=party_dict)
