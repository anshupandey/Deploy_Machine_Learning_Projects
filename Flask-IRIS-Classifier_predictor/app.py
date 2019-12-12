from flask import Flask, render_template,request
# create an app
app = Flask(__name__)
import joblib
model = joblib.load("iris_model.pkl")

@app.route("/")
def fun1():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def fun2():
    data = dict(request.form)
    data2 = [data["SL"],data["SW"],data["PL"],data["PW"]]
    data2 = [int(i) for i in data2]
    output = model.predict([data2])
    data["Prediction"] = output[0]
    return render_template("output.html",output=data)

if __name__=="__main__":
    app.run()