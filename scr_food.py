#周思妤 405631515

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

PTT_URL = 'https://www.ptt.cc'

city = ['基隆','台北','新北','桃園','新竹','苗栗','台中','彰化','雲林','嘉義',
        '台南','高雄','屏東','台東','花蓮','宜蘭','綠島','蘭嶼','馬祖','金門','澎湖']

df = pd.DataFrame(index=city,columns=["count_city"])
df.fillna(value=0, inplace=True)
#print(df)

food_df = pd.DataFrame(columns=["餐廳名稱","消費時間","餐廳區域","餐廳地址","營業時間","電話","平均價位","推薦菜色"])

#---------------------------------------------------------------------

def get_web_page(url):
    
    time.sleep(0.1) # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    res = requests.get(url)
    return res.text

#---------------------------------------------------------------------

def get_total_page(block_link):
    
    
    soup = BeautifulSoup(block_link, 'html.parser')

    select_data = soup.select('div .btn-group-paging a')

    select = []
        
    for line in select_data:
        select.append(line)
            
    link = select[1].get('href')

    startIndex = link.find('index')
    
    endIndex = link.find('.html')
    
    pageNumber = link[startIndex + 5: endIndex]
    return pageNumber

#---------------------------------------------------------------------
    
def get_pageLink(data):
    
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.select('div.title a')       ## find lines in <a>
    
    linkArray = []                      ## save link

    for line in articles:               ## get link of [食記]
         if '[食記]' in  line.text:
            web = PTT_URL + line['href']
            linkArray.append(web)       ## put link while is [食記]
    
    return linkArray

#---------------------------------------------------------------------
    
#選一篇文章中的重點字
def parse(data):
    
    soup = BeautifulSoup(data, 'html.parser')
    
    select_content = soup.find(attrs={"name":"description"})['content']
    
    if '餐廳名稱' not in select_content:
        return -1
    elif '看板' in select_content:
        return -1
    else :
        return select_content

#---------------------------------------------------------------------
#def turnAD(num):
#    if num/



#---------------------------------------------------------------------
        
if __name__ == '__main__':
    current_link = 'https://www.ptt.cc/bbs/Food/index.html'
    current_page = get_web_page(current_link)

    total_pages = int(get_total_page(current_page)) + 1
    print('total pages = ',total_pages)
    pages = 500
    
    add = 1
    
    for i in range(total_pages,total_pages-pages,-1):
        current_link = 'https://www.ptt.cc/bbs/Food/index'+str(i)+'.html'
        print(current_link)
        #取該個page中所有文章網址
        current_page = get_web_page(current_link)
    
        #迴圈讀每一篇文章，並擷取重點
        for a in get_pageLink(current_page):
            
            data = get_web_page(a)
        
            selected_data = parse(data)
            
            #如果'餐廳名稱有在文章中'
            if selected_data != -1:
                selected_data = selected_data.split('\n')
                tmp_a, tmp_b, tmp_c, tmp_d, tmp_e ,tmp_f = ["" for _ in range(6)]
                tmp_loc = ""
                tmp_time = ""
                for j in range(0,len(selected_data)):
                    selected_data[j] = selected_data[j].lstrip()
                    if "餐廳" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip("餐廳名稱:：")
                        tmp_a = selected_data[j]
                    elif "地址" in selected_data[j]:
                        for k in city:
                            if k in selected_data[j]:
                                tmp_loc = k
                        selected_data[j] = selected_data[j].lstrip("地址:：")
                        tmp_b = selected_data[j]
                    elif "消費時間" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip("消費時間:：")
                        tmp_time = selected_data[j]
                    elif "營業時間" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip("營業時間:：")
                        tmp_c = selected_data[j]
                    elif "電話" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip("電話:：")
                        tmp_d = selected_data[j]
                    elif "價位" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip(":：")
                        tmp_e = selected_data[j]
                    elif "推薦菜色" in selected_data[j]:
                        selected_data[j] = selected_data[j].lstrip("推薦菜色:：")
                        tmp_f = selected_data[j]
                                    
                temp_dict={
                        "餐廳名稱":[tmp_a],
                        "消費時間":[tmp_time],
                        "餐廳區域":[tmp_loc],
                        "餐廳地址":[tmp_b],
                        "營業時間":[tmp_c],
                        "電話":[tmp_d],
                        "平均價位":[tmp_e],
                        "推薦菜色":[tmp_f]
                        }
            
#                print(temp_dict)
                
                food_df = food_df.append(pd.DataFrame(temp_dict),ignore_index=True)
                print(add,end=' ')
                add+=1
                food_df.sort_values('餐廳區域',ascending = False ,inplace=True)
                food_df.to_csv("/Users/aaron/Desktop/food1.csv",index=0,encoding="utf_8_sig")
                
        print('\n-------------------------------------------------')           
    
    #將以上資料儲存為csv格式
    

    
    
    
    