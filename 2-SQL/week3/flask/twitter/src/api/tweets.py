from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

bp=Blueprint('tweets',__name__,url_prefix='/tweets')

# decorator takes path and list of HTTP verbs
@bp.route('',methods=['GET'])
def index():
    # ORM performs SELECT query
    tweets=Tweet.query.all()
    result=[]
    for t in tweets:
        #build list of Tweets as dictionaries
        result.append(t.serialize())
    # return JSON response 
    return jsonify(result)

@bp.route('/<int:id>',methods=['GET'])
def show(id:int):
    t=Tweet.query.get_or_404(id,"Tweet not found")
    return jsonify(t.serialize())

@bp.route('',methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'user_id' not in request.json or 'content' not in request.json:
        return abort(400)
    
    # user with id of user_id must exist
    User.query.get_or_404(request.json['user_id'], "User not found")

    #construct Tweet
    t=Tweet(
        user_id=request.json['user_id'],
        content=request.json['content']
    )

    # prepare CREATE statment
    db.session.add(t)

    # execute CREATE statement
    db.session.commit()

    return jsonify(t.serialize())


#delete tweet endpoint
@bp.route('/<int:id>',methods=['DELETE'])
def delete(id:int):
    t=Tweet.query.get_or_404(id,"Tweet not found")
    try:
        # prepare DELETE statement
        db.session.delete(t)

        # execute DELETE statement
        db.session.commit()

        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)