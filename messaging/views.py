from django.http import HttpResponse
from .tasks import send_email, log_message

def index(request):
    sendmail = request.GET.get('sendmail')
    talktome = request.GET.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return HttpResponse({'message': f'Email queued to {sendmail}'})

    if talktome:
        log_message.delay()
        return HttpResponse({'message': 'Message logged'})

    return HttpResponse({'message': 'No action taken'})
