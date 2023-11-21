from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import math
app = Flask(__name__)
CORS(app)

PI = 3.14159265358
#calculate/poll the data you want
mu_earth = 398600 #km^3/s^2
R_earth = 6380 #km
arg_peri = 327.9325*PI/180 #radians
h_perigee = 417 #km
r_p = h_perigee + R_earth 
h_apogee = 419 #km
r_a = h_apogee + R_earth
RA_AN = 277.2343*PI/180 #radians
e = (r_a - r_p)/(r_a + r_p)
print(e)
i = 51.6*PI/180 #radians
h = math.sqrt(r_p*mu_earth*(1+e))
theta = np.linspace(0, 2*PI, 360)
R31 = [[np.cos(arg_peri), np.sin(arg_peri), 0], [-np.sin(arg_peri), np.cos(arg_peri), 0], [0, 0, 1]]
R1 = [[1, 0, 0], [0, np.cos(i), np.sin(i)], [0, -np.sin(i), np.cos(i)]]
R32 = [[np.cos(RA_AN), np.sin(RA_AN), 0], [-np.sin(RA_AN), np.cos(RA_AN), 0], [0, 0, 1]]
C = np.matmul(R31, np.matmul(R1, R32))
C_trans = np.transpose(C)
positions = []
for angle in theta:
    r_peri = np.transpose([h**2/mu_earth*np.cos(angle)/(1+e*np.cos(angle)), h**2/mu_earth*np.sin(angle)/(1+e*np.cos(angle)), 0])
    r_geo = np.matmul(C_trans, r_peri)
    r_geo1 = [r_geo[0]*1000, r_geo[1]*1000, r_geo[2]*1000]
    positions.append(r_geo1)

#placeholder for the webpage
@app.route("/")
def hello_world():
    return "<p>This is a placeholder for the server api</p>"


#return the iss positions/times with the /issdata get request
@app.route("/issdata")
def get_issdata():

    return jsonify(positions)

if __name__ == "__main__":
    app.run(debug = True)