from server.extensions import db
from sqlalchemy.orm import relationship

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='pizza'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

    def to_dict_basic(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }
