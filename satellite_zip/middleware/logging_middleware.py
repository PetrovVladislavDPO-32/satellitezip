import socket
import time
from django.conf import settings

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        ip_address = request.META.get('REMOTE_ADDR')
        
        response = self.get_response(request)
        
        duration = time.time() - start_time

        log_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'ip_address': ip_address,
            'method': request.method,
            'path': request.path,
            'status_code': response.status_code,
            'duration': round(duration, 4)
        }
        
        self.write_log(log_data)
        
        return response
    
    def write_log(self, log_data):
        log_line = (
            f"{log_data['timestamp']} - {log_data['ip_address']} - "
            f"{log_data['method']} {log_data['path']} - "
            f"Status: {log_data['status_code']} - "
            f"Duration: {log_data['duration']}s\n"
        )
        
        with open(settings.REQUEST_LOGGING_FILE, 'a') as log_file:
            log_file.write(log_line)