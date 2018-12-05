Let's look some more at the following HTTP request methods for connecting to an Application Programming Interface through JavaScript:

Before you use the request methods below, see if you can retrieve a response through the browser itself. Just enter the completely-formed API url with endpoint, wanted queries, credentials, everything. Got some data back? You're WINNING!

---

### XMLHttpRequest object
Used w/o needing to have a page refresh! 
The "XML" part of the name is antiquated and is used for historical purposes, so don't worry about that. 

This object can retrieve ANY XML, JSON, or HTML data as a response, etc.

Steps for use:
- *Optional but is a good idea* Check to see if the window supports XMLHttpRequest object. An example conditional is below.
- Create a new request XMLHttpRequest object
- Open that new request
- Set any request headers (always set this after .open and before .send)
- Send that request

Some examples
	'''
	var url = "https://rest.coinapi.io/v1/exchangerate/BTC?apikey=809CA8DC-73D9-4616-A709-14D76FA433ED";
		var request = new XMLHttpRequest();

		request.open('GET', url, true);
		request.onload = function () {
			$("div").text(this.response);
		}

		request.send(null);
	'''
Or

	''' 
	if (window.XMLHttpRequest) {
		let xhr = new XMLHttpRequest()
		xhr.open('GET', "api.com/api/results/", true)

		xhr.setRequestHeader("Authorization", 'Bearer ' + "12345")
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

		xhr.responseType = 'arraybuffer'

		xhr.onload = function(res) {
		  if (this.status === 200) {
		    console.log("Congrats");
		  }
		}
	} else {
		// do a chosen action
	}
	'''

Or
	'''
		var xhr = new XMLHttpRequest();

		var url = 'https://api.shop.com:8443/sites/v1/search/term/{term}'.replace(/{term}/g, encodeURIComponent('socks'));

		var queryParams = '?' +  encodeURIComponent('count') + '=' + encodeURIComponent('2')+ '&' +  encodeURIComponent('apikey') + '=' + encodeURIComponent('l7xxf3812d7184d34e7d9da1b4a6824fe9d0');

		xhr.open('GET', url + queryParams);

		xhr.onreadystatechange = function () {
		    if (this.readyState == 4) {
		        alert('Status: '+this.status+'\nHeaders: '+JSON.stringify(this.getAllResponseHeaders())+'\nBody: '+this.responseText);
		    }
		};

		xhr.send('');
	'''

---
### jQuery AJAX request

Note: Make sure to include the jQuery CDN or downloaded jQuery library file name in your HTML! The dataType setting can be set to xml, json, jsonp, script, html, or text

Note: If you're using an older jQ version (< 1.9.0) you should use "type" instead of "method", although they are interchangeable anyway

An example
	'''
	$(document).ready(function() {
		var todaysData = "";
		var yourHeaders = {"a": "header"};

		$.ajax({
      		method: "GET",
      		url: "somekinda.edu/api", 
      		dataType: ‘json’,
  			cache: false,
      		headers: yourHeaders,
      		success: function(result) {
      			console.log("Of COURSE this worked");
      			todaysData += results;
      			console.log(todaysData);
      		},
      		error: function(err) {
      			console.log("Error: " + err);
      		}
  		});
	}
	'''


Or, using some Promise callbacks (.done(), .fail())
	'''
	$(document).ready(function() {
		var todaysData = "";
		var yourHeaders = {"a": "header"};

		$.ajax({
      		method: "GET",
      		url: "somekinda.edu/api", 
      		dataType: ‘json’,
      		headers: yourHeaders,
      		error: function(err) {
      			console.log("Error: " + err);
      		}
      	})
  		.done(function(responseData) {
      		success: function(result) {
      			console.log("Of COURSE this worked");
      			todaysData += results;
      			console.log(todaysData);
      		},
  		})
  		.fail(function() { console.log("This process failed"); });
	}
	'''
---
### Fetch request

For this type of request there are two steps. The first is to make the request and the second is to call the .json()method to transform the received data, aka the response.

Here's an example of the Fetch request structure
	'''
	// Of course, you have to form your headers 
	var h = new Headers();
	h.append('Accept', 'application/json');

	let req = new Request( "https://api.easyapi.net/program/classroom", {
		method:'GET',
		headers:h,
		mode: "cors"
	});


	fetch(req)
		.then(response => return response.json())
		.then(transformedData => 
			console.log(transformedData[0] + " is the name of the doll I love in the doll collection!"))
		.catch(err => console.log("Damnit! So THIS happened: " + err));
	'''

---
And now for a new method to us folks:
### Axios.js
Axios is yet another third-party (not an official JS tool) library for doing cool stuff like sending HTTP requests.

For our use, connecting with the XMLHttpRequest object through our client browsers is done with Axios by using the ES6 Promise API.

Steps to use the library:
- *BEST insted of downloading it* Add a CDN for the Axios library. One example is '''<script src="https://unpkg.com/axios/dist/axios.min.js"></script>'''
- Store the API's root url in a variable to grab later
- Pass that variable to the axios.get() method
- Add any and all needed headers

Example code
	'''
	axios.get(url, {
		params: {
			gamer: "Ninja",
			currency: "Dollar"
		}
	})
	.catch(err => console.log("Oookaaay... Something went wrong."))
	.then(response => console.log("Great! Here is the response: " + response));

	'''
Or
	'''
	const instance = axios.create({
	  baseURL: 'https://api.domain.com/apidirectory/',
	  timeout: 10000,
	  headers: {'A-Custom-Header': 'header-value'}
	});
	'''
Or 
	'''
	const data = { 'foo': "food", "bar": "bar" };
	var headerPairs = {"X-Custom-Header":"Custom-Answer","Another-header":"another-Answer"};

	const options = {
	  method: 'GET',
	  headers: headerPairs,
	  data: JSON.stringify(data),
	  url,
	};
	axios(options);
	'''

Or, by using an (ES 2017!) async/await function as some API SDKs require (remember the try/catch statement?!):
	'''
	async function userData() {
	  try {
	    var response = await axios.get('v4/chosenendpoint?clientid=2341');
	    console.log(response);
	  } catch (error) {
	    console.error(error);
	  }
	}
	'''

Axios is nifty because you have methods like .get(), .post(), .request(), .options(), etc.

For the response object there are the following properties:
- response.data
- response.status
- response.headers
- response.config
- response.statusText

---
References
https://www.carnaghan.com/using-jquery-ajax-to-retrieve-sample-json-data/

https://api.jquery.com/jQuery.ajax/

http://codeheaven.io/how-to-use-axios-as-your-http-client/

https://medium.com/@thejasonfile/fetch-vs-axios-js-for-making-http-requests-2b261cdd3af5

---
Any problems? Try clearing the browser cache, reloading the page, checking out the inspect tool, load the page in another browser, try hosting the site on Github.io or download a local server and run the site's code from it, search on StackOverflow/Reddit/Medium/a general Google search for a solution, pray, ask another developer, load dummy data temporarily, test it out in a curl request (with the needed headers) in the command prompt, try an api that doesn't need credentials or a key, ask in the Slack channels!

Example of a curl command:
	'''
		curl https://api.fantasydata.net/v3/nfl/stats/json/News%20HTTP/1.1 -H "Ocp-Apim-Subscription-Key: 33bbfdd021184014a83998a965065af"
	'''
