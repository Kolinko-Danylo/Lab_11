from task_2.arrays import Array2D

class BlankImage:
    """Represent Image ADT"""
    def __init__(self, rows, cols):
        self._array = Array2D(rows, cols)

    def width(self):
        "Return width of the image"
        return self._array.num_rows()

    def height(self):
        "Return height of the image"
        return self._array.num_cols()

    def clear(self, value=0):
        "Set all pixels with the same number"
        self._array.clear(value)

    def __getitem__(self, tuple):
        """ Return element with given coordinates """
        return self._array[tuple]

    def __setitem__(self, tuple, value):
        """ Set new walue to the cell in the matrix. """
        if value not in range(256):
            raise ValueError

        self._array[tuple] = value

