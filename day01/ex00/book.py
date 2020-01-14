from datetime import datetime

class Book:
    #attributes
    name = ""
    last_update = datetime.today()
    creation_date = datetime.now()
    recipes_list = dict(starter = "", lunch = "", dessert = "")

    #methods
    def get_recipe_by_name(self, name):
        if name == self.name:
            return (self)
        else:
            print ("This recipe doesnt exist.")

    def get_recipes_by_types(self, recipe_type):
        if recipe_type == self.recipe_type:
            for i in self.name:
                print(self.name)
        else:
            print ("This recipe type doesnt exist.")

    def add_recipe(self, recipe):
        pass