from flask import Blueprint, jsonify, abort, request
from ..models import User,db,Tweet,likes_table
import hashlib
import secrets
import sqlalchemy


def scramble(password: str):
    """Hash and salt the given password"""
    salt=secrets.token_hex(16)
    return hashlib.sha512((password+salt).encode('utf-8')).hexdigest()


bp=Blueprint('users',__name__,url_prefix='/users')

@bp.route('',methods=['GET'])
def index():
    # ORM performs SELECT query
    users=User.query.all()
    result=[]
    for u in users:
        #build list of Tweets as dictionaries
        result.append(u.serialize())
    # return JSON response 
    return jsonify(result)

@bp.route('/<int:id>',methods=['GET'])
def show(id:int):
    u=User.query.get_or_404(id,"User not found")
    return jsonify(u.serialize())

@bp.route('',methods=['POST'])
def create():
    # req body must contain username and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    
    # user with id of user_id must exist<< no use
    # User.query.get_or_404(request.json['user_id'], "User not found")

    if len(request.json['username'])<3 or len(request.json['password'])<8:
        return abort(400)
    
    #construct Tweet
    u=User(
        username=request.json['username'],
        # password=request.json['password']
        password=scramble(request.json['password'])
    )

    # prepare CREATE statment
    db.session.add(u)

    # execute CREATE statement
    db.session.commit()

    return jsonify(u.serialize())


#delete user endpoint
@bp.route('/<int:id>',methods=['DELETE'])
def delete(id:int):
    u=User.query.get_or_404(id,"User not found")
    try:
        # prepare DELETE statement
        db.session.delete(u)

        # execute DELETE statement
        db.session.commit()

        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
    
@bp.route('/<int:id>',methods=['PATCH','PUT'])
def update(id:int):
    #check if the update user exist
    # user record with id is mapped to a python object named u
    u=User.query.get_or_404(id,"User not found")

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'username' in request.json:
        if len(request.json['username'])<3:
            return abort(400)
        else:
            u.username=request.json['username']

    if 'password' in request.json:
        if len(request.json['password'])<8:
            return abort(400)
        else:
            u.password=scramble(request.json['password'])

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
    
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id:int):
    u=User.query.get_or_404(id)

    result=[]

    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)


# Bonus Task 1 -- NO IDEA
@bp.route('/<int:id>/likes', methods=['POST'])
def like(id:int):
    if 'tweet_id' not in request.json:
        return abort(400)
    tweet_id=request.json['tweet_id']

    u=User.query.get_or_404(id,"User not found")
    t=Tweet.query.filter_by(tweet_id=id).get_or_404()

    # A User should not be able to like a Tweet twice.
    # Therefore, any subsequent requests should respond with false.
    stmt=sqlalchemy.insert(User).values(liking_users=u,liked_tweets=t)


# Bonus Task 2 -- NO IDEA
@bp.route('/<int:tweet_id>/likes/<int:user_id>', methods=['DELETE'])
def unlike(user_id:int,tweet_id):
    u=User.query.get_or_404(user_id,"User not found")
    t=Tweet.query.get_or_404(tweet_id,"Tweet not found")

    try:
        # prepare DELETE statement
        # db.session.delete(u)
        stmt=sqlalchemy.delete(likes_table).where(likes_table.tweet_id==t)

        # execute DELETE statement
        db.session.commit()

        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)



