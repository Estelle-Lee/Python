# import SQLAlchemy class from flask_sqlalhemy
# SQLAlchemy: A database adapter
# datetime: standard library for the create_at column
from flask_sqlalchemy import SQLAlchemy
import datetime

# create a database adapter object
db=SQLAlchemy()

# create the User class as a subclass of SQLAlchemy's db.Model class
class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(128),unique=True,nullable=False)
    password=db.Column(db.String(128),nullable=False)

    tweets=db.relationship('Tweet',backref='user',cascade="all,delete")

    # user model revisited.
    # add constructor function
    def __init__(self,username:str, password:str):
        self.username=username
        self.password=password

    def serialize(self):
        return{
            'id':self.id,
            'username':self.username
        }

# Next:
# generate a migration file 
# that we can use to create a users table in our Postgres database from the User class/model.


# Flask-Migrate: is a package that helps Alembic and Flask work with each other.

# run the command to generate a migration file based on this new User class:
    # flask db migrate

# to apply migration
    # flask db upgrade

# create and migrate tweet model class 
# (many-to-one with User)

likes_table=db.Table(
    'likes',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'tweet_id',db.Integer,
        db.ForeignKey('tweets.id'),
        primary_key=True
    ),

    db.Column(
        'created_at',db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)


class Tweet(db.Model):
    __tablename__='tweets'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.String(280),nullable=False)
    created_at=db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    liking_users=db.relationship(
        'User',secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_tweets',lazy=True)
    )

    # tweet model revisited.
    # add constructor function
    def __init__(self,content: str, user_id:int):
        self.content=content
        self.user_id=user_id

    #add serialize method: to prepare if for transmission
    # we are preparing to transmit Tweet objects represented as JSON over HTTP
    # we are going to serialize a Tweet as a simple dictionary with key-value pairs for each column in the tweets database table.
    # the only formatting we will make is to the created_at timestamp
        # convert this to a format known as ISO Format
    
    def serialize(self):
        return{
            'id':self.id,
            'content':self.content,
            'created_at':self.created_at.isoformat(),
            'user_id':self.user_id
        }


# create and migrate Like model
# (many-to-many with User and Tweet)
# between the User and Tweet classes in models.py -- line 34

# back references
# get all of the Tweets for a given User, and all of the Likes for a given Tweets
# (or, another way to put it, all the liking_users for a given Tweets)
    # by adding property to the end of the User class.
    # by adding property to the end of the Tweets class.
        # these two changes don't create new migration file of SQL output
        # because they don't modify anything at the SQL layer.