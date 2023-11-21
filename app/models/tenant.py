from sqlalchemy import Column, Integer, String

from models.database import session, Base


class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    company = Column(Integer)
    email = Column(String)
    phone_number = Column(String)

    @classmethod
    def add_tenant(cls, tenant_entity):
        session.add(tenant_entity)
        session.commit()
