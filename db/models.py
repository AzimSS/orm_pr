from db import films, base

def create_table():
	print("connect database")
	base.db.connect()
	base.db.create_tables([films.FilmModel])