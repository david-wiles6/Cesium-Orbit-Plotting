# Orbit Plotting With Cesium

This project visualizes orbits using Cesium to create the graphics. It also uses a flask server to calculate the orbit trajectory based on classical orbital elements (right ascension of ascending node, eccentricity, argument of periapsis, semimajor axis, and inclination)

## Motivation

I wanted to do this project because of my Astronautics class where we were learning about defining orbits using orbital elements. At the same time, I was doing a project with cesium for an internship, so I wanted to put these two things together, especially because cesium is such a powerful tool for earth based visualization. 

## Current State

Currently the orbit is defined using hard coded numbers in the server. The server communicates with the client using socketio websockets. The client waits for the server to send an orbit, then plots that orbit and runs the visualization.

## Future Plans

In the future, I'd like to add an input gui on server side with tkinter to plot multiple orbits that can be user-defined. This would also involve polling the server on the client side to adjust the data plotted as it changes. I'd also like to potentially account for orbital perturbations to get a more accurate simulation. 
