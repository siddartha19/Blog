from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_type = Column(String(250),nullable=False)
    description = Column(String(3000), nullable=False)
    comment = Column(String(500))
    ratings = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'post_type': self.post_type,
            'description': self.description,
            'comment': self.comment,
            'ratings': self.ratings,
        }



engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)


