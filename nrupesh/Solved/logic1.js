d3.csv("defaultrate.csv", function(error, Data) {
  if (error) return console.warn(error);

  console.log(Data);
 
  // log a list of names
  
  var states = Data.map(data => data["States"]);
  console.log("States", states);
  var defaults = Data.map(data => data["Defaults"]);
  console.log("Defaults", defaults);
  var loans = Data.map(data => data["Loans"]);
  console.log("Loans", loans);
  var defRate = Data.map(data => data["Def Rate"]);
  console.log("Def Rate", defRate);
  var coordinates = Data.map(data => data["Coordinates"]);
  console.log("Coordinates", coordinates);

  var myMap = L.map("map", {
    center: [39.8283, -98.5795],
    zoom: 4
  });
  
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);
  
  for (var i = 0; i < states.length; i++) {
    console.log(i)
    L.marker(JSON.parse(coordinates[i]))
      .bindPopup("<h1>" + states[i] + "</h1> <hr> <h3>Defaults: " + defaults[i] + "</h3> <h3>Loans: " + loans[i] + "</h3> <h3>Default Rates: " + defRate[i] + "</h3>")
      .addTo(myMap);
  };
})
