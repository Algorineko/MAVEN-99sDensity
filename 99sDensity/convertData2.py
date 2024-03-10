import csv

tab_file_path = r'./rawData/2014/10/mvn_acc_l3_pro-acc-p00049_20141007_v02_r01.tab.txt'
csv_file_path = r'./data/2014/10/20141007.csv'

with open(tab_file_path, 'r') as tab_file, open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # 设置分隔符为一个空格
    tab_reader = csv.reader((line.replace('\t', ' ') for line in tab_file), delimiter=' ')
    csv_writer = csv.writer(csv_file)

    # 写入列标题
    csv_writer.writerow([
        'Seconds from Periapsis',
        'Areodetic Latitude',
        'Longitude',
        'True Local Solar Time',
        'Solar Zenith Angle',
        'AREODETIC ALTITUDE',
        '99-SEC DENSITY',
        'SIGMA 99-SEC DENSITY',
        '1-SEC DENSITY',
        'SIGMA 1-SEC DENSITY',
        'SPACECRAFT MASS',
        'BIAS NOISE 1-SIGMA'
    ])

    # 读取tab文件并写入csv文件
    for row in tab_reader:
        # 过滤掉空白行和连续的空格
        filtered_row = [field for field in row if field != '']
        if filtered_row:
            csv_writer.writerow(filtered_row)

print(f'数据已从 {tab_file_path} 转移到 {csv_file_path}')
