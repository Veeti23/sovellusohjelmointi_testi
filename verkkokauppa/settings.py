import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
