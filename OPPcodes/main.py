from OPPcodes.encapsulation import EncapsulationExample
from OPPcodes.Inheritence import TechnologyBrand, FashionBrand
from OPPcodes.polymorphism import PolymorphismExample


def main():
    # Creating instances of TechnologyBrand and FashionBrand classes
    tech_brand = TechnologyBrand("Apple", "USA", "Smartphones")
    fashion_brand = FashionBrand("Dior", "Italy", "Fashion")
    # Displaying information for both brands by calling their display_info() method
    tech_brand.display_info()
    fashion_brand.display_info()

    encapsulation_example = EncapsulationExample()
    print(encapsulation_example.get_private_data())
    encapsulation_example.set_private_data("New private data")
    print(encapsulation_example.get_private_data())

    polymorphism_example = PolymorphismExample()
    polymorphism_example.display()


if __name__ == "__main__":
    main()