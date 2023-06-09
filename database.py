import pymssql


class Database:
    __connection = None

    @classmethod
    def __connect(cls):
        if cls.__connection is None:
            cls.__connection = pymssql.connect(server='cisdbss.pcc.edu',
                                               user='275student',
                                               password='275student',
                                               database='NAMES')

    @classmethod
    def readNames(cls):

        lstNames = []

        if (cls.__connection is None):
            cls.__connect()

        myCursor = cls.__connection.cursor()
        myCursor.execute(
            "SELECT top 100 ID,Name,Gender,Year,NameCount FROM all_data;")

        myRows = myCursor.fetchall()

        # loop one Row at a time and print the entire row (All Fields\Columns)
        for r in myRows:
            lstNames.append(
                {"Name": r[1], "Gender": r[2], "Year": r[3], "Births": r[4]})

        return lstNames

        ##################################################

    @staticmethod
    def readNamesStatic():

        lstNames = []

        if (Database.__connection is None):
            Database.__connect()

        myCursor = Database.__connection.cursor()
        myCursor.execute("SELECT * FROM Names;")

        myRows = myCursor.fetchall()

        # loop one Row at a time and print the entire row (All Fields\Columns)
        for r in myRows:
            lstNames.append(
                {"Name": r[1], "Gender": r[2], "Year": r[3], "Births": r[4]})

        return lstNames

        ########################################################

    @classmethod
    def readNamesByNameAndGender(cls, Name, Gender):

        lstNames = []

        if (cls.__connection is None):
            cls.__connect()

        myCursor = cls.__connection.cursor()
        myCursor.execute(
            "SELECT Top 50 ID,Name,Gender,Year,NameCount FROM all_data WHERE "
            "Name=%s AND Gender=%s",
            (Name, Gender))

        myRows = myCursor.fetchall()

        # loop one Row at a time and print the entire row (All Fields\Columns)
        for r in myRows:
            print(r[0])
            lstNames.append(
                {"Name": r[1], "Gender": r[2], "Year": r[3], "Births": r[4]})

        return lstNames

    @classmethod
    def readNames_OLD(cls):

        lstNames = [
            {"Name": "Bob", "Gender": "M", "Year": "1907", "Births": 34000},
            {"Name": "Tom", "Gender": "M", "Year": "1907", "Births": 17800},
            {"Name": "Liz", "Gender": "F", "Year": "1907", "Births": 54557},
            {"Name": "Ed", "Gender": "M", "Year": "1907", "Births": 67129},
            {"Name": "Sue", "Gender": "F", "Year": "1907", "Births": 11788},
        ]

        return lstNames
