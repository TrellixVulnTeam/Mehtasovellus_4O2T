import React from 'react';
import {Component} from 'react';
import ReactDOM from 'react-dom';

var request = new XMLHttpRequest();

request.open(
  "GET",
  "https://bgpo5j271l.execute-api.eu-west-1.amazonaws.com/dev/v2/all",
  true
);
request.onload = function() {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  data.response.forEach(function(element) {

var tiedot = "<h1> " + element.locationName + "</h1>"
+ "<p> Pysähdyspaikkoja: " + element.points.length + "<br>"
+ "Lämpötila: " + element.weather.temperature + " °C <br>"
+ "Sää: " + element.weather.weather + " <br>"
+ "Reittejä: " + element.routes.length +  "</p>";

var i ; var text = "";
for (i = 0; i < element.routes.length; i++) {
  text += i+1 + ". reitin pituus: " + Math.round(element.routes[i].length * 100) / 100 + " km <br>";
}

    // Create a div with a card class
      const button = document.createElement("button");
      button.setAttribute("class", "card");
      button.onclick = function(){
    document.getElementById("infolaatikko").innerHTML = tiedot;
    document.getElementById("text").innerHTML += text;
    document.getElementById("overlay").style.display = "block";
};
      // Create an h1 and set the text content to the film's title
      const h1 = document.createElement("h1");
      h1.textContent = element.locationName;
      // Each card will contain an h1 and a p
      const p3 = document.createElement("p");
      p3.textContent = "Sää: " + element.weather.weather;

      const p4 = document.createElement("p");
      p4.textContent = "Lämpötila: " + element.weather.temperature + " °C";

      const p5 = document.createElement("p");
      p5.textContent = "Pysähdyspaikat: " + element.points.length;

      button.appendChild(h1);
      button.appendChild(p3);
      button.appendChild(p4);
      button.appendChild(p5);

      document.body.appendChild(button);

      });

}
request.send();
