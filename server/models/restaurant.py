from server.extensions import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [
                rp.pizza.to_dict_basic()
                for rp in self.restaurant_pizzas if rp.pizza
            ]
        }

    def to_dict_basic(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
