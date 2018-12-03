'use strict';

$( document ).ready(function() {
	// Variables
		$("a").attr("target","_blank");

		var NYTTIMES_API_URL	= "https://api.nytimes.com/svc/topstories/v2/nyregion.json?api-key=",
	  	GHIBLI_API_URL			= "https://ghibliapi.herokuapp.com/films",	
	  	OPENWEATHERMAPS_API_URL	= "https://api.openweathermap.org/data/2.5/weather?zip=11226,us&appid=",
		// SPOTIFY_API_URL			= "https://api.spotify.com/v1/browse/categories?limit=3",
		// SPOTIFY_API_URL			= "https://accounts.spotify.com/en/authorize?response_type=code&redirect_uri=https:%2F%2Fgithubbubber.github.io%2F&client_id=",
		GIPHY_API_URL			= "http://api.giphy.com/v1/gifs/trending?limit=5&api_key="; 
		// GFYCAT_API_URL			= "https://api.gfycat.com/v1/gfycats/search?search_text=omg&gfyCount=1",
		// GIANTBOMB_API_URL		= "https://www.giantbomb.com/api/game/3030-47342/?field_list=name,genre,image,theme,platforms&api_key=",
		// TWITCH_API_URL			= "https://id.twitch.tv/oauth2/authorize?&response_type=code&edirect_uri=https://githubbubber.github.io/&scope=viewing_activity_read+openid&client_id=",
		// MTA_API_URL				= "http://datamine.mta.info/mta_esi.php?&feed_id=1&key="; 

		let allURLs				= {
								"nyt"		:NYTTIMES_API_URL, 
								"ghibli"	:GHIBLI_API_URL, 
								"openwm"	:OPENWEATHERMAPS_API_URL, 
								// "spotify"	:SPOTIFY_API_URL, 
								"giphy"		:GIPHY_API_URL 
								// "gyfycat"	:GHIBLI_API_URL,
								// "giantbomb"	:GHIBLI_API_URL, 
								// "twitch"	:TWITCH_API_URL, 
								// "mta"		:GHIBLI_API_URL
								};

	// User msg letting them know how up to date this API page is
		var months 				= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
			theDate 			= new Date(), updated 			= new Date("November 23, 2018"),
			today 				= months[theDate.getMonth()] + " " + theDate.getDate() + ", " + theDate.getFullYear(),
			dateLastUpdated 	= months[updated.getMonth()] + " " + updated.getDate() + ", " + updated.getFullYear();

		var msgForLastUpdated	= $("span#lastUpdated"), msgForWhatIsToday	= $("span#whatIsToday"), msgForUpToDateOrNot	= $("span#upToDateOrNot"),
			totalDays			= 45; //today - dateLastUpdated;

		msgForLastUpdated[0].innerText		= dateLastUpdated;
		msgForWhatIsToday[0].innerText		= today;
		msgForUpToDateOrNot[0].innerText	= (totalDays > 30)? "pretty accurate" : "kinda out of date";

	// If the user selects an API from the dropdown list, navigate to that API's section
		$( "#apiSelect" ).on("change", function() {
			location.href = location.pathname + "#"+ $('#apiSelect').val();
		});		

	function theCallBackFunc() { console.log("It worked!"); }

	// Displaying all API info in index.html's API section
		Object.entries(allURLs).forEach(([key, value]) => {
			var whichCors = ((key == "spotify")||(key == "giantbomb")||(key == "twitch"))? 'no-cors' : 'cors';

			let h = new Headers();
			h.append('Accept', 'application/json');

			let req = new Request( value, {
				method:'GET',
				headers:h,
				mode: whichCors
			});

			fetch(req)
				.then((response) => {
					if(response.ok) {
						return response.json();
					} else {
						$("section.apis div.row div.two-thirds." + key).append('<p>This API is currently unavailable. Please try again.</p>');
						throw new Error('Bad HTTP stuff');
					}
				})
				.then( (jsonData) => {
					var someVar = "";

					switch(key) {
						case "nyt":
							someVar = 'Title: "' + 
								jsonData["results"][0]["title"] + 
								'"<br />Abstract: "' + 
								jsonData["results"][0]["abstract"] + 
								'"<br />'+
								'<a href="' + jsonData["results"][0]["url"] + '">Read more on NYTimes.com</a> ';
							break;
						case "ghibli":
							someVar = 'Title: "' + 
								jsonData[0]["title"] + 
								'"<br />Description: "' + 
								jsonData[0]["description"] + 
								'"';
							break;
						case "openwm":
							someVar = '<img src="http://openweathermap.org/img/w/' + 
								jsonData.list[0].weather[0].icon + '.png" alt="Weather icon" style="height: 40px; width:auto;" /> &nbsp; There is ' + jsonData.list[0].weather[0].description + 
								' right now.<br />';
							break;
						// case "spotify":
							// console.log("The location now is " + location.href);
							// someVar = jsonData.weather[0];

							// let h = new Headers();
							// h.append('Accept', 'application/json');
							
							// console.log("The location now is " + location.href);

							// let req = new Request( location.href, {
							// 	method:'GET',
							// 	headers:h,
							// 	mode:'no-cors'
							// });

							// fetch(req)
							// 	.then( (response) => {
							// 		if(response.ok) {
							// 			console.log(response);

							// 			return response.json();
							// 		} else { 
							// 		$("section.apis div.row div.two-thirds." + key).append('<p>Aww, The Spotify API is currently unavailable. Please try again.</p>');
							// 			throw new Error('Bad Spotify HTTP stuff');
							// 		}
							// 	})
							// 	.then( (jsonData) => {
							// 		var someVar = "";
							// 	})
							
							// break;
						case "giphy":
							someVar = '<img src="' + 
								jsonData["data"][0]["images"]["downsized"]["url"] + 
								'" alt="Funny Giphy API gif" style="width:300px; height:auto;"/><br />Title: "' + 
								jsonData["data"][0]["title"] + 
								'"';
							break;
						// case "gyfycat":
							// 	someVar = '<img src="' + 
							// 		jsonData[0]["gfycats"][0]["tags"]["gifUrl"] + 
							// 		'" alt="Another funny gif API" style="width: 300px; height: auto;" /><br />This gif was viewed: ' + 
							// 		jsonData[0]["gfycats"][0]["tags"]["views"] + ' times.';
							// 	break;
						// case "giantbomb":
							console.log(jsonData);
							someVar = 'Title: "' + 
								jsonData + 
								'"<br />Description: "' + 
								jsonData + 
								'"';
							break;
						// case "twitch":
							someVar = 'Title: "' + 
								jsonData[0]["title"] + 
								'"<br />Description: "' + 
								jsonData[0]["description"] + 
								'"';
							break;
						default:
							someVar = "Looks like this one has no results to show."
					}

					

					$("." + key).append('<p>'+someVar+'</p>');
				})
				.catch((err) => { console.log('Error', err.message); });

		});
		
});

