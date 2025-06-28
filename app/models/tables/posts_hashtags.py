from ...config.db import db

posts_hashtags = db.Table('posts_hashtags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtags.id'), primary_key=True)
)