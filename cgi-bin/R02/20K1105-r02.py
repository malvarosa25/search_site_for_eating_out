# 20K1105 伊藤葵
# レポート課題 R02
# 実行方法: http://localhost:8000/cgi-bin/R02/20K1105-r02.py
# ログイン画面
# ユーザー名: イトウアオイ
# パスワード: Hkkx3P6SB3
# -----------------------------------
import sys, io
import cgi, cgitb
import sqlite3

connection = sqlite3.connect("users.sqlite3")
cur = connection.cursor()

cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, 
                              encoding='utf-8')
form=cgi.FieldStorage()
# -----------------------------------
v_user = form.getvalue('user', '')
v_password = form.getvalue('password', '')
# -----------------------------------
template = """
<html><head>
  <meta charset="utf-8">
  <title> 最終課題(20K1105) </title>
  <link rel="stylesheet" href="http://localhost:8000/cgi-bin/R02/stylesheet.css">
</head>
<body>
  <form method="POST" action="/cgi-bin/R02/20K1105-r02.py">
  <h1 style="color: #8ed0f7; background-color: #294188; font-family: fantasy; ; text-align: center">★★・‥…―━━━―…‥・・‥…―━―…‥・・‥…―━━━―…‥・★★<br>
  今日の外食検索サイト<br>
  ★★・‥…―━━━―…‥・・‥…―━―…‥・・‥…―━━━―…‥・★★</h1>
  <h2 style="color: #8ed0f7; background-color: #294188; font-family: fantasy; ; text-align: center">ログイン</h2>
  <p>ユーザー名とパスワードを入力してください。</p>
  <p>ユーザー名: <input type="text" name="user">
  <p>パスワード: <input type="text" name="password">
  <p> <input type="submit"></p>
  {result}
</body>
<html>
"""
cur.execute(f" SELECT name FROM users WHERE name='{v_user}' ")
user = cur.fetchall()
if user == []:# ユーザーが存在しない場合
    result = "<p>そのユーザーは存在しません。</p>"
if user != []:
    cur.execute(f" SELECT password FROM users WHERE name='{v_user}' ")
    pw = cur.fetchall()
    if v_password == pw[0][0]:
        result = "<p>認証に成功しました。 <a href='/cgi-bin/R02/search.py'>進む</a></p>"
    else:
        result = "<p>パスワードが違います。</p>"
if v_user == v_password == '':
    result = ""
    

text = template.format(result = result)
print("Content-type: text/html\n")
print(text)