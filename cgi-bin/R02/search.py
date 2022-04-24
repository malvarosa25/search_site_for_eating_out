# 20K1105 伊藤葵
# レポート課題 R02
# メインページ
# ホットペッパーの API を用い、飲食店を検索します
# いいね数の表示は、ページのリロードボタンを押してから反映されます。
# -----------------------------------
import sys, io
import requests
import cgi, cgitb
import re
import sqlite3

cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, 
                              encoding='utf-8')
form=cgi.FieldStorage()
# -----------------------------------
v_genre = form.getvalue('genre', '')
v_range = form.getvalue('range', '')
v_nice = form.getvalue('nice', '')
# -----------------------------------
def search_current_location():
    geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
    data = requests.get(geo_request_url).json()
    latitude = data['latitude']
    longitude = data['longitude']
    return latitude, longitude

def collect_info(xml):
    connection = sqlite3.connect("shops.sqlite3")
    cur = connection.cursor()
    name = r'</id><name>(.*?)</name>'
    name_list = re.findall(name, xml)
    station = r'<station_name>(.*?)</station_name>'
    station_list = re.findall(station, xml)
    access = r'<access>(.*?)</access>'
    access_list = re.findall(access, xml)
    open_time = r'<open>(.*?)</open>'
    open_list = re.findall(open_time, xml)
    close = r'<close>(.*?)</close>'
    close_list = re.findall(close, xml)
    wifi = r'<wifi>(.*?)</wifi>'
    wifi_list = re.findall(wifi, xml)
    price = r'</name><average>(.*?)</average>'
    price_list = re.findall(price, xml)
    shops = []
    for x in range(len(name_list)):
        cur.execute(f" SELECT nice FROM shops WHERE shop='{name_list[x]}' ")
        point = cur.fetchall()
        if point == []:
            data = [name_list[x], station_list[x], access_list[x],
                    open_list[x], close_list[x], wifi_list[x], 
                    price_list[x], 0]
        else:
            data = [name_list[x], station_list[x], access_list[x],
                  open_list[x], close_list[x], wifi_list[x], 
                  price_list[x], point[0][0]]
        shops.append(data)
    return shops

def shop_search(v_g, la, lo, v_r):
    response = requests.get(
        'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/',
        params={
        'key': 'xxxxxxxxxxxxxx',
        'genre': v_g,
        'lat': la,
        'lng': lo,
        'range': v_r}
        )
    result = response.text
    shops = collect_info(result)
    return shops
  
def make_ans(shops):
    ans = ""
    for s in range(len(shops)):
        ans += "<p>"
        ans += f"{s+1}店目</p>"
        ans += "<ul>"
        ans += f"<li>店名: {shops[s][0]}</li>"
        ans += f"<li>最寄り駅: {shops[s][1]}</li>"
        ans += f"<li>行き方: {shops[s][2]}</li>"
        ans += f"<li>開店・閉店時間: {shops[s][3]}~{shops[s][4]}</li>"
        ans += f"<li>wi-fi の有無: {shops[s][5]}</li>"
        ans += f"<li>平均予算: {shops[s][6]}</li>"
        ans += f"<li>「いいね！」された回数: {shops[s][7]}</li>"
        ans += "</ul>"
        ans += "</p>"
    favorite = "<p>お店に「いいね！」をつけませんか？<br>"
    for s in range(len(shops)):
        favorite += f"<p>{s+1}店目"
        favorite += f"<button type='submit' name='nice' value='{shops[s][0]}'>いいね！</button><br>"
    favorite += "</p>"
    return ans+favorite
    
def add_nice(v_nice):
    connection = sqlite3.connect("shops.sqlite3")
    cur = connection.cursor()
    cur.execute(f" SELECT nice FROM shops WHERE shop='{v_nice}' ")
    point = cur.fetchall()
    if point == []:
        cur.execute(f'INSERT INTO shops VALUES("{v_nice}", "1")')
        connection.commit()
    else:
        p = int(point[0][0])
        new_p = p+1
        cur.execute(f"UPDATE shops set nice='{new_p}' where shop='{v_nice}'")
        connection.commit()
    connection.close()
        

# -----------------------------------
template = """
<html><head>
  <meta charset="utf-8">
  <title> 最終課題(20K1105) </title>
</head>
<body>
  <form method="POST" action="/cgi-bin/R02/search.py">
  <h1 style="color: #8ed0f7; background-color: #294188; font-family: fantasy; ; text-align: center">★★・‥…―━━━―…‥・・‥…―━―…‥・・‥…―━━━―…‥・★★<br>
  今日の外食検索サイト<br>
  ★★・‥…―━━━―…‥・・‥…―━―…‥・・‥…―━━━―…‥・★★</h1>
  <h2 style="color: #8ed0f7; background-color: #294188; font-family: fantasy; ; text-align: center">今日はどこに食べに行きますか？</h2>
  <p>以下の項目を埋めることで、今日の貴方にお勧めのお店を検索します！</p>
  <p>ジャンル:
  <select name="genre">
    <option value="G001">居酒屋</option>
    <option value="G002">ダイニングバー・バル</option>
    <option value="G003">創作料理</option>
    <option value="G004">和食</option>
    <option value="G005">洋食</option>
    <option value="G006">イタリアン・フレンチ</option>
    <option value="G007">中華</option>
    <option value="G008">焼肉・ホルモン</option>
    <option value="G017">韓国料理</option>
    <option value="G009">アジア・エスニック料理</option>
    <option value="G010">各国料理</option>
    <option value="G011">カラオケ・パーティ</option>
    <option value="G012">バー・カクテル</option>
    <option value="G013">ラーメン</option>
    <option value="G0016">お好み焼き・もんじゃ</option>
    <option value="G014">カフェ・スイーツ</option>
    <option value="G015">その他グルメ</option>
  </select></p>
  <p>検索範囲:
  <select name="range">
    <option value="1">300</option>
    <option value="2">500</option>
    <option value="3">1000</option>
    <option value="4">2000</option>
    <option value="5">3000</option>
  </select>m</p>
  <p> <input type="submit"></p>

  Powered by <a href="http://webservice.recruit.co.jp/">ホットペッパー Webサービス</a>
  <h2 style="color: #8ed0f7; background-color: #294188; font-family: fantasy; ; text-align: center">検索結果</h2>
  {ans}
</body>
<html>
"""
la, lo = search_current_location() # 現在地の緯度・経度を取得
shops = shop_search(v_genre, la, lo, v_range)
add_nice(v_nice)
ans = make_ans(shops)
text = template.format(ans = ans)
print("Content-type: text/html\n")
print(text)
