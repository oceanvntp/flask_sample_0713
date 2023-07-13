import pandas as pd

def writeCSV(year:int, month:int, day:int, learned:str, memo:str):
    df = pd.read_csv('src/record.csv', header=0)
    new = pd.DataFrame({
        '年':[year],
        '月':[month],
        '日':[day],
        '勉強したこと':[learned],
        'メモ':[memo]
    })
    
    df_ = pd.concat([df, new], axis=0)
    df_.to_csv('src/record.csv', index=None)
    
def all_clearCSV():
    df = pd.DataFrame({
        '年':[],
        '月':[],
        '日':[],
        '勉強したこと':[],
        'メモ':[]
    })
    df.to_csv('src/record.csv', index=None)