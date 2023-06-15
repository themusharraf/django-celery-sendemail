from django.http import HttpResponse

from .tasks import send_email


def index(request):
    send_to = 'shubham.tmp123@gmail.com'
    send_email.delay(send_to)
    return HttpResponse("Mail request sent")