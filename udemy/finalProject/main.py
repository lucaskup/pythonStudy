from flask import Flask, render_template, request
from geopy import Nominatim
import pandas

nom = Nominatim()
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        df1 = pandas.read_csv(f)
        df1["CAddress"] = df1["Address"] +', '+df1["City"]+", "+df1["State"]
        df1["Longitude"] = df1["CAddress"].apply(lambda x: nom.geocode(x).longitude if nom.geocode(x) != None else None )
        df1["Latitude"] = df1["CAddress"].apply(lambda x: nom.geocode(x).latitude if nom.geocode(x) != None else None )
        print(df1)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
