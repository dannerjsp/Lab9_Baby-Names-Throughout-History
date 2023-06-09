from database import Database


class Name:

    # Constructor method
    def __init__(self, name, gender, year, births):
        self.__name = name
        self.__gender = gender
        self.__year = year
        self.__births = births

    # Accessor methods (the getters). Allows you to read/access the data.
    @property
    def Name(self):
        return self.__name

    @property
    def Gender(self):
        return self.__gender

    @property
    def Year(self):
        return self.__year

    @property
    def Births(self):
        return int(self.__births)



    @classmethod
    def get_names(cls):

        list_return = []

        names_list = Database.read_names()

        for l in names_list:
            new_name = Name(l['Name'], l['Gender'], l['Year'], l['Births'])
            list_return.append(new_name)

        return list_return

    @classmethod
    def getNamesByNameAndGender(cls, the_name, the_year):
        lst_return = []

        lst_names = Database.readNamesByNameAndGender(the_name, the_year)

        for l in lst_names:
            new_name = Name(l['Name'], l['Gender'], l['Year'], l['Births'])
            lst_return.append(new_name)

        return lst_return
