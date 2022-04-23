from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObserver(self, temp, humidity, pressure):
        if self.observers:
            for i in self.observers:
                i.update(temp, humidity, pressure)
        else:
            print('No observers!')


class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        pass


class Observer(DisplayElement):
    def __init__(self, temp=None, humidity=None, pressure=None):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"temp: {self.temp}, humidity: {self.humidity}, pressure: {self.pressure}")

    def attach(self, weather_station):
        weather_station.registerObserver(self)

    def detach(self, weather_station):
        weather_station.removeObserver(self)


class WeatherData(Subject):
    def __init__(self, temp=None, humidity=None, pressure=None):
        super().__init__()
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

    def measurementsChanged(self, temp, humidity, pressure):
        self.notifyObserver(temp, humidity, pressure)

    def setMeasurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged(self.temp, self.humidity, self.pressure)


class WeatherStation:
    @staticmethod
    def main():
        weatherData = WeatherData()
        observer = Observer()
        # weatherData.registerObserver(observer)  # Subject adds Observer
        observer.attach(weatherData)  # Observer subs to Subject
        weatherData.setMeasurements(80, 65, '30.4f')


WeatherStation().main()
