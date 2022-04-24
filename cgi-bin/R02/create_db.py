# 20K1105 伊藤葵
# レポート課題 R02
# データベース作成
# -----------------------------------
import sqlite3
connection = sqlite3.connect("users.sqlite3")
cur = connection.cursor()

# ユーザーとそのパスワードのデータベースを作成する
cur.execute("CREATE TABLE users(name, password)")
def create_users(cur, name, password):
    cur.execute(f'INSERT INTO users VALUES("{name}", "{password}")')
# 名前とパスワード一覧（今回は乱数を用いて 100 件生成）
names = ['モリモトリク', 'クロサマナ', 'イトウアオイ', 'サカイユウダイ', 'コバヤシリョウ', 'マスカタイサーク', 'オガワハラシンヤ', 'シノハラサキ', 'マツカワミナト', 'トミバリワカナ', 'ヤマモトツネコ', 'ハナミズザカマモリ', 'コニシユキコ', 'ミヤガワミエコ', 'サカキラン', 'イノウエカオル', 'ヤマガタダニアオイ', 'テンノカワハルカ', 'キクフロレンティナ', 'タジマスミコ', 'ディアネット', 'コラリーヌ', 'レオノール', 'ランシーヌ', 'ジャニーヌ', 'ジャネット', 'サンドロン', 'ジャニエス', 'エルミニク', 'マガリーヌ', 'エロイネス', 'エリザボー', 'コラリーヌ', 'リリアーヌ', 'デライネス', 'カロル', 'エグラベル', 'アリアニック', 'アリアーヌ', 'カトリエル', 'エルベーレ', 'コッランコ', 'ルクウーゴ', 'ルチジェロ', 'ランベリオ', 'ルチジルド', 'ウゼビーノ', 'ディナテッロ', 'アベラード', 'ポリナルド', 'アルリエト', 'バルトビア', 'カールジョ', 'フィロルド', 'チェチェロ', 'エルマーロ', 'ルキオッレ', 'ドリアーノ', 'グアルフォ', 'ルフレンテ', 'カミラ', 'エルファニ', 'ストリーセ', 'ダクマリー', 'ルネリーデ', 'ユッテ', 'ギーゼルマ', 'ドーリーザ', 'ルトラーラ', 'ヘルミルダ', 'ルハイルゼ', 'イジドゥラ', 'ジークシア', 'ブリエラ', 'リーザンナ', 'ラッヘルタ', 'ルフリヤム', 'クダレーナ', 'フロレーア', 'ウルズザネ', 'ジャスター', 'ティクシス', 'デイモンド', 'ハーヴァン', 'ランダレル', 'ハーヴァー', 'ストフリー', 'ライアラン', 'アイザック', 'ジェラリー', 'クラレッド', 'シルヴァン', 'アルヴィン', 'トバイラス', 'パーシュア', 'メレデニス', 'クラレッグ', 'デルバジル', 'アンドニー', 'ヴァレッド']
passwords = ['5Vz140DtTl', '9ZxzUXDgQ7', 'Hkkx3P6SB3', 'u36a8Ecg4w', '0RM39G4Rq1', 'eTC1o1fOcE', 'bRXNCN0qfm', 'G89S0TH1He', 'lV59U040Sg', '6T4294b30s', 'Wr05QNlT6Y', 'QsAlVT50hc', 'kx2J4X9Kp6', '0y5bD4rr6u', 'fCIwO0A4S9', 'lc8lIlh5w0', 'TgIkw8zi6F', '0FsmT2C2KY', '7W0Q68u0Wl', '24a85YygHc', '6csf3A5V7O', 'B06TQa49S0', 'rzZZ3FBkEK', 'R4UHP4JUAH', '70IMMg2d6R', 'vc0Ay0pVv2', '0m2SKzoPsa', 'aZBHEghiRI', 'h640F7wsAY', 'ZI0280VW5g', 'pSO06VrqL6', 'hhNyp6fpO2', '2r03994F0p', '00d775B6oK', '6myLdO2oEq', '71LLhZaAy0', 'kpDF8ZUmWO', 'Sx2f807OFm', 'xcPOJWStu5', 'omQ3BP8tR8', 'BcEryV04e8', 'itM8QjhTbR', 'wxlo6K4s4T', 'v0Ntz0lQqR', 'KYswjD3uJ5', 'm7kLqHj9Kr', '2tBw0ppF17', 'zIhovgDsJI', 'r4d83f000J', 'LcwmIFub6f', '0Slmo4R89F', 'PSpH1AnCDJ', 'JisxLCu90m', 'gJihFmKGgo', '79Wo4dNVmu', '5SAwIGaqw6', 'KSK3XpLDCF', 'xFXm1AnYW2', 'NMFkGqQQ3s', 'EyLd0JiIMC', 'mzi00n2fb7', 'qayD00T96K', '3DrcRks39E', 'F8f10atHFq', '4RGKneD7n0', 'mL8iX428r0', 'Q1mLcl7DW2', 'KO00CuLr0G', 'hj927ETWBA', '5wn3SUc9bm', 'R2qa4FYwtN', 'X0Zol9BFXq', '0SJ3T19Ru6', 'YQTaGrO0uh', 'Db80JeZp39', 'dVBvP51VEB', '6y3nbXX9S6', 'TiDJ6V0D30', 'B6F271puS8', 'C6p1a1w42b', '00c046yAL0', '5k5j98CRG4', 'O2xOSG9M13', 'bReQdtoj4w', '0OTRSWfxPj', 'rn4aXLnBtD', 'mwk07019UE', '9F975DqtuR', '7UbTG1A5HA', '2x632pd3qK', '4lbPSaLy0d', 'F3Dx8xT4Wh', '3Oq0BBqjR8', '5xQOm80Ooj', 'bh0itAg719', '6r80xE74vu', '04uS9XItk0', '0q8nj7Go7l', 'xouQn0O5BB', 'CUtEUdtjF4']
for x in range(100):
    create_users(cur, names[x], passwords[x])
connection.commit()
connection.close()

# 店名といいねされた回数のデータベースを作成する
connection = sqlite3.connect("shops.sqlite3")
cur = connection.cursor()
cur.execute("CREATE TABLE shops(shop, nice)")
connection.commit()
connection.close()



