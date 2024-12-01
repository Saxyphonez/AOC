from enum import Enum

class FileType(Enum):
    SPACE = 0
    REALFILE = 1


class File():
    
    def __init__(self, size, head, tail, id = None, type = FileType.SPACE):
        
        self.id = id
        self.filesize = size
        self.type = type

        self.head = head
        self.tail = tail

        if(self.type == FileType.SPACE):
            self.text = '.'
        
        else:
            self.text = str(id)


    def __repr__(self):
        
        if(self.type == FileType.SPACE):
            return "<{}: addr{}->{} ({})>\r\n".format(self.type.name, self.head, 
                                               self.tail, self.filesize)
        
        else:
            return "<ID{}: addr{}->{} ({})>\r\n".format(self.id, self.head, 
                                                 self.tail, self.filesize)


    def __str__(self):
        
        return self.__repr__()
    

class Drive():
    def __init__(self):
        
        self.files = []

        self.largestSpace = 0
        self.ptr_largestSpace = 0
        self.spaceAddressTable = {}
        self.spaceIDCounter = 0
        
        self.addressTable = {}
        self.largestID = 0


    def addFile(self, file):
        """
        Adds a File object to the list of files.
        If the File is a space, and the size is larger than the current
        largest, set the largest space variables to the new File
        """

        self.files.append(file)

        if(file.type == FileType.SPACE):
            self.spaceAddressTable[self.spaceIDCounter] = len(self.files)-1
            self.spaceIDCounter += 1

            if(file.filesize >  self.largestSpace):
                self.largestSpace = file.filesize
                self.ptr_largestSpace = file.head
        else:
            self.addressTable[file.id] = len(self.files)-1
            self.largestID += 1


    def attemptMove(self, ):
        """
        
        """
        # Check ID of file size against size of largest space to the "left"
        
        # If none big enough
            # return 0 #ie could not swap
        # If big enough, do the swap
            # update head and tail pointer for file
            # update addressTable for file 

            # update head and tail pointer for the space
            # update addressTable for space 

            # go through the drive and find the location of the largest space
            # that is to the "left" of the space just moved # #clever ;)


            #return 1


        pass


    def moveFileToSpace(self, file, space):

        #perform the move

        pass



    def __repr__(self):
        
        return self.files


    def __str__(self):
        
        return self.__repr__()