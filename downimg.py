import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート

URL = 'https://www.it-college.ac.jp/' # URL入力
images = [] # 画像リストの配列

soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src")) # imagesリストに格納
    elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
        images.append(link.get("src")) # imagesリストに格納

for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open('/home/s19011/Documents/date/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

print("ok") # 確認
