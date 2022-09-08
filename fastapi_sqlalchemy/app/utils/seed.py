from sqlalchemy import text
from app.db.env import Session
from app.entities import MovieEntity

def seed_movie_entities():
    with Session() as session:
        films = [
            MovieEntity(name="Blade Runner", director="Ridley Scott"),
            MovieEntity(name="Endgame", director="Anthony Russo"),
            MovieEntity(name="Rocky", director="John G. Avildsen"),
            MovieEntity(name="The Matrix", director="The Wachowskis"),
            MovieEntity(name="The Terminator", director="James Cameron"),
            MovieEntity(name="The Terminator 2: Judgement Day",
                        director="James Cameron"),
            MovieEntity(name="The Terminator 3: Rise of the Machines",
                        director="Jonathan Mostow"),
        ]
        session.execute(text("delete from movies"))
        session.add_all(films)
        session.commit()
