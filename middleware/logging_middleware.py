import logging

# Logging sensitive data
logger = logging.getLogger(__name__)

def log_request(request):
    # Logging passwords
    logger.info(f'User: {request.form.get("username")}')
    logger.info(f'Password: {request.form.get("password")}')
    logger.info(f'Token: {request.headers.get("Authorization")}')
