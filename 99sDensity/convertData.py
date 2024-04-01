import csv
import glob
import os

# tab_file_path = r'./rawData/2014/10/mvn_acc_l3_pro-acc-p00077_20141012_v02_r01.tab'
csv_file_path = r'./testData/testData.csv'
folder_path = r'./rawData/2014/10'
isRecursive=True

with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # 若为空则写入列标题
    if os.stat(csv_file_path).st_size == 0:
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

# recursive为文件夹是否递归查找,开启递归需要注意加"**"
tab_files = glob.glob(os.path.join(folder_path, '**/*.tab'), recursive=isRecursive)
tab_files = [p.replace("\\","/") for p in tab_files]

cnt=0
for tab_file_path in tab_files:
    with open(tab_file_path, 'r') as tab_file, open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        # 设置分隔符为一个空格
        tab_reader = csv.reader((line.replace('\t', ' ') for line in tab_file), delimiter=' ')
        csv_writer = csv.writer(csv_file)
        # 读取tab文件并写入csv文件
        for row in tab_reader:
            # 过滤掉空白行和连续的空格
            filtered_row = [field for field in row if field != '']
            if filtered_row:
                csv_writer.writerow(filtered_row)
    cnt+=1
    print(f'已处理完{cnt}个tab文件')
