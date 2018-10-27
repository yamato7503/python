your_point = input('点数をカンマ区切りで入力してください： ')
point_list = your_point.split(',')
total = 0

for point in point_list:
    total += int(point)
print(total)