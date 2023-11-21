
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";
import "../src/css/main.css"

//calculate iss orbit using data? - start with something else
var positions = []
var h = 6773345; //m
var theta = 0; //rad
for (var i = 0; i<361; i++){
    theta = i*2*Math.PI/360;
    var posfromdeg = new Cesium.Cartesian3(Math.cos(theta)*h, Math.sin(theta)*h, 0);
    positions.push(posfromdeg);
}
var viewer = new Cesium.Viewer('cesiumContainer');

const issLine = viewer.entities.add({
    name: "Iss Line",
    polyline: {
      positions: positions,
      width: 5,
      material: Cesium.Color.PINK,
    },
  });