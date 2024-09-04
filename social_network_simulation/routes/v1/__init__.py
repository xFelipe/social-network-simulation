from fastapi.routing import APIRouter
from social_network_simulation.routes.v1.user_router import router as user_router
from social_network_simulation.core.settings import settings


router = APIRouter(prefix=settings.API_V1_PREFIX)


router.include_router(user_router, prefix="/user", tags=["user"])
