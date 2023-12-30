from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/week3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Veggie(Base):
    __tablename__="veggies"

    # set autoincrement to use the serial data type
    id=Column(Integer,primary_key=True,autoincrement=True)
    colour=Column(String,nullable=False)
    name=Column(String,nullable=False)

    def formatted_name(self):
        return self.colour.capitalize()+" "+self.name.capitalize()

#recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data=[
    {'name':'carrot','colour':'orange'},
    {'name':'onion','colour':'yellow'},
    {'name':'zucchini','colour':'green'},
    {'name':'squash','colour':'yellow'},
    {'name':'pepper','colour':'red'},
    {'name':'onion','colour':'red'}
]

# turn the seed data into a list of Veggie objects
veggie_objects=[]
for item in seed_data:
    v=Veggie(name=item["name"],colour=item["colour"])
    veggie_objects.append(v)

# create a session, insert new records, and commit the session
session=Session()
session.bulk_save_objects(veggie_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# Run a SELECT * query on the veggies table
veggies = session.query(Veggie).all()

for v in veggies:
    print(v.colour, v.name)


# SELECT * FROM veggies ORDER BY name, color
veggies = session.query(Veggie).order_by(
    Veggie.name, Veggie.colour).all()

for i, v in enumerate(veggies):
    print(str(i+1) + ". " + v.formatted_name())