# Sudoku
A python program works to create a random sudoko then try to solve it
The program will create a "seed" as beginning of a suduko, then do some random exchange between numbers, rows, columns to make this suduko be a new one.
Then, program still do some random selection to delete some cells of this sudoko. The number of cells deleted can be entered at the begeinning of the programm.
At last, program will try to solve the suduko problem shows above. Attention: if blank cells are many, it may finished by another result.

About algorithm
------------------
How does program solve a sudoko problem created by itself?
First, it will count the number of blanks in whole suduko, then solve them one by one.
Second, every steps, the program will find the cell which has the minimum solutions.
Third, the program will try to fill a possible number , then call itself (recursion), till it returns a "True" value which menas the way fill up all blanks. If this possible number get all "False" return, program will try another possible number, then do it again.

Advantages
---------
Before I add function "Find minimum solutions" in , the program solve each cells from start to end, which is inefficient. Because the characteristics of recursion show that a number of trys at beginning will cause much more calculation than a number of trys at last, for each step of recursion will times the number of calculation. So put as much as possible trys at last will help program run quickly.
In fact, this kind of method is not an improvement, it is the key to help program work when blanks are over 40, or too many calculation will cost several months to finish this problem. (I promise your brain is faster than it) So, the most important things for an argorithm is to make sure it will solve problem by correct method in acceptable time.
