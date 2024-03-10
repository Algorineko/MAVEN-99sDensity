import pandas as pd


tab_file_path = r'./rawData/2014/10/mvn_acc_l3_pro-acc-p00056_20141008_v02_r01.tab.txt'
csv_file_path = r'./data/2014/10/20141007.csv'

new_data = pd.read_csv(tab_file_path, delimiter='\t')
new_data.to_csv(csv_file_path, mode='a', header=False, index=False)

print("数据已附加成功")