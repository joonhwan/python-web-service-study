import random
from sqlmodel import Session, create_engine, SQLModel
from jewel_app.models.gem import *

engine = create_engine("sqlite:///gem.db", echo=False)

def create_and_update_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


color_multiplier = {
    'D': 1.8,
    'E': 1.6,
    'G': 1.4,
    'F': 1.2,
    'H': 1,
    'I': 0.8
}


def calculate_gem_price(gem, gem_pr):
    price = 1000
    if gem.gem_type == 'Ruby':
        price = 400
    elif gem.gem_type == 'Emerald':
        price = 650

    if gem_pr.clarity == 1:
        price *= 0.75
    elif gem_pr.clarity == 3:
        price *= 1.25
    elif gem_pr.clarity == 4:
        price *= 1.5

    price = price * (gem_pr.size**3)

    if gem.gem_type == GemType.DIAMOND:
        multiplier = color_multiplier[gem_pr.color]
        price *= multiplier

    return price

all_gem_colors = [e.value for e in GemColor]

def create_gem_props():
    size = random.randint(3, 70)/10
    color = random.choice(all_gem_colors)
    clarity = random.randint(1, 4)

    gemp_p = GemProperties(size=size, clarity=clarity,
                           color=color)
    return gemp_p


all_gem_types = [e.value for e in GemType]

def create_gem(gem_prop):
    type = random.choice(all_gem_types)
    gem = Gem(price=1000, gem_properties_id=gem_prop.id, gem_type=type)
    price = calculate_gem_price(gem, gem_prop)
    price = round(price, 2)
    gem.price = price
    return gem


def create_gems_db():
    #gem_p = create_gem_props()
    gem_props = [create_gem_props() for x in range(100)]
    print(gem_props)
    with Session(engine) as session:
        session.add_all(gem_props)
        session.commit()
        gems = [create_gem(gem_props[x]) for x in range(100)]
        # g = create_gem(gem_p.id)
        session.add_all(gems)
        session.commit()



if __name__ == "__main__":
    create_and_update_db()
    create_gems_db()




