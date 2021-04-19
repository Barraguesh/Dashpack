#Python/Django
import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

#Models
from clientModule.models import Log
from clientModule.models import Client
from clientModule.models import Device
from clientModule.models import Ticket

#Global variables
date_now = datetime.datetime.now()
date_db_format = "%Y-%m-%d"
date_pretty_format = "%Y-%m-%d %H:%M"

@permission_required("clientModule.view_ticket")
def index_view(request):
    log = Log(log=f'LOAD INDEX USER -{request.user.username}- {date_now.strftime(date_pretty_format)}',date=date_now.strftime(date_db_format))
    log.save()
    args = {}
    args["module"] = "clientModule"
    args["url"] = "/clientModule/load_table/"
    args["clients"] = Client.objects.all()
    try:
        tickets = Ticket.objects.all()
        if not tickets:
            raise Exception
        else:
            args["months"] = []
            args["month_tickets"] = []
            past_month = date_now.month - 5
            if past_month < 1:
                past_month = 12 + past_month
            for _ in range(6):
                args["months"].append(past_month.strftime("%B"))
                args["month_tickets"].append(len(tickets.filter(date__month=past_month)))
                if past_month < 12:
                    past_month += 1
                else:
                    past_month = 1
            args["months"] = str(args["months"])
            args["services_data"] = []
            for service in get_services():
                args["services_data"].append(len(tickets.filter(service=service)))
    except Exception:
        args["no_data"] = True
    return render(request, 'index.html', args)

@permission_required("clientModule.view_ticket")
def load_table_view(request):
    client = request.GET.get("client")
    log = Log(log=f'LOAD TABLE CLIENT -{client}- USER -{request.user.username}- {date_now.strftime(date_pretty_format)}',date=date_now.strftime(date_db_format))
    log.save()
    args = {}
    try:
        args["tickets"] = Ticket.objects.all().filter(client=client)
        if not args["tickets"]:
            raise Exception
        else:
            args["months"] = []
            args["month_tickets"] = []
            past_month = date_now.month - 5
            if past_month < 1:
                past_month = 12 + past_month
            for _ in range(6):
                args["months"].append(past_month.strftime("%B"))
                args["month_tickets"].append(len(args["tickets"].filter(date__month=past_month)))
                if past_month < 12:
                    past_month += 1
                else:
                    past_month = 1
            args["months"] = str(args["months"])
            args["services_data"] = []
            for service in get_services():
                args["services_data"].append(len(args["tickets"].filter(service=service)))
            args["devices_number"] = []
            args["devices_name"] = []
            args["total_devices"] = 0
            for device in Device.objects.all().filter(client=client):
                args["devices_number"].append(len(args["tickets"].filter(device=device)))
                args["devices_name"].append(device.get_nombre())
                args["total_devices"] += 1
    except Exception:
        args["no_data"] = True
    return render(request, 'tickets_table.html', args)

@permission_required("clientModule.view_ticket")
def ticket_view(request, ticket_id):
    log = Log(log=f'LOAD TICKET -{ticket_id}- USER -{request.user.username}- {date_now.strftime(date_pretty_format)}',date=date_now.strftime(date_db_format))
    log.save()
    args = {}
    args["module"] = "clientModule"
    args["ticket"] = get_object_or_404(Ticket, ticket_id=ticket_id)
    return render(request, 'ticket.html', args)

@permission_required("clientModule.view_device")
def device_view(request, device_id):
    log = Log(log=f'LOAD DEVICE -{device_id}- USER -{request.user.username}- {date_now.strftime(date_pretty_format)}',date=date_now.strftime(date_db_format))
    log.save()
    args = {}
    args["module"] = "clientModule"
    args["device"] = get_object_or_404(Device, device_id=device_id)
    return render(request, 'device.html', args)

#
#Helpers
#
def get_services():
    services = [
        "premium",
        "advanced",
        "standard",
        "low cost"
    ]
    return services