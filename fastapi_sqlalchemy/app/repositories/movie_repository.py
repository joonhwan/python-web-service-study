from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.func import get_db
from app.viewmodels import Movie, MovieCreate
from app.entities import MovieEntity

class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_movie(self, movie_id: int):
        return self.db.query(MovieEntity).filter(MovieEntity.id == movie_id).first()

    def get_movies(self, skip:int = 0, limit:int = 10):
        return self.db.query(MovieEntity).offset(skip).limit(limit).all()

    def create_movie(self, movie: MovieCreate):
        db_movie = MovieEntity(
            title=movie.title,
            director=movie.director,
        )
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

    def delete_movie(self, movie_id: int):
        db_movie = self.db.query(MovieEntity).filter(MovieEntity.id == movie_id).first()
        self.db.delete(db_movie)
        self.db.commit()
        return db_movie

    def update_movie(self, movie_id: int, movie: Movie):
        db_movie = self.db.query(MovieEntity).filter(MovieEntity.id == movie_id).first()
        db_movie.title = movie.title
        db_movie.director = movie.director
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

    @staticmethod
    def inject(db: Session = Depends(get_db)):
        return MovieRepository(db)
