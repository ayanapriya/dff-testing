import os

LOG_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'custom': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s] [%(filename)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIRECTORY + "/logs/logfile.log",
            'maxBytes': 1000000,
            'backupCount': 100,
            'formatter': 'custom',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'api_log': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    }
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
