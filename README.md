# a_star-algoithm
An example of an a star algorithm being used to solve both eight tile puzzle and a sliding puzzle games

Program output example

These examples are hard to read and should be cleaned up however have still been provided to help ilistrate the output of the project

8 tile puzzle example
	Initial configuration
	2 8 3
	1 6 4
	7 0 5
	Goal configuration 
	1 2 3
	8 0 4
	7 6 5
	Output:
	Printing path
0  depth --  6  f
2 ,  8 ,  3
1 ,  6 ,  4
7 ,  0 ,  5
1  depth --  5  f
2 ,  8 ,  3
1 ,  0 ,  4
7 ,  6 ,  5
2  depth --  6  f
2 ,  0 ,  3
1 ,  8 ,  4
7 ,  6 ,  5
3  depth --  7  f
0 ,  2 ,  3
1 ,  8 ,  4
7 ,  6 ,  5
4  depth --  6  f
1 ,  2 ,  3
0 ,  8 ,  4
7 ,  6 ,  5
5  depth --  5  f
1 ,  2 ,  3
8 ,  0 ,  4
7 ,  6 ,  5
Sliding puzzle example
	Initial input
	B, B, B, -, W, W, W
	Output:
	Printing path
0  depth --  9  f
['B', 'B', 'B', '-', 'W', 'W', 'W']
1  depth --  10  f
['B', '-', 'B', 'B', 'W', 'W', 'W']
3  depth --  10  f
['B', 'W', 'B', 'B', '-', 'W', 'W']
4  depth --  11  f
['B', 'W', 'B', 'B', 'W', 'W', '-']
6  depth --  11  f
['B', 'W', 'B', '-', 'W', 'W', 'B']
7  depth --  12  f
['B', 'W', 'B', 'W', '-', 'W', 'B']
8  depth --  12  f
['B', 'W', '-', 'W', 'B', 'W', 'B']
9  depth --  12  f
['-', 'W', 'B', 'W', 'B', 'W', 'B']
11  depth --  13  f
['W', 'W', 'B', '-', 'B', 'W', 'B']
12  depth --  13  f
['W', 'W', 'B', 'W', 'B', '-', 'B']
14  depth --  14  f
['W', 'W', '-', 'W', 'B', 'B', 'B']
