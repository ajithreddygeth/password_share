DEBUG = True

# Redis configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

# Untouched password entries will be deleted after this period (in seconds)
TTL = 600    # 10 min

# APPLICATION SERVER
APP_PORT = 5000
APP_HOST = '0.0.0.0'

# User Agent blacklist to prevent password withdrawal by bot (in lowercase)
UA_BLACKLIST = [
    'facebook',
    'googlebot',
    'slack'
    'bot',
    'external-hit',
    'fetcher',
    'twitterbot',
    'telegrambot'
]
