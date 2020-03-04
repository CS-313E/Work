# Work
Vyasa has to complete a programming assignment overnight. He has to write n lines of code before morning. He is dead tired and he tries drinking some black coffee to keep him awake. But each time he drinks a cup of coffee he stays awake for a short amount of time but his productivity goes down by a constant factor k

This is how he plans to write the program. He will write the first v lines of code, then drink his first cup of coffee. Since his productivity has gone down by a factor of k he will write v // k lines of code. He will have another cup of coffee and then write v // k**2 lines of code. He will have another cup of coffee and write v // k**3 lines of code and so on. He will collapse and fall asleep when v // k ** p becomes 0.

Now Vyasa does want to complete his assignment and maximize on his sleep. So he wants to figure out the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code before he falls asleep.

Your input file will be called work.txt. Here is a typical file:

2
300 2
59 9
The first line is T the number of test cases. This will be followed by T lines of input. Each line of input will have two numbers n and k. n is the number of lines of code to write and k is the productivity factor, where 1 ≤ n ≤ 106 and 2 ≤ k ≤ 10.
For each test case your output to the screen will be v lines of code the Vyasa has to write, as well as the time it took for each function. For the above two test cases, the output will be:

Binary Search: 152
Time: 9.512901306152344e-05

Linear Search: 152
Time: 0.0005910396575927734


Binary Search: 54
Time: 4.696846008300781e-05

Linear Search: 54
Time: 9.012222290039062e-05
