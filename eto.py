year_str = input('あなたの生まれ年を西暦４桁で入力してください：　')
year = int(year_str) # 西暦を数値に変換する
number_of_eto = (year + 8) % 12
print('あなたの干支の順番は', number_of_eto + 1, '番です。')
eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
eto_name = eto_list[number_of_eto]
print('あなたの干支は', eto_name, 'です。')
