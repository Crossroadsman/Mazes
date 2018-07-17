class Cell():
    def __init__(row, column):
         self.row = row
         self.column = column

         self.north = None
         self.east = None
         self.south = None
         self.west = None

         self.links = {}

    def set_link(cell, status, bidirectional=True):
        """Connects (sets True) or disconnects (removes entry) the Cells `self` 
        and `cell`.
        
        If `bidirectional` is True, also sets the corresponding property on
        `cell`.
        """
        valid_statuses = [True, False]
        if status not in valid_statuses:
            raise ValueError("`status` parameter must be one of: {}".format(valid_statuses))
        if status:
            self.links[cell] = status
        else:
            self.links.pop(cell, False)
            
        if bidirectional:
            cell.set_link(self, status, bidirectional=False)
         
    def get_links():
        """Returns a list of connected cells"""
        return self.links.keys()
    
    def is_linked(cell):
        """Returns True if a specified cell is connected, False otherwise"""
        return self.links.get(cell, False)

    def get_neighbours():
        """Returns the neighbour Cells of a Cell. None if there is no
        corresponding neighbour
        """
        neighbours = []
        for direction in [self.north, self.east, self.south, self.west]:
            if direction:
                neighbours.append(direction)
            else:
                neighbours.append(None)
        return neighbours
