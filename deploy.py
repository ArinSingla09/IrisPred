from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

model=pickle.load(open('IrisFlower.pkl','rb'))

@app.route('/')
def home():
    res='Please Enter the details'
    return render_template('index.html',result=res)

@app.route('/predict',methods=['POST'])
def predict():
    sepalLength=float(request.form['sepal_length'])
    sepalWidth=float(request.form['sepal_width'])
    petalLength=float(request.form['petal_length'])
    petalWidth=float(request.form['petal_width'])

    arr=[sepalLength,sepalWidth,petalLength,petalWidth]
    res=model.predict([arr])

    return render_template('index.html',result=res[0])

if __name__=='__main__':
    app.run(debug=True)