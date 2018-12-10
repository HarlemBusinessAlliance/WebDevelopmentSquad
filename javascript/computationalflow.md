## Computational flow
Let's think about computational flow in a stack form

function double(x) { 
	return 2 * x; 
}

function squareAndAddFive(y) { 
	return square(y) + 5; 
}

function square(z) { 
	return z * z; 
}

function maths(num) {
    var answer = double(num);
    answer = squareAndAddFive(answer);
    return answer;
}

maths(5);
    
---

The four initial functions are made by the programmer before any calculations are made. The functions are just "there", waiting to be used... Standing at attention so to speak. Now, at the end of this program there is a function call. THIS ONE CALL will activate ALL of the functions in our program!

1) maths is a) called and b) given a parameter value of 5
2) The maths computational block is retrieved, and run line by line: A variable is created, ... 
3) The double computational block is retrieved, and run line by line: 2 times the parameter value (5) is calculated and then returned

-> maths is called; JS pushes maths call on its call stack
-> inside maths, double is called; JS pushes double onto its call stack
-> doubles completes, returns value 10; JS pops double off its call stack
-> back inside maths, squareAndAddFive is called;
   JS pushes squareAndAddFive on its call stack
-> inside squareAndAddFive, square is called;
   JS pushes square on its call stack

Let's look at call stack right now

square
squareAndAddFive
maths
main

-> square completes, returns 100
-> squareAndAddFive completes, returns 105
-> maths completes, returns 105
