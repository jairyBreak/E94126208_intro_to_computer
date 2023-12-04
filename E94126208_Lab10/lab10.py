from flask import *
import random
app = Flask(__name__)


# 設定根目錄(通常代表首頁)之路由
# 使用render_template函式讓首頁的路由能夠回傳html檔(簡單架構)給前端，來顯示首頁畫面，而不是僅用return文字的方式
@app.route("/",methods=['GET'])
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾) 
    return render_template('Lab10.html')


# 設定路由為/set

# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存


@app.route('/student_data',methods = ['POST'])
def root():
    name = request.form['string1']
    ID = request.form['string2']
    #data = request.form.to_dict()
    print("name:",name)
    print("student_id:",ID)
    return 'ok' # response ok

@app.route('/rsp',methods = ['GET'])
def rsp():

    # 使用 request.args.get('參數明稱',預設值)
    chioce_u = request.args.get('choice')
    pc = random.random()
    if pc > 0.66:
        chioce_c = "r"
    elif 0.66 > pc >0.33:
        chioce_c = "s"
    else:
        chioce_c = "p"
    print("玩家出拳：",chioce_u,"\n電腦出拳：",chioce_c)
    if chioce_c == chioce_u:
        return 'It is Tie!'
    
    elif chioce_u  == "r" and chioce_c == "s":
        return "You win!"
    elif chioce_u  == "s" and chioce_c == "p":
        return "You win!"
    elif chioce_u  == "p" and chioce_c == "r":
        return "You win!"
    
    elif chioce_u  == "r" and chioce_c == "p":
        return "You Lose!"
    elif chioce_u  == "s" and chioce_c == "r":
        return "You Lose!"
    elif chioce_u  == "p" and chioce_c == "s":
        return "You Lose!"
    else:
        return "Wrong input!Try again!"
    
app.run(host="0.0.0.0", port=3000, debug=True)