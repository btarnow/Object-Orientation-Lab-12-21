############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller,
    ):
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color 
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller 

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    all_melon_types.append(musk)
    musk.add_pairing("mint")

    cas = MelonType("Casaba", "cas", 2003, "orange", False, False)
    all_melon_types.append(cas)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")

    cren = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    all_melon_types.append(cren)
    cren.add_pairing("prosciutto")

    yw = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, True)
    all_melon_types.append(yw)
    yw.add_pairing("ice cream")

    return all_melon_types

melon_list = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # make_melon_types()
    
    for melon in melon_types:
        print(f"{melon.name} pairs with" )
        for pairing in melon.pairings:
            print(f"- {pairing} ") 
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    def make_melon_type_lookup(melon_types):
   
    #key --> melon code 
    #value --> type of melon

        melon_codes = {}

        for melon in melon_types:
            melon_codes[melon.code] = melon.name

        return melon_codes      

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
