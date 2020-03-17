#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KRos, 2020-Mar-14, added constructors, properties and methods to CD Class
# KRos, 2020-Mar-15, added in save_inventory and load_inventory
# KRos, 2020-Mar-16, added in menu options, updated save and load functions
# KRos, 2020-Mar-16, updated docstrings
# KRos, 2020-Mar-16, added a show_inventory call into the add cd option
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        formatted: (string) returns a formatted string of the cd infomation
        saveFormat: (string) returns a formatted string for saving to a file
        __str__: returns formatted
    """

    # -- CONSTRUCTOR -- #
    def __init__(self, cd_id=1, cd_title='title', cd_artist='artist'):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    # -- ATTRIBUTES -- #
    # -- PROPERTIES -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, idno):
        if idno.isnumeric():
            self.__cd_id = int(idno)
        else:
            raise Exception("IDs can only be numeric")
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title):
        if title ==  "":
            raise Exception("CD title cannot be empty")
        else:
            self.__cd_title = title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, artist):
        if artist == "":
            raise Exception("CD artist cannot be empty")
        else:
            self.__cd_artist = artist
    # -- METHODS -- #
    def formatted(self):
        return '{}\t{} by: {}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    def saveFormat(self):
        return '{},{},{}\n'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    def __str__(self):
        return self.formatted()

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def load_inventory(file_name, table):
        """Function that reads data from a file and saves to 2D table
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of obj): 2D data structure that holds the data during runtime
        Returns:
            table (list of obj): 2D data structure after loading data from file
            
        """
        try:
            with open(file_name, 'r') as objFile:
                for line in objFile:
                    data = line.strip().split(',')
                    cd = CD(int(data[0]),data[1],data[2])
                    table.append(cd)
            print("{} successfully loaded!".format(file_name))
        except FileNotFoundError:
            print("Could not load {}".format(file_name))
        return table


    @staticmethod
    def save_inventory(file_name, table):
        """Function that saves inventory to text file
        
        Args:
            file_name (string): name of file used to save data to
            table (list of obj): 2D data structre that holds data during runtime
        Returns:
            
        """
        with open(file_name, 'w') as objFile:
            for cd in table:
                objFile.write(cd.saveFormat())
        return table


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handles User inputs and outputs"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.
            
        Returns:
            None.
        """
        
        print('Menu: \n\n[1] Load Inventory from File\n[2] Add CD\n[3] Display Current Inventory')
        print('[4] Delete CD from Inventory\n[5] Save Inventory to file\n[0] Exit Program\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        
        Args:
            None
        
        Returns:
            choice (string): a string of the users input out of the choices 0 through 5
        
        """
        choice = ''
        while choice not in ['0', '1', '2',  '3', '4', '5']:
            choice = input('Please select an option number: ').strip()
        print() #formatting
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        
        Args:
            table (list of obj): 2D data structure that holds the data during runtime
        
        Returns:
            None
        
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title by: Artist\n')
        for cd in table:
            print(cd)

        print('======================================')

    @staticmethod
    def input_CD():
        """Asks user for CD inputs
        
        Args:
            None
        
        Returns:
            ID, Title, Artist
        
        """
        try:
            ID = input('Enter ID: ').strip()
            Title = input('What is the CD\'s title? ').strip()
            Artist = input('What is the Artist\'s name? ').strip()
            return ID, Title, Artist
        except ValueError:
            print('ID should be an integer.')
    
    @staticmethod
    def delete_CD(idno, table):
        """Function that removes a CD from table
        
        Args:
            idno (int): CD ID number to be deleted
            table (list of Obj): 2D list of objects that CD should be removed from
            
        Returns:
            table (list of Obj): edted 2D list
        """
        intRowNr = -1
        blnCDRemoved = False
        for cd in table:
            intRowNr += 1
            if cd.cd_id == idno:
                del table[intRowNr]
                blnCDRemoved= True
                break
        if blnCDRemoved:
            print('The CD was removed.')
        else:
            print('Coud not find CD!')
        return table


# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
# Display menu to user
while True:

    IO.print_menu()
    strChoice = IO.menu_choice()


    # let user load inventory from file
    if strChoice == '1':
        print("WARNING: This will clear current inventory.")
        strYesNo = input("Type 'yes' to continue. ")
        if strYesNo.lower() == 'yes':
            lstOfCDObjects = [] # clears table
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
        else:
            print("Inventory not reloaded")
        continue
    # let user add cd to inventory
    elif strChoice == '2':
        new_id, new_title, new_artist = IO.input_CD()
        newCD = CD()
        try:
            newCD.cd_id = new_id
            newCD.cd_title = new_title
            newCD.cd_artist = new_artist
            lstOfCDObjects.append(newCD)
        except Exception as e:
            print(e)

        IO.show_inventory(lstOfCDObjects)
        continue
    #display inventory
    elif strChoice == '3':
        IO.show_inventory(lstOfCDObjects)
        continue
    #added delete CD option
    elif strChoice == '4':
        try:
            del_ID = int(input('Which ID would you like to delete? ').strip())
            IO.delete_CD(del_ID, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        except ValueError:
            print("Expected an ID number.")
        continue
    # let user save inventory to file
    elif strChoice == '5':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('File saved!')
        else:
            print('File was not saved!')
        continue
    else:
        print('Exiting program.')
        break
