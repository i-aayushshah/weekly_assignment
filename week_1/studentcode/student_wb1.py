from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()

    # ====> insert your code below here
    for digit1 in puzzle.value_set:
        for digit2 in puzzle.value_set:
            for digit3 in puzzle.value_set:
                for digit4 in puzzle.value_set:
                    # Set the current combination
                    my_attempt.variable_values = [digit1, digit2, digit3, digit4]

                    try:
                        # Evaluate if this combination is correct
                        result = puzzle.evaluate(my_attempt.variable_values)

                        # If result is 1, we found the correct combination
                        if result == 1:
                            return my_attempt.variable_values
                    except ValueError:
                        # Skip invalid combinations
                        continue

    # <==== insert your code above here

    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    for name in namearray:
        family_names.append(name[-6:])
        return family_names


    # <==== insert your code above here
    return family_names

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    for name in namearray:
        family_names.append(name[-6:])
        return family_names


    # <==== insert your code above here
    return family_names

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    for i in range(namearray.shape[0]):
        # Extract the last 6 characters for each name (family name)
        family_name_chars = namearray[i, -6:]
        # Join the characters to form a string
        family_name = ''.join(family_name_chars)
        # Add it to our list
        family_names.append(family_name)
    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays

    # ====> insert your code below here

    # Use assertions to check that the array has 2 dimensions each of size 9
    assert attempt.ndim == 2, "Input must be a 2D array"
    assert attempt.shape[0] == 9, "Array must have 9 rows"
    assert attempt.shape[1] == 9, "Array must have 9 columns"

    # Add all rows to the slices list
    for i in range(9):
        row = attempt[i, :]
        slices.append(row)

    # Add all columns to the slices list
    for j in range(9):
        col = attempt[:, j]
        slices.append(col)

    # Add all 3x3 sub-squares to the slices list
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = attempt[i:i+3, j:j+3].flatten()  # Flatten to 1D array
            slices.append(square)

    for slice in slices:  # easiest way to iterate over list
        # Get number of unique values in slice
        unique_values = np.unique(slice)

        # If there are exactly 9 unique values, increment tests_passed
        if len(unique_values) == 9:
            tests_passed += 1

    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
