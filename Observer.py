from abc import ABCMeta, abstractmethod

class Observer():
	__metaclass__=ABCMeta

	@abstractmethod
	def update(self, message):
		pass

class Observable():
	__metaclass__=ABCMeta

	def __init__(self):
		self.observers = []

	def register(self, observer):
		self.observers.append(observer)

	def detach(self, observer):
		if observer in self.observers:
			self.observers.remove(observer)

	def notify(self, message):
		for observer in self.observers:
			observer.update(message)

class Newspaper(Observable):

	def __init__(self, name, yearOfCreate):
		self.name = name
		self.yearOfCreate = yearOfCreate

	def add_news(self, news):
		self.notify(news)

class Citizen(Observer):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def update(self, message):
		print('{} learned the news: {}'.format(self.name, message))

if __name__ == '__name__':
	newspaper = Newspaper('City', 1980)
	maksim = Citizen('Max', 20)
	igor = Citizen('Igor', 20)
	newspaper.register(maksim)
	newspaper.register(igor)

	newspaper.add_news('Good news came to our city ...')

	newspaper.detach(igor)

	newspaper.add_news('We lost the Igor!')