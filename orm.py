# import psycopg2

# connection = psycopg2.connect(  # -> \c db_name
#     database='my_projects',
#     user='muhamadamin',
#     password='11',
#     host='localhost',
#     port='5432'

# )
# print("DATABASE succesfully opened")

"""Creating database"""
# cursor = connection.cursor()
# cursor.execute(
# 	'''
# 	CREATE TABLE company(
# 		id SERIAL PRIMARY KEY,
# 		name VARCHAR(100) NOT NULL,
# 		city VARCHAR(50)NOT NULL
# 	)
# 	'''
# )

# print("Table successfully created")
# connection.commit()
# connection.close()

"""Creating records in database"""
# cursor = connection.cursor()
# cursor.execute(
# 	'''
# 		INSERT INTO company(name,city) VALUES ('IBM', 'Los Angeles'),
# 		('Apple', 'Cupertino'),('IBM', 'New York'),('DELL', 'New Jersy')
# 	'''
# )
# connection.commit()
# print("Inserted records")
# connection.close()

"""Print result in here"""
# cursor = connection.cursor()
# cursor.execute(
#     'SELECT * FROM company'
# )
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()

# cursor.execute(
# 	'SELECT name, city FROM company WHERE id=2'
# )
# data = cursor.fetchone()
# print(data)

# from sqlalchemy import Column, Table, Integer, String, MetaData
# from sqlalchemy import create_engine
# engine = create_engine(
#     'postgresql+psycopg2://muhamadamin:11@localhost:5432/my_projects')
# print("DATABASE created successfully")
# metadata = MetaData()
# students_table = Table(
#     'students', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String)
# )
# students_table.create(bind=engine)
# # print("Succesfully created")
# inserted_data = students_table.insert().values(name='John')

# engine.execute(inserted_data)
# print("Successfully inserted")
# from sqlalchemy import select
# query = select([students_table.c.name])
# data = engine.execute(query).fetchall()
# for item in data:
# 	print(*item)]


# from sqlalchemy import create_engine
# from sqlalchemy import Column, Table, Integer, String, MetaData
# engine = create_engine('postgresql+psycopg2://muhamadamin:11@localhost:5432/my_projects')

# metadata = MetaData()
# company_table = Table(
#     'company', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('city', String)
# )
# metadata.create_all(engine)
# class Company:
# 	def __init__(self, name, city):
# 		self.name = name
# 		self.city = city
# 	def __str__(self):
# 		return f'Company {self.name} in {self.city}'
# from sqlalchemy.orm import mapper
# mapper(Company, company_table)
# print("Success")


# from requests import session
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('postgresql+psycopg2://muhamadamin:11@localhost:5432/my_projects')

# Base = declarative_base()
# class Company(Base):
# 	__tablename__ = 'company'
# 	id = Column(Integer, primary_key = True)
# 	name = Column(String)
# 	city = Column(String)

# 	def __init__(self, name, city):
# 		self.name = name
# 		self.city = city

# 	def __str__(self):
# 		return f'Company {self.name} in {self.city}'
# Base.metadata.create_all(engine)
# print("Table created")
# ////""
"""Creating table"""
# Session = sessionmaker(bind=engine)
# session = Session()
# apple = Company(name = 'Aplle', city='Cupertino')
# samsung = Company(name = 'Samsung', city='Seoul')
# session.add(samsung)
# session.commit()


# our_company = session.query(Company).filter_by(city ='Seoul').all()
# print(our_company)

# session.add_all([Company('IBM', 'Washington'), Company('DELL', 'New York')])
# session.commit()
# query = session.query(Company.name, Company.city).all()
# print(query)
