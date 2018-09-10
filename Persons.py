# ------------Persons.py Module ---------------#
# Desc:  Classes that hold Personal data
# Dev:   RRoot
# Date:  12/12/2020
# ChangeLog:(When,Who,What)
# ---------------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


# --- Make the class ---
class Person(object):
    """ Base Class for Personal data """
    # -------------------------------------#
    # Desc:  Holds Personal data
    # Dev:   RRoot
    # Date:  12/12/2020
    # ChangeLog:(When,Who,What)
    # -------------------------------------#

    # --Fields--
    __Counter = 0  # Hey Devs, please consider this a private class field. Thx!

    # --Constructor--
    def __init__(self,FirstName=""):
        # Attributes
        self.__FirstName = FirstName  # Private Attribute
        Person.__SetObjectCount()  # Private Method

    def __init__(self,LasttName=""):
        # Attributes
        self.__LastName = LasttName  # Private Attribute
        Person.__SetObjectCount()  # Private Method

    # --Properties--
    # FirstName
    @property  # getter(accessor)
    def FirstName(self):
        return self.__FirstName

    # LastName
    @property  # getter(accessor)
    def LastName(self):
        return self.__LastName

    @FirstName.setter  # (mutator)
    def FirstName(self, Value):
        self.__FirstName = Value

    @LastName.setter  # (mutator)
    def LastName(self, Value):
        self.__LastName = Value

    # --Methods--
    def ToString(self):
        """Explictly returns field data"""
        return self.FirstName

    def ToString(self):
        """Explictly returns field data"""
        return self.LastName

    def __str__(self):
        """Implictly returns field data"""
        return self.FirstName

    def __str__(self):
        """Implictly returns field data"""
        return self.LastName

    @staticmethod
    def GetObjectCount():  # You do not need the self keyword
        return Person.__Counter

    @staticmethod
    def __SetObjectCount():  # This is a private and static method
        Person.__Counter += 1

    # --End of class Person--
