# データから必要なカラムを抜き出し、新たなcsvファイル
import pandas as pd

df_info = pd.read_csv("data_csv/info.csv", encoding="shift-jis")
print(df_info.columns)

print("作業を開始します")

new_columns = [
    'レースコード', 
    '1枠_艇番', '1枠_登録番号', '1枠_選手名', '1枠_年齢', '1枠_支部', '1枠_体重', '1枠_級別',
    '1枠_全国勝率', '1枠_全国2連対率', '1枠_当地勝率', '1枠_当地2連対率',
    '1枠_モーター番号', '1枠_モーター2連対率', '1枠_ボート番号', '1枠_ボート2連対率',
    '2枠_艇番', '2枠_登録番号', '2枠_選手名', '2枠_年齢', '2枠_支部', '2枠_体重', '2枠_級別',
    '2枠_全国勝率', '2枠_全国2連対率', '2枠_当地勝率', '2枠_当地2連対率',
    '2枠_モーター番号', '2枠_モーター2連対率', '2枠_ボート番号', '2枠_ボート2連対率',
    '3枠_艇番', '3枠_登録番号', '3枠_選手名', '3枠_年齢', '3枠_支部', '3枠_体重', '3枠_級別',
    '3枠_全国勝率', '3枠_全国2連対率', '3枠_当地勝率', '3枠_当地2連対率',
    '3枠_モーター番号', '3枠_モーター2連対率', '3枠_ボート番号', '3枠_ボート2連対率',
    '4枠_艇番', '4枠_登録番号', '4枠_選手名', '4枠_年齢', '4枠_支部', '4枠_体重', '4枠_級別',
    '4枠_全国勝率', '4枠_全国2連対率', '4枠_当地勝率', '4枠_当地2連対率',
    '4枠_モーター番号', '4枠_モーター2連対率', '4枠_ボート番号', '4枠_ボート2連対率',
    '5枠_艇番', '5枠_登録番号', '5枠_選手名', '5枠_年齢', '5枠_支部', '5枠_体重', '5枠_級別',
    '5枠_全国勝率', '5枠_全国2連対率', '5枠_当地勝率', '5枠_当地2連対率',
    '5枠_モーター番号', '5枠_モーター2連対率', '5枠_ボート番号', '5枠_ボート2連対率',
    '6枠_艇番', '6枠_登録番号', '6枠_選手名', '6枠_年齢', '6枠_支部', '6枠_体重', '6枠_級別',
    '6枠_全国勝率', '6枠_全国2連対率', '6枠_当地勝率', '6枠_当地2連対率',
    '6枠_モーター番号', '6枠_モーター2連対率', '6枠_ボート番号', '6枠_ボート2連対率'
]

df_new_info = df_info[new_columns]
df_new_info.to_csv("data_csv/new_info.csv", index=False)

print("作業を終了しました")
