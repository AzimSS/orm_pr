import requests

from db import models, films

URL = 'https://cinematica.kg/api/v1/movies/today'


def get_response_to_json(url):
    response = requests.get(url).json()
    return response


json_response = get_response_to_json(URL)['list']
film1 = json_response[0].get('details')


class Film:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def get_info(self):
        return self.__dict__


all_film = [Film(**film) for film in film1]
for film in all_film:
    try:
        print(films.FilmModel.create(film.get_info()))
    except:
        print(film.get_info())
        continue
def get_films(sort: str = None): # -> Select * From filmmodel
	if sort is None:
		for film in films.FilmModel.select():
			print(film.title, film.value, film.order)
	else:
		if hasattr(films.FilmModel, sort):
			# filter = getattr(films.FilmModel, sort)
			for film in films.FilmModel.select().order_by(films.FilmModel.title):
				print(film.id, film.title, film.value, film.order)
		else:
			raise ValueError("нет такого поля!!!")

def get_film(pk:int):#-> Select * From filmmodel where id = pk
	film =  films.FilmModel.get(films.FilmModel.id == pk)
	return {"id":film.id, 'title': film.title, "value":film.value}

def delete_film(pk: int):
	try:
		film = films.FilmModel.get(films.FilmModel.id == pk)
	except Exception:
		print(f'objectc how to id{pk} DoesNotExist')
	else:
		return film.delete_instance()

def update_film(pk: int, **kwargs):
	film = films.FilmModel.get(films.FilmModel.id == pk)
	film.title = kwargs.get("title", film.title)
	film.order = kwargs.get("order", film.order)
	film.value = kwargs.get("value", film.value)
	film.save()

# get_films(sort='title')
# update_film(pk=3, order=3)
# get_films()

# delete_film(pk=)
# get_films()

# obj = Film(**film1[0])
# film_model1 = films.FilmModel(order =obj.order, value = obj.value, title = obj.title)
# film_model1.save()
# films.FilmModel(order =obj.order, value = obj.value, title = obj.title)
# print(film_model1)

# print(obj.get_info())
# models.create_table()