# Defining a class to demonstrate the concept of encapsulation
class EncapsulationExample:
    def __init__(self):
        self.__private_data = "This is private data"


    def set_private_data(self, data):
        if len(data) > 0:
            self.__private_data = data
        else:
            print("Data must not be empty")


    def get_private_data(self):
        return self.__private_data