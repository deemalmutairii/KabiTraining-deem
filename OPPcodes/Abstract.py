from abc import ABC, abstractmethod

# Creating an abstract  class Brand, which will be inherited by other classes
class Brand(ABC):
    def __init__(self, name, country_of_origin):
        self.__name = name
        self.__country_of_origin = country_of_origin

    @abstractmethod
    def display_info(self):
        pass

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Name must not be empty.")

    def get_name(self):
        return self.__name

    def set_country_of_origin(self, country):
        if len(country) > 0:
            self.__country_of_origin = country
        else:
            print("Country must not be empty.")

    def get_country(self):
        return self.__country_of_origin