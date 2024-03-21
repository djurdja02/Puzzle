Pyzzle is a graphical simulation written in the Python programming language, which demonstrates the operation of basic search algorithms on the k-Puzzle game problem. 
The game consists of a square matrix of tiles labeled from 1 to k, along with one blank space labeled as 0. The objective of the game is to rearrange the order of the tiles by moving them horizontally or vertically across the blank space, so that they form a matrix with tiles in ascending order.
The program is executed from the terminal by using the following command:
.\main.py size image algorithm heuristic
By pressing the SPACE button, it is possible to start or temporarily pause the display of the solution. Pressing the ENTER button allows displaying the final solution.
Pressing the ESC button terminates the application's operation and closes its main window.
Implemented algorithms:
Implemented algorithms:
- Breadth-First Search.
- Best-First Search: In case there are two or more nodes with equal heuristic function values, such nodes are sorted based on the increasing value of the node's identification label.
- A* Algorithm: If there are two or more partial paths with the same estimated function value, such partial paths are sorted based on the increasing value of the identification label of the last node on the path.

Implemented heuristics:
- Hamming: The number of tiles that are not in their corresponding target positions.
- Manhattan: The sum of Manhattan distances of each tile to its corresponding target position.
