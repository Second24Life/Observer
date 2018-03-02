from abc import ABCMeta, abstractmethod

# Абстрактный класс для наблюдателя
# имеет метод update, который необходимо обязательно переопределить в наследуемых классах
# метод update выполняет какое-либо действие после того как наблюдаемый объект сообщить об событии
class Observer():
	__metaclass__=ABCMeta

	@abstractmethod
	def update(self, message):
		pass

# Абстрактный класс для наблюдаемого объекта
# метод register добавляет новых наблюдателей
# метод detach отцепляет наблюдателя от наблюдаемого объекта
# метод notify сообщает наблюдателям о новом событии
class Observable():
	__metaclass__=ABCMeta
	observers = []

	def register(self, observer):
		self.observers.append(observer)

	def detach(self, observer):
		if observer in self.observers:
			self.observers.remove(observer)

	def notify(self, message):
		for observer in self.observers:
			observer.update(message)

# Класс газеты и немного минимум информации
# метод add_news вызывает метод notify из абстрактного класса, чтобы сообщить о новости 
class Newspaper(Observable):

	def __init__(self, name, yearOfCreate):
		self.name = name
		self.yearOfCreate = yearOfCreate

	def add_news(self, news):
		self.notify(news)

# Класс горожанина и немного информации о нем
# метод update переопределен
class Citizen(Observer):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def update(self, message):
		print('{} learned the news: {}'.format(self.name, message))

# Создаем объект класса Newspaper
newspaper = Newspaper('City', 1980)
# Создаем объекты класса Citizen
maksim = Citizen('Max', 20)
igor = Citizen('Igor', 20)
# Подписываем созданных горожан на газету
newspaper.register(maksim)
newspaper.register(igor)

# Газета добавляет новую новость и сообщает о ней подписчикам
newspaper.add_news('Good news came to our city ...')

# Один из горожан решил отписаться от газеты
newspaper.detach(igor)

# Газета добавляет новость о отписке своего подпичсика
newspaper.add_news('We lost the Igor')