
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # SelectAndMoveFromOpenList()
        if len(self.open_list) == 0:
            return next_soln
        # my_index ← GetLastIndex(open_list)
        my_index = len(self.open_list) - 1

        # the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)


        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if len(self.open_list) == 0:
            return next_soln
        # SelectAndMoveFromOpenList()
        # my_index ← GetFirstIndex(open_list)
        my_index = 0

        # the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)

        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # Find the index of the candidate with the best quality in the openlist
        if self.open_list:
            best_quality = self.open_list[0].quality
            best_index = 0
            for i, candidate in enumerate(self.open_list):
                if candidate.quality < best_quality:
                    best_quality = candidate.quality
                    best_index = i

            # Remove the candidate with the best quality from the openlist
            next_soln = self.open_list.pop(best_index)


        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if len(self.open_list) == 0:
            return next_soln

        # Find solution with minimum f(n) = g(n) + h(n)
        min_score = float('inf')
        min_index = 0

        for i, solution in enumerate(self.open_list):
            # Calculate f(n) = g(n) + h(n)
            # Using len(solution.variable_values) for path length and solution.quality for heuristic
            f_score = len(solution.variable_values) + solution.quality
            if f_score < min_score:
                min_score = f_score
                min_index = i

        # Get solution with minimum score and remove from openlist
        next_soln = self.open_list.pop(min_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    # Create maze that breaks depth-first search
    maze = Maze(mazefile="maze.txt")

    # Create a very deep path that leads to a dead end
    # This will cause DFS to waste all its trials exploring this path
    for i in range(2, 19):
        maze.contents[i][10] = hole_colour  # Create a long vertical path downward

    # Make the goal unreachable via the deep path
    maze.contents[19][10] = wall_colour  # Block the path at the bottom

    # Create an alternative longer path that leads to the goal
    for i in range(11, 19):
        maze.contents[2][i] = hole_colour  # Horizontal path

    for i in range(3, 19):
        maze.contents[i][19] = hole_colour  # Vertical path on the right side

    # Create path to goal
    maze.contents[19][11] = hole_colour
    maze.contents[19][12] = hole_colour
    maze.contents[20][12] = hole_colour

    # Save maze to file
    maze.save_to_txt("maze-breaks-depth.txt")

    # <==== insert your code above here

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    # Create maze where depth-first is more efficient
    maze = Maze(mazefile="maze.txt")

    # Create a direct path to the goal
    # Position the path so it aligns with depth-first search's preference
    # for exploring certain directions first

    # Clear existing obstacles near the start
    for i in range(5):
        for j in range(9, 15):
            if i > 0:  # Don't modify the top wall
                maze.contents[i][j] = hole_colour

    # Create a path that depth-first will find quickly
    # This assumes depth-first prioritizes going down and right
    for i in range(1, 21):
        maze.contents[i][11] = hole_colour  # Create a direct vertical path

    # Add some extra paths that will distract breadth-first
    # but won't affect depth-first as much
    for i in range(12, 25):
        if j < maze.width:  # Ensure we don't go out of bounds
            maze.contents[3][j] = hole_colour  # Horizontal path
            maze.contents[10][j] = hole_colour  # Another horizontal path

    for i in range(3, 10):
        maze.contents[i][15] = hole_colour  # Vertical connector
        maze.contents[i][20] = hole_colour  # Another vertical connector

    # Save maze to file
    maze.save_to_txt("maze-depth-better.txt")


    # <==== insert your code above here
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    # Create maze that breaks depth-first search
    maze = Maze(mazefile="maze.txt")
    maze.contents[2][10] = hole_colour
    maze.save_to_txt("maze-breaks-depthfirst.txt")

    # <==== insert your code above here

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    # Create maze where depth-first is more efficient
    maze = Maze(mazefile="maze.txt")

    # Create a hole in the wall, one place to the right of the entrance, three blocks down
    maze.contents[2][10] = hole_colour
    maze.save_to_txt("maze-depth-better.txt")


    # <==== insert your code above here
