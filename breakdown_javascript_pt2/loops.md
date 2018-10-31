## Loops in JS 


## What is a for loop?

A **for loop** goes through a block of code over and over again. 

For example:

		for (var i = 0; i < 5; i++){
			console.log(i);
		}

`var i = 0` sets a variable before the loops starts. This variable will always start with `i`.
`i < 5` definies the condition for the loop to run. (Ex: i must be less than 5).
`i++` increases the value of i + 1 each time the code block in the loop has been executed. 

In this example, the loop will only run 4 times because **i must be less than 5** . 
`console.log(i)` will print the following: 
	
	0
	1
	2
	3
	4
	


## What is a while loop?  

A **while loop** is similar but instead it loops through a block of code while a specified condition is **true**. For example: 
	
	var i = 0;
	 while (i < 5){
		console.log(i);
	}
	
This can be viewed as while `i < 5` print that number to the console.

while `0 < 5 ` print `0` to the console (true)
while `1 < 5 ` print `1` to the console (true)
while `2 < 5 ` print `2` to the console (true)
while `3 < 5 ` print `3` to the console (true)
while `4 < 5 ` print `4` to the console (true)

All of these statments are true so we are telling the computer to print out the following: 

	0
	1
	2
	3
	4


**5** will never be printed because that condition is **false**. 5 cannot be less than 5. 

## How can we stop a for loop? 

To stop a for or while loop you can easily do so by using the `return` statement. As we mentioned earlier, functions will completey stop what it is doing and immediately return back to you the value that you wanted. 


## Why is it useful? 
For loops are useful in JavaScript because it allows computers to perform a particular task repeatedly until no action is required. It reduces the amount of time spent in order for a computer to perform a task in a matter of seconds which makes it more efficient and effective in the programming world. 






















