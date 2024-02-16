


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from com.Emp_data.database.model import User, Company, Client, Employee


class DAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)

    def get_companies_by_employees_range(self, min_employees, max_employees):
        session = self.Session()
        companies = session.query(Company).filter(Company.employees.between(min_employees, max_employees)).all()
        session.close()
        return companies

    def get_clients_by_user(self, user_id):
        session = self.Session()
        clients = session.query(Client).filter(Client.user_id == user_id).all()
        session.close()
        return clients

    def search_companies_by_name(self, name):
        session = self.Session()
        companies = session.query(Company).filter(Company.name.like(f'%{name}%')).all()
        session.close()
        return companies

    def get_companies_with_max_revenue(self):
        query = """
        SELECT c.id, c.name
        FROM companies c
        JOIN (
            SELECT company_id, MAX(revenue) as max_revenue
            FROM (
                SELECT e.company_id, COUNT(*) as revenue
                FROM employees e
                GROUP BY e.company_id
            ) as sub
            GROUP BY company_id
        ) as sub2 ON c.id = sub2.company_id;
        """
        session = self.Session()
        companies = session.execute(query)
        session.close()
        return companies


