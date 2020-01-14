class Recipe:
    #attributes
    name = ""
    cooking_lvl = 1
    cooking_time = 1
    ingredients = []
    description = ""
    recipe_type = ""

    #methods
    def strcmp(self, str1, str2):
        i = 0
        while i < len(str1):
            if (str1[i] == str2[i]):
                i = i + 1
            else:
                return (0)
        return (1)

    def fill_list(self, str):
        list = []
        if self.strcmp(str, "done") == 1:
            print("\nAddition cancelled.\n")
            return (0)
        else:
            list.append(str)
            while self.strcmp(str, "done") == 0:
                str = input("\nNext entry:\n")
                list.append(str)
            list.pop()
            self.ingredients = list.copy()
            del list
            return (1)

    def init_recipe(self):
        self.name = input("Name of the recipe ?")
        try:
            self.cooking_lvl = int(input("Level of difficulty ? (1-5)"))
            self.cooking_time = int(input("Cooking time ? (In minutes)"))
        except:
            print("Input error. Exiting.")
            self.cooking_lvl = 1
            self.cookin_time = 1
            self.name = ""
            return
        str = (input("Ingredients ? (Enter \"done\" to finish)"))
        while self.fill_list(str) != 1:
            pass
        self.description = input("Description ?")
        self.recipe_type = input("Recipe type ?")
        print("Recipe added.")

    def __str__ (self):
        txt = "Name : " + self.name
        txt += "\nCooking level : " + str(self.cooking_lvl)
        txt += "\nCooking time : " + str(self.cooking_time)
        txt += "\nDescription : " + self.description
        txt += "\nRecipe type : " + self.recipe_type
        txt += "\nIngredients : " + "".join(self.ingredients) + ".\n"
        return txt