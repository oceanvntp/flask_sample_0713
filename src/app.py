# 必要なモジュールのインポート
from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SubmitField
import datetime
from csv_controller import writeCSV, all_clearCSV
import pandas as pd

# Flaskをインスタンス化
app = Flask(__name__)


# 入力フォーム
class ProgForm(Form):
    learned = StringField('やったこと',[validators.InputRequired()])
    memo = StringField('メモ',[validators.InputRequired()])
    # choice = SelectField('進み具合',
    #                      validators=[validators.InputRequired()],
    #                      choices=[('1', 'ぜんぜん')])
    
    submit = SubmitField('記録')
    delete = SubmitField('全消去')
    
    
# ルートディレクトリにアクセスがあったときの処理
@app.route('/', methods=['GET', 'POST']) 
def index():
    title_ = '機械学習の勉強記録'
    message_ = '学習記録を入力しよう'
    
    progForm = ProgForm(request.form)    
    dt_now = datetime.datetime.now()
    year_ = dt_now.year
    month_ = dt_now.month
    day_ = dt_now.day
    time_ = f'{year_}年{month_}月{day_}日'
    
    # print(request.form.get('submit')=='記録')
    # print(request.form.get('delete'))
    
    if request.method == 'GET':
        record = pd.read_csv('src/record.csv', header=0)
        return render_template('index.html', title=title_, 
                               message=message_, forms=progForm,
                               time=time_, table=record.to_html(header='true'))
    
    elif request.method == 'POST':
        if progForm.validate() == False:
            return render_template('index.html', title=title_, 
                                   message=message_, forms=progForm,
                                   time=time_, table=record.to_html(header='true'))
        else:
            if request.form.get('submit')=='記録':
                str_Learned = str(progForm.learned.data)
                str_memo = str(progForm.memo.data)
                writeCSV(year_, month_, day_,
                        learned=str_Learned, memo=str_memo)
                record = pd.read_csv('src/record.csv', header=0)
                return render_template('index.html', title=title_, 
                                    message=message_, forms=progForm,
                                    time=time_, table=record.to_html(header='true'))
            
            elif request.form.get('delete')=='全消去':
                all_clearCSV()
                record = pd.read_csv('src/record.csv', header=0)
                return render_template('index.html', title=title_, 
                                    message=message_, forms=progForm,
                                    time=time_, table=record.to_html(header='true'))
                
            

# エントリーポイント
if __name__ == '__main__':
    app.run(debug=True)
    
    
    