class BinaryTreeMaze():
    """Binary Tree
       ===========
    This is a very simple and fast (O(n)) method for creating a perfect maze.
    However, it has some very serious biases that affect the texture of the map:
    - the north edge and east edge are corridors
    """

    # Set the size of the grid
    # ------------------------
    # Set the start point
    # -------------------
    def __init__(width, height, start_corner):
        """width is the number of units wide that the maze is,
        height is the number of units wide that the maze is,
        start_corner is the starting corner for carving the route.
        Valid start_corner choices are ('nw','ne','sw','se')
        """
        self.width = width
        self.height = height
        valid_corners = ['nw','ne','sw','se']
        if start_corner not in valid_corners:
            error_text = "start_corner value must be one of the following: {}"
            raise ValueError(error_text.format(valid_corners))
        self.start_corner = start_corner

    # Carve the route
    # ---------------
