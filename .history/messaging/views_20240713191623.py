from django.http import HttpResponse
from .tasks import send_email, log_message
import re

def email_valid(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def index(request):
    sendmail = request.GET.get('sendmail')
    talktome = request.GET.get('talktome')

    if sendmail:
        if email_email(sendmail):
            try:
                send_email.delay(sendmail)
                return HttpResponse({'message': f'Email queued for sending to {sendmail}'})
            except Exception as e:
                return HttpResponse({'message': f'Failed to send email: {str(e)}'}, status=500)
        else:
            return HttpResponse({'message': 'Invalid email format'}, status=400)

    if talktome:
        log_message()
        return JsonResponse({'message': 'Message logged'})

    return JsonResponse({'message': 'Use ?sendmail or ?talktome parameters'})

def get_logs(request):
    try:
        with open('/var/log/messaging_system.log', 'r') as f:
            logs = f.read()
        return JsonResponse({'logs': logs}, status=200)
    except Exception as e:
        return JsonResponse({'message': f'Failed to retrieve logs: {str(e)}'}, status=500)
