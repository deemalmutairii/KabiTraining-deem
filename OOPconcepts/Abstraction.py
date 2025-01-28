# Importing ABC and abstractmethod to define Abstract Class
from abc import ABC, abstractmethod

# Defining an abstract class Brand that inherits from ABC and
# Constructor to initialize the brand's name and country of origin
class Brand(ABC):
    def __init__(self, name, country_of_origin):
        self.__name = name
        self.__country_of_origin = country_of_origin

    # Abstract method that must be implemented by any subclass of Brand
    @abstractmethod
    def display_info(self):
        pass

    # Setter method to set the brand's name with validation to ensure it's not empty
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Name must not be empty.")

    # Getter method to retrieve the brand's name
    def get_name(self):
        return self.__name

    # Setter method to set the country of origin with validation
    def set_country_of_origin(self, country):
        if len(country) > 0:
            self.__country_of_origin = country
        else:
            print("Country must not be empty.")

    # Getter method to retrieve the country of origin
    def get_country(self):
        return self.__country_of_origin
