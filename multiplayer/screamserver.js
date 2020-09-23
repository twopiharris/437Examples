//screamserver.js
//takes every request and returns it 
//as all uppercase
// modified from 
// https://www.npmjs.com/package/nodejs-websocket
// uses nodejs-websocket

var ws = require("nodejs-websocket");
var connection;
var server = ws.createServer(function(conn) {
	connection = conn;
	console.log("New connection");
       	
	//hook up event handlers
	conn.on("text", textIn);
	conn.on("close", closeConn);
});

var textIn = function(str){
	console.log("received: " + str);
	connection.sendText(str.toUpperCase() + ", Dude!!!");
} // end textIn

var closeConn = function(code, reason){
	console.log("connection closed");
} // end closeConn

server.listen(8001);


