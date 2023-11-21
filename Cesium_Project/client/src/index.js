
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";
import "../src/css/main.css"

async function getpositions() {
  const response = await fetch("http://127.0.0.1:5000/issdata");
  const __coords = await response.json();
  return __coords;
}
var coords = await getpositions();
var positions = [];
var posArray = [];
console.log(coords.length)
for(var i = 0; i<coords.length; i++){
  var currCar3 = new Cesium.Cartesian3(coords[i][0], coords[i][1], coords[i][2]);
  var currPos = [coords[i][0], coords[i][1], coords[i][2]];
  posArray.push(currPos);
  positions.push(currCar3);
}
console.log(posArray)
var viewer = new Cesium.Viewer('cesiumContainer');

const issLine = viewer.entities.add({
    name: "Iss Line",
    polyline: {
      positions: positions,
      width: 5,
      material: Cesium.Color.PINK,
    },
  });