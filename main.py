from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.clients import router as clients_router
from app.routes.businesses import router as businesses_router
from app.routes.staff import router as staff_router
from app.routes.services import router as services_router
from app.routes.reservations import router as reservations_router
from app.routes.client_staff_reservations import router as csr_router
from app.routes.addresses import router as addresses_router

app = FastAPI(title="Business Reservation API", version="1.0.0")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(clients_router)
app.include_router(businesses_router)
app.include_router(staff_router)
app.include_router(services_router)
app.include_router(reservations_router)
app.include_router(csr_router)
app.include_router(addresses_router)

@app.get("/")
def root():
    return {"message": "Business Reservation API is running!"}

