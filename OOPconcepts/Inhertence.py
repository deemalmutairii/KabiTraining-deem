from OOPconcepts.Abstraction import Brand


# Defining the TechnologyBrand class, which represents a technology brand
class TechnologyBrand(Brand):
    def __init__(self, name, country_of_origin, tech_type):
        super().__init__(name, country_of_origin)
        self.tech_type = tech_type

    def display_info(self):
        print(f"Brand: {self.get_name()} | Country: {self.get_country()} | Tech Type: {self.tech_type}")


# Defining the FashionBrand class, which represents a Fashion brand
class FashionBrand(Brand):
    def __init__(self, name, country_of_origin, fashion_type):
        super().__init__(name, country_of_origin)
        self.fashion_type = fashion_type

    def display_info(self):
        print(f"Brand: {self.get_name()} | Country: {self.get_country()} | Fashion Type: {self.fashion_type}")
