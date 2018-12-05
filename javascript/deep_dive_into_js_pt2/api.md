API stands for Application Program Interface, which can be defined as a set of methods of communication between various software components. In other words, an API allows software to communicate with another software.

	// JSON tut
	var myJSON = '{"name":"John", "age":31, "city":"New York"}';
	var myObj = JSON.parse(myJSON);
	console.log(myObj.name);

	//Storing data:
	myObj = {name: "John", age: 31, city: "New York"};
	myJSON = JSON.stringify(myObj);
	localStorage.setItem("testJSON", myJSON);

	//Retrieving data:
	text = localStorage.getItem("testJSON");
	obj = JSON.parse(text);
	console.log(obj.name);





	// Outside the JS context, when you receive the response the JSON-structured object looks like this
	{"employees":[
	    { "firstName":"John", "lastName":"Doe" },
	    { "firstName":"Anna", "lastName":"Smith" },
	    { "firstName":"Peter", "lastName":"Jones" }
	]}








	// From the tut https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/
	var request = new XMLHttpRequest();

	request.open('GET', 'https://ghibliapi.herokuapp.com/films', true);
	request.onload = function () {
	  alert(this.response);
	  }

	request.send(null);





We’re going to use JSON.parse() to parse the response, and create a data variable that contains all the JSON as an array of JavaScript objects. Using forEach(), we’ll console log out the title of each film to ensure it’s working properly.

References
https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/

