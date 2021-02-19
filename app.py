from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np




app=Flask(__name__)
model=pickle.load(open("model_practice.pkl",'rb'))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/Predict',methods=['POST'])
def Predict():
    ssc_p = request.form['ssc_p']
    hsc_p = request.form['hsc_p']
    degree_p = request.form['degree_p']
    etest_p = request.form['etest_p']
    mba_p = request.form['mba_p']
    gender = request.form['gender_M']
    ssc_board = request.form['ssc_b_Others']
    hsc_board = request.form['hsc_b_Others']
    hsc_stream = request.form['hsc_s_Others']
    graduation_stream = request.form['degree_t_Others']
    work_ex = request.form['workex_Yes']
    specialisation = request.form['specialisation_Mkt&HR']
    value=[ssc_p,hsc_p,degree_p,etest_p,mba_p,gender,ssc_board,hsc_board,hsc_stream,graduation_stream,work_ex,specialisation]
    
    data=[np.array(value)]
    prediction= model.predict(data)

    if prediction <= 0.5:
        return render_template('index.html',prediction_text = "You Will Not Placed")
    else:
        return render_template('index.html',prediction_text = "You Will Placed")


    


if __name__== '__main__':
    app.run(debug=True)
