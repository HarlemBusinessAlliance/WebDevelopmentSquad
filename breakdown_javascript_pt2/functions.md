## The Breakdown of Functions in JS 


## What is a function?

A **function** is a *subprogram* designed to perform a particular task. Functions are executed when they are called which is known as *invoking* a function. Values can be **passed** into functions and used within the function. Functions always `return` a value. In JavaScript, if no `return` value is specified, the function will return `undefined`. 



## How do we define a function in JS? 

In **JavaScript** we define a **function** by writing the function keyword followed by the name of the function. For example: 

	 	function name(parameters){
		
			//statements goes here...
		}

`function` is a keyword that declares a new function. 
`name` can be anything that you want your function to be called.
`parameters` are placeholders for the value(s) that you are passing through the function as "inputs"
`statements` are the instructions that you want your function to follow and  that will execute the desired "output" that you want to recieve. 


## What are parameters? 
**Parameters** are used when defining a function, they are names created in the function definition. Parameters are always separated by commas in the `( )` parenthesis. 

For Example: 

		 function example(num1,num2){
			return num1 + num2; 
		}
		

## What is the difference between using console.log and return? 


**console.log** - is only used to print out information in the console of your browser. It is a great tool to use for when you are debugging your code.  

**return** - is a statement that will make the function stop immediately and execute back the specified value. 



## What does it mean to callback your function? 

When progamming you always want to make sure that you declare your function and after you write some statements inside of the body of the function you want to call back your function at the end of it. 

For example: 

Here I am declaring my function called aboutMe: 

		function aboutMe(name){
			return 'Hello My Name Is' + '' + name;
		}


Now I am going to callback my function called `aboutMe`. 
		
		aboutMe('Tionna'); 
		

The expected outcome should be `Hello My Name Is Tionna`. If you do not call your function at the end, the computer will throw you an error of `undefined`. 


























