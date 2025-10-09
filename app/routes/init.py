from .auth import router as auth_router
from .users import router as users_router
from .clients import router as clients_router
from .businesses import router as businesses_router
from .staff import router as staff_router
from .services import router as services_router
from .reservations import router as reservations_router
from .client_staff_reservations import router as csr_router
from .addresses import router as addresses_router

__all__ = [
    "auth_router",
    "users_router", 
    "clients_router",
    "businesses_router",
    "staff_router",
    "services_router",
    "reservations_router", 
    "csr_router",
    "addresses_router"
]