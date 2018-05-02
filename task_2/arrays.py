import ctypes


# Implements the Array ADT using array capabilities of the ctypes module.

class Array:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__(self):
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

class Array2D:
    """Represents 2-dimmensional array."""
    def __init__(self, numRows, numCols):
        self._rows = Array(numRows)
        for i in range(numRows):
            self._rows[i] = Array(numCols)

    def num_rows(self):
        "Return number of rows."
        return len(self._rows)

    def num_cols(self):
        "Return number of columns."
        return len(self._rows[0])

    def clear(self, value):
        "Clear the array"
        for i in range(self.num_rows()):
            self._rows[i].clear(value)

    def __getitem__(self, ind_tuple):
        assert len(ind_tuple) == 2, "Wrong number of indices"
        assert ind_tuple[0] in range(self.num_rows()), "Rows number is out of the range"
        assert ind_tuple[1] in range(self.num_cols()), "Columns number is out of the range"
        return self._rows[ind_tuple[0]][ind_tuple[1]]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, ind_tuple, value):
        assert len(ind_tuple) == 2, "Wrong number of indices"
        assert ind_tuple[0] in range(self.num_rows()), "Rows number is out of the range"
        assert ind_tuple[1] in range(self.num_cols()), "Columns number is out of the range"
        self._rows[ind_tuple[0]][ind_tuple[1]] = value
