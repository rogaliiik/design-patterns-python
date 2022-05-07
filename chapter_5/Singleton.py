from threading import Thread


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


def call():
    s = Singleton()
    print(s)


t1 = Thread(target=call()).run()
t2 = Thread(target=call()).run()
