from psycopg2 import ProgrammingError
from sqlalchemy import Column, DateTime, Integer, String, func

from core.db import Base, SessionLocal


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(128))
    content = Column(String(256))
    author = Column(String(128))
    created_at = Column(DateTime, default=func.now())


def create_post(title: str, content: str, author: str):
    with SessionLocal() as session:
        post = Post(title=title, content=content, author=author)
        session.add(post)
        try:
            session.commit()
        except ProgrammingError as e:
            raise ProgrammingError('Incorrect data was passed')
    return post


def get_post(post_id: int):
    with SessionLocal() as session:
        session = SessionLocal()
        post = session.query(Post).get(post_id)

    if post:
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author
        }
        return post_data
    raise ProgrammingError('Post not found')


def update_post(post_id: int, title: str, content: str):
    with SessionLocal() as session:
        post = session.query(Post).get(post_id)

        if post:
            post.title = title if title else post.title
            post.content = content if content else post.content
            session.commit()
            return post
    raise ProgrammingError('Post not found')


def delete_post(post_id):
    with SessionLocal() as session:
        post = session.query(Post).get(post_id)
        if post:
            session.delete(post)
            session.commit()
            return 1
    raise ProgrammingError('Post not found')
