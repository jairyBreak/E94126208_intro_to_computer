#coding=utf-8

from flask import *
import random
app = Flask(__name__)
current_data = {}#create the dict


@app.route("/")
def index():
    # return the first page
    return render_template('lab10_plus.html')

# /set
@app.route('/set',methods = ['POST'])
def root():
    print(current_data)
    while True :
        Store = request.form['string1']
        Score = request.form['string2']
        current_data[Store] = Score #input data in dict 
        #current_data_str = str(current_data)
        print("[user input]:store name:",Store," ; score:",Score)
        print("[data on server]: ",current_data) 
        return render_template('lab10_plus.html',current_data_str=current_data) #把字典轉成為字串之後再傳到前端
    #return data in html
   


@app.route('/reset/<clear>',methods = ['GET'])
def reset(clear):
    global current_data
    #input y to clear the dict
    #print(current_data)
    #print(clear)
    if clear == 'y' :
        current_data={}#clear
        print("[data on server]: ",current_data)
    return render_template('reset.html')#return the reset.html
    #return render_template('lab10_plus.html',current_data_str=current_data)
app.run(host="0.0.0.0", port=3000, debug=True)
