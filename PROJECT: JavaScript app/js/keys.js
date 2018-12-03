// All API keys will be saved here

/*
APIs I will use: NYTimes, Studio Ghibli, Open Weather Maps, Google Maps, Spotify, Giphy, GiantBomb, Twitch, MTA, BRAINTREE
*/

var API_HEADERCAT 			= "Authorization:",
	API_HEADERVALUE 		= "Bearer ???",

	NYTTIMES_API_URL		= "https://api.nytimes.com/svc/topstories/v2/technology.json",
	NYTTIMES_API_KEY 		= "e94c8105097b4ba0980ac033f5b2386b", // SECURED with site url; From https://developer.nytimes.com/signup
  	NYTTIMES_API_URL 		+= '?' + $.param({ 'api-key': NYTTIMES_API_KEY }),

  	GHIBLI_API_URL			= "https://ghibliapi.herokuapp.com/films",	// From https://ghibliapi.herokuapp.com
	
  	OPENWEATHERMAPS_API_URL	= "http://api.openweathermap.org/data/2.5/forecast?zip=11226,us&APPID=", // From https://openweathermap.org/api
	OPENWEATHERMAPS_API_KEY = "f955e61b38f6dee6525e507644d69d1b",
	OPENWEATHERMAPS_API_URL += OPENWEATHERMAPS_API_KEY,

	GOOGLEMAPS_API_URL		= "https://maps.googleapis.com/maps/api/js?key=",
	GOOGLEMAPS_API_KEY 		= "AIzaSyBoY3z4NiYnKgu1fCdmukSf4gh8OFfm49A",	// SECURED with site url; From https://developers.google.com/maps/documentation/javascript/get-api-key
	GOOGLEMAPS_API_URL		+=	GOOGLEMAPS_API_KEY	+ "&callback=initMap",

	SPOTIFY_API_URL			= "https://accounts.spotify.com/en/authorize?response_type=code&redirect_uri=https:%2F%2Fgithubbubber.github.io%2F&client_id=",
	// SPOTIFY_API_URL			= "https://api.spotify.com/v1/browse/categories?limit=3",
	SPOTIFY_API_CLIENTID 	= "4dd922fd6541490fa0b14160086426d0",	// SECURED with site url; From https://developer.spotify.com/documentation/web-api/
	
	GIPHY_API_URL			= "http://api.giphy.com/v1/gifs/trending?limit=5&api_key=", 
	GIPHY_API_KEY			= "H8Zn9ZKYesqZ0lffFenz67ZlfvPWaXOt",
	GIPHY_API_URL			+= GIPHY_API_KEY,

	GFYCAT_API_OAUTH		= "https://api.gfycat.com/v1/oauth/token",
	// curl -v -XPOST -d '{"client_id":"YOUR_ID_HERE", "client_secret": "YOUR_SECRET_HERE", "grant_type": "client_credentials"}' https://api.gfycat.com/v1/oauth/token

	GFYCAT_API_URL			= "https://api.gfycat.com/v1/gfycats/search?search_text=omg&gfyCount=1", // From https://developers.gfycat.com/api

	GIANTBOMB_API_URL		= "https://www.giantbomb.com/api/game/3030-47342/?format=json&field_list=name,genre,image,theme,platforms&api_key=",
	GIANTBOMB_API_KEY 		= "18f19ab9edab370b2351b0e0ba0c22eb84656fc4",

	TWITCH_API_URL			= "https://api.twitch.tv/kraken/", // SECURED with site url; https://dev.twitch.tv/docs; OAUTH generated with info from this page: https://dev.twitch.tv/docs/authentication/getting-tokens-oidc/#oidc-authorization-code-flow

	/*  https://id.twitch.tv/oauth2/authorize?client_id=itphoii95ha6ohzh3hzjik8fz7wezr&response_type=code&edirect_uri=https://githubbubber.github.io/&scope=viewing_activity_read+openid which is 
		https://id.twitch.tv/oauth2/authorize
		?
		client_id=itphoii95ha6ohzh3hzjik8fz7wezr
		&
		response_type=code
		&
		redirect_uri=https://githubbubber.github.io/
		&
		scope=viewing_activity_read+openid
	*/
	TWITCH_API_CLIENTID		= "itphoii95ha6ohzh3hzjik8fz7wezr", 
	TWITCH_API_KEY 			= "9d4vywl3lztz8ynwa2pzn6wfpzqgabd",
	
	MTA_API_KEY				= "2ce220470bccc1aa5f0adfaafb5185dc",
	MTA_API_URL				= "http://datamine.mta.info/mta_esi.php?key=" + MTA_API_KEY+ "&feed_id=1", ///api/v1/trains",


	// <script src="https://js.braintreegateway.com/web/dropin/1.14.1/js/dropin.min.js"></script>
	BRAINTREE_API_MERCHANTID 	= "dzyxnw47qy7zxphd", // Sandbox Keys & Configuration
	BRAINTREE_API_KEY 			= "g34jhjf278g3x4bw",
	BRAINTREE_API_PRIVATEKEY 	= "784c00c9d891e00384dd78b347b0479b";

var allURLs					= [NYTTIMES_API_URL, GHIBLI_API_URL, OPENWEATHERMAPS_API_URL, GOOGLEMAPS_API_URL, GFYCAT_API_URL, GIANTBOMB_API_URL, TWITCH_API_URL, MTA_API_URL];


var tempHolder = "key=AIzaSyD4Ocmhp_nfGsfRAcVjIaFevDJ7ehSXeUs";