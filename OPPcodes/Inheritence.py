from OPPcodes.Abstract import Brand

# Defining a class TechnologyBrand that inherits from the Brand class
class TechnologyBrand(Brand):
    def __init__(self, name, country_of_origin, tech_type):
        super().__init__(name, country_of_origin)
        self.tech_type = tech_type

    def display_info(self):
        print(f"Brand: {self.get_name()} | Country: {self.get_country()} | Tech Type: {self.tech_type}")

# Defining a class FashionBrand that also inherits from the Brand class
class FashionBrand(Brand):
    def __init__(self, name, country_of_origin, fashion_type):
        super().__init__(name, country_of_origin)
        self.fashion_type = fashion_type

    def display_info(self):
        print(f"Brand: {self.get_name()} | Country: {self.get_country()} | Fashion Type: {self.fashion_type}")