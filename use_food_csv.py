#周思妤 405631515

import pandas as pd

if __name__=="__main__":
    
    data = '/Users/aaron/Desktop/food.csv'
    df = pd.read_csv(data)
    
    cities = ['基隆','台北','新北','桃園','新竹','苗栗','台中','彰化','雲林','嘉義',
        '台南','高雄','屏東','台東','花蓮','宜蘭','綠島','蘭嶼','馬祖','金門','澎湖']
    
    print('Ptt美食版資料查詢')
    print('輸入 1 選擇店名關鍵字查詢功能')
    print('輸入 2 選擇城市名稱查詢功能')
    print('輸入 3 選擇csv合併功能')
    choose = int(input('你選擇的功能為...>'))
    
    
    if choose == 1:
        shop = input('請輸入欲查詢餐廳的關鍵字..>')
        print('正在為你查詢店名為(',shop,')的店家.......')
        for x in range(len(df)):
            if shop in df.loc[x]['餐廳名稱']:
                print(df.loc[x],'\n')
    
    elif choose == 2 :
        city = input('請輸入欲查詢餐廳的城市(若不指定城市請輸入0)..>')
        print('正在為你查詢所在城市為(',city,')的店家.......')
        if city in cities:
            df = df[df['餐廳區域']==city]
            df.to_csv("/Users/aaron/Desktop/search.csv",index=0,encoding="utf_8_sig")
            print('已將你要的查詢放至桌面:search.csv')
        elif city == 0:
            df = df
            df.to_csv("/Users/aaron/Desktop/search.csv",index=0,encoding="utf_8_sig")
            print('已將你要的查詢放至桌面:search.csv')
        else:
            print('輸入城市名稱錯誤，請重新操作程式')
    
    elif choose == 3:
        data1 = input('請輸入第1個csv檔案名稱：')
        data2 = input('請輸入第2個csv檔案名稱：')
        data1 =  '/Users/aaron/Desktop/' + data1
        data2 =  '/Users/aaron/Desktop/' + data2
        df1 = pd.read_csv(data1)
        df2 = pd.read_csv(data2)
        new_df = pd.merge(df1,df2,how='outer')
        new_df.sort_values('餐廳區域',ascending = False ,inplace=True)
        new_df.to_csv("/Users/aaron/Desktop/food.csv",index=0,encoding="utf_8_sig")
        print('合併為 food.csv 成功')
        
    else:
        print('輸入錯誤，請重新操作程式')
    