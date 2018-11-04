# Understanding JavaScript Arrays 

## Goal

To learn and understand how to use arrays to store complex data in your JavaScript programs. Arrays have different types of built-in methods just like Strings that will allow you to manipulate different values . 


## What is an Array?  
An array in JavaScript allows you to store multiple values in a single variable. These values can be different types of elements such as a string, number, object, an array itself, and more.   

For example: If you wanted to store a list of supplies into a single variable, instead of doing the following, you can simply create an array to hold these multiple values all at once. 

		`var supplies1 = 'pens';`
		`var supples2 = 'notebooks;'`
		`var supplies3 = 'binder';`
		`var supplies4 = 'calculator';`


		`var supplies = ['pens', 'notebooks', 'binder', 'calculator'];`

Note: Each element within an array is seperated by a comma. 

## How do we create an Array?  

**Syntax for an Array:** 

	`var` `arrayNameGoesHere` `=` `[ `item1`, `item2`, ...]` `;`



Another way to create it in JavaScript is by declaring the `Array` which is a keyword that can be used to create a new one. For example: 

	`var thingsToDo = new Array('study', 'attend js workshop', 'buy groceries');`

This does the exact same thing the example before it. 


## How can we have access to certain elements within an Array?  

Anytime you are working with elements inside an array, each element has its own index/position that it stands in. The index/position in an array will always start at `0`. For example if I wanted to get `apples` out of this array I can pull it out by specifying it's index/position of `3`.


		`var fruits = ['bananas', 'oranges', 'pineapples', 'apples', 'grapes'];` 
		`bananas = 0;`
		`oranges = 1;`
		`pineapples = 3;`
		`apples = 4;`
		`grapes = 5;`

		`console.log(fruits[3]) --> 'apples';`


I am calling the name of the array which is `fruits` and bracketing into it by passing in the index of `3` which will pull out the value of `apples`. 


## Why are Arrays Useful in JS? 

Arrays are useful in JavaScript because it gives you a more cleaner, faster and efficient way of accessing some type of data. With arrays you have the ability to go through this list of data by using a `for loop` in order to maniuplate or use the data in a way that may work best for the program that you are building. 






