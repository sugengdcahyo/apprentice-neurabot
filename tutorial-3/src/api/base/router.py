from django.views.generic import base
from rest_framework import routers
from api.base.auth.viewsets import (
    RegisterViewsets,
    LoginViewsets
)
from api.base.products.viewsets import (
    ProductViewsets
)

router = routers.DefaultRouter()
router.register('auth/register', RegisterViewsets, basename='register-viewsets')
router.register('auth/login', LoginViewsets, basename='login-viewsets')
router.register('products', ProductViewsets, basename='products-viewsets')
api_v1 = router.urls