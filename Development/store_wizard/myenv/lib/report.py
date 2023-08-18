from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship

class report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product")
    total_sales = Column(Integer)
    total_revenue = Column(Integer)

    @classmethod
    def generate_report(cls, session):
        # Query the total sales and revenue per product
        result = session.query(
            Sale.product_id,
            func.sum(Sale.quantity).label('total_sales'),
            func.sum(Sale.total_amount).label('total_revenue')
        ).group_by(Sale.product_id).all()

        # Generate report objects and add them to the session
        for product_id, total_sales, total_revenue in result:
            report = Report(
                product_id=product_id,
                total_sales=total_sales,
                total_revenue=total_revenue
            )
            session.add(report)

        session.commit()

    def __repr__(self):
        return f"<Report(id={self.id}, product='{self.product.name}', total_sales={self.total_sales}, total_revenue={self.total_revenue})>"

    Report.generate_report(session)

    reports = session.query(Report).all()
    for report in reports:
    print(report)
