#參考網址: https://oranwind.org/python-pandas-ji-chu-jiao-xue/

#pandas練習
import pandas as pd
import os

#讀取CSV檔
pwd = os.getcwd()#獲取當前路徑
print("當前路徑為:",pwd)
path1 = '/Users/aaron/Desktop/R/Data/Report02.csv'
df = pd.read_csv(path1)  
print(df)  

# 讀取 HTML
dfs = pd.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')  
print(dfs)  

# Intro. 
# Pandas提供的資料框架有三種
# 1.Series：用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。
# 2.DataFrame：用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。
# 3.Panel：用來處理有資料及索引、列索引與欄標籤的三維資料集。


cars = ["BMW", "BENZ", "Toyota", "Nissan", "Lexus"]
# 1. Series
    # 資料可以的類型如：array dictionary 單一資料 

# Array
select = pd.Series(cars)
print("Array -> \n",select)

# Dictionary
dict = {  
    "factory": "Taipei",
    "sensor1": "1",
    "sensor2": "2",
    "sensor3": "3",
    "sensor4": "4",
    "sensor5": "5"
}
select = pd.Series(dict, index = dict.keys()) # 排序與原 dict 相同  
print("Dictionary -> \n",select)

# 2. DataFrame
# 資料為dictionary轉dataframe
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
       }

select_df = pd.DataFrame(dict)

print("DataFrame1 -> \n ",select_df) # 看看資料框的外觀


#資料為Array轉dataframe
arr = groups = [["Movies", 46],["Sports", 8], ["Coding", 12],
                ["Fishing",12], ["Dancing",6], ["cooking",8]]
df = pd.DataFrame(arr, columns = ["name", "num"]) # 指定欄標籤名稱  
print("DataFrame2 -> \n",df)

#Dataframe操作
print("-----")
print(".shape \n",df.shape) # 回傳列數與欄數  
print("-----") 
print("describe() \n",df.describe()) # 回傳描述性統計  
print("-----")  
print(df.head(3)) # 回傳前三筆觀測值  
print("-----")  
print(df.tail(3)) # 回傳後三筆觀測值  
print("-----")  
print(".columns \n",df.columns) # 回傳欄位名稱  
print("-----")  
print(".index \n",df.index) # 回傳 index  
print("-----")  
print(".info \n",df.info) # 回傳資料內容 


#dataframe 取值
