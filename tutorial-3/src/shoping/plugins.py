# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_ALLOW_ALL = True

'''
Addition configurations
'''
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'X-Auth-Token',
    'Content-Range'
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'api.helpers.paginations.StandardResultsSetPagination',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'PAGE_SIZE': 100,
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'api.serializer.authSerialize.TokenSerialize'
}
