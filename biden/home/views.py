from urllib import response
from xml.dom import xmlbuilder
from zoneinfo import available_timezones
from django.shortcuts import render
from . models import Shipment



def home(request):
    return render(request, 'index.html', {} )


def err404(request):
    tr = request.POST['mess']
    return render(request,'404.html', {'tr':tr } )

def tracking(request):
    if request.method == "POST":
        searched = request.POST['mess']
        shipment = Shipment.objects.filter(no__iexact=searched)
        for x in shipment:
            no = x.no
            fname = x.firstname
            lname = x.lastname
            address = x.address
            country1 = x.country1
            country2 = x.country2
            city1 = x.city1
            city2 = x.city2
            city3 = x.city3
            city4 = x.city4
            city5 = x.city5
            city6 = x.city6
            city7 = x.city7
            date1 = x.date1
            date2 = x.date2
            date3 = x.date3
            date4 = x.date4
            date5 = x.date5
            date6 = x.date6
            date7 = x.date7
            time1 = x.time1
            time2 = x.time2
            time3 = x.time3
            time4 = x.time4
            time5 = x.time5
            time6 = x.time6
            time7 = x.time7
            msg1 = x.msg1
            msg2 = x.msg2
            msg3 = x.msg3
            msg4 = x.msg4
            msg5 = x.msg5
            msg6 = x.msg6
            msg7 = x.msg7

        if shipment:
            return render(request,'tracking.html', {'searched':searched, "fname":fname, "lname":lname, "no":no, 'address':address,
        'country1':country1, 'country2':country2, 'city1':city1, 'city2':city2, 'city3':city3, 'city4':city4, 'city5':city5, 
        'city6':city6,'city7':city7,  'date1':date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6,'date7':date7, 'time1':time1,
        'time2':time2, 'time3':time3, 'time4':time4, 'time5':time5, 'time6':time6, 'time7':time7, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3,
        'msg4':msg4, 'msg5':msg5, 'msg6':msg6, 'msg7':msg7,        
        })
        else:
            return render(request,'404.html', {"searched":searched } )
    else:
        return render(request,'4042.html', { } )