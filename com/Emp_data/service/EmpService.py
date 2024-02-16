from typing import List
from datetime import datetime
from com.Emp_data.Dao.EmpDao import DAO
from com.Emp_data.database.model import User, Company, Client, Employee


class Service:
    def __init__(self, db_uri):
        self.dao = DAO(db_uri)

    def get_companies_by_employees_range(self, min_employees: int, max_employees: int) -> List[Company]:
        return self.dao.get_companies_by_employees_range(min_employees, max_employees)

    def get_clients_by_user(self, user_id: int) -> List[Client]:
        return self.dao.get_clients_by_user(user_id)

    def search_companies_by_name(self, name: str) -> List[Company]:
        return self.dao.search_companies_by_name(name)

    def get_companies_with_max_revenue(self):
        companies = self.dao.get_companies_with_max_revenue()
        return [{'id': c.id, 'name': c.name} for c in companies]

    # Additional business logic can be added here

    def create_client(self, name: str, email: str, phone: str, user_id: int, company_id: int) -> Client:
        # Additional validation can be performed here
        client = Client(name=name, email=email, phone=phone, user_id=user_id, company_id=company_id)
        return self.dao.create_client(client)

    def change_client_field(self, client_id: int, field: str, value: str) -> Client:
        # Additional validation can be performed here
        return self.dao.change_client_field(client_id, field, value)
















