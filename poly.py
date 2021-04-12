class India():
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

    def type(self):
        print("India is a country.")


class USA():
    def capital(self):
        print("Washington")

    def language(self):
        print("English")

    def type(self):
        print("USA is a country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()