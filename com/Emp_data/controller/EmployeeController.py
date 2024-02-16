from fastapi import FastAPI
from com.Emp_data.service.EmpService import Service
from com.Emp_data.database.model import Company, Client
import uvicorn

app = FastAPI()



@app.get("/companies/")
def get_companies(min_employees: int, max_employees: int):
    companies = Service.get_companies_by_employees_range(min_employees, max_employees)
    return companies


@app.get("/clients/")
def get_clients(user_id: int):
    clients = Service.get_clients_by_user(user_id)
    return clients


@app.get("/companies/search/")
def search_companies(name: str):
    companies = Service.search_companies_by_name(name)
    return companies


@app.get("/companies/revenue/")
def get_companies_with_max_revenue():
    companies = Service.get_companies_with_max_revenue()
    return companies


@app.post("/clients/")
def create_client(client: Client):
    created_client = Service.create_client(client.name, client.email, client.phone, client.user_id, client.company_id)
    return created_client


@app.patch("/clients/{client_id}/")
def change_client_field(client_id: int, field: str, value: str):
    updated_client = Service.change_client_field(client_id, field, value)
    return updated_client


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

