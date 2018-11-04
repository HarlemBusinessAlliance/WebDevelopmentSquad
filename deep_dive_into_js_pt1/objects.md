# Understanding JavaScript Objects

## Goal

Alongside arrays, you will learn and understand how to use the next JavaScript data structure which is **Objects** that will also allow you to store complex data in your programs.


## What is an Object?  
Objects behave just like an array where it allows you to store multiple values inside of a named variable. These named variables are known as the object's properities. 


For example: It is similar to the way you write code inside of your CSS. In CSS, you targeted a certain HTML element where you have written some type of information about how you wanted this element to behave or be styled. 

Now instead of targeting an specific HTML element, we are now declaring a variable which is set to an object that will hold some type of information about something. 

		`var person = {

			firstname: 'Ashley', 
			lastname: 'Carter', 
			age: 28, 
			hometown: 'Los Angeles'
		}; 

Note: `firstname` is the property's **name** and `Ashley` is the property's **value.** If you have multiple properties within an object it is also seperated by a comma. 

## How do we create an Object?  

**Syntax for creating an Object:** 

	`var` `objectNameGoesHere` `=``{
				`propertyName' `:` `propertyValue`
			};`

## How can we have access to certain elements within an Object?  

You can access information within an Object similarly to the way you would do it with an Array. There are **two** way for you to do with Object which is by using the **dot notation** or **bracketing into the object** just like we did with the array. 

For example: 

		`var fruits = {
			type1: 'bananas',
			type2: 'apples',
			type3: 'oranges', 
			type4: 'pineapples', 
			type5: 'grapes'
		};

If I wanted to get `oranges` I could either do this: `fruits.type3` which will give me `apples`
OR I could do `fruits["type3"]` which will also give me `apples`. 

The syntax to access a certain value will always be `objectName.propertyName` or `objectName["propertyName"]` 

## Why are Objects Useful in JS? 

Similar to Arrays, Objects does an excellent job with allowing you to have an easier,faster and more cleaner way of accessing some type of data. It also improves the way your code's data is being represented. In JavaScript you will always find yourself interacting with some type of data that you will eventually need to use when building out your own programs. 



