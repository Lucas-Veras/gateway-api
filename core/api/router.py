from core.api import views
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter(trailing_slash=False)

router.register(r"gateway", views.GatewayAPI, basename="gateway")
