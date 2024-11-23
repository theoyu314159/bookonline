from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    return html

@app.route('/finish',methods=['POST'])
def finisih():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html=f.read()
    name=request.form.get('name')
    date=request.form.get('date')
    time=request.form.get('time')
    email=request.form.get('email')
    printin='name:'+name+'date:'+date+'time:'+time+'email:'+email+'<br>'
    with open('back.txt','a',encoding='utf-8') as f:
        f.write(printin)
    return html.replace('<out/>','預約成功')

@app.route('/back')
def back():
    html=''
    out=''
    with open('back.html','r',encoding='utf-8') as f:
        html=f.read()
    with open('back.txt',"r",encoding="utf-8") as f:
        out=f.read()
    return html.replace('<out/>',str(out))

app.run(debug=True, host='0.0.0.0')
