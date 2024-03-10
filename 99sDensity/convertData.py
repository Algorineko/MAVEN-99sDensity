# 不适用,使用convertData2
import csv

tab_file_path = r'./rawData/2014/10/mvn_acc_l3_pro-acc-p00049_20141007_v02_r01.tab.txt'
csv_file_path = r'./data/2014/10/20141007.csv'

with open(tab_file_path, 'r') as tab_file, open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    tab_reader = csv.reader(tab_file, delimiter='\t')
    csv_writer = csv.writer(csv_file)
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
    for row in tab_reader:
        csv_writer.writerow(row)

print(f'数据已从 {tab_file_path} 转移到 {csv_file_path}')
