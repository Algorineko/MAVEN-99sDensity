from train import Model
import torch

model = Model()

# 加载保存的模型权重
model.load_state_dict(torch.load(r'model/99sDensity_model.pth'))
model.eval()  # 设置模型为评估模式

txt_file_path = r'./testData/validationData.txt'
data=[]
with open(txt_file_path, 'r') as file:
    for line in file:
        data = [float(value) for value in line.split()]
        # print(data)

Seconds_from_Periapsis=float(data[0])
Areodetic_Latitude=float(data[1])
Longitude=float(data[2])
True_Local_Solar_Time=float(data[3])
Solar_Zenith_Angle=float(data[4])
AREODETIC_ALTITUDE=float(data[5])
_99_SEC_DENSITY=float(data[6])
SIGMA_99_SEC_DENSITY=float(data[7])
_1_SEC_DENSITY=float(data[8])
SIGMA_1_SEC_DENSITY=float(data[9])
SPACECRAFT_MASS=float(data[10])
BIAS_NOISE_1_SIGMA=float(data[11])

arr=[
        Areodetic_Latitude,
        Longitude,
        True_Local_Solar_Time,
        Solar_Zenith_Angle,
        AREODETIC_ALTITUDE,
        SIGMA_99_SEC_DENSITY,
        _1_SEC_DENSITY,
        SIGMA_1_SEC_DENSITY,
        SPACECRAFT_MASS,
        BIAS_NOISE_1_SIGMA,
    ]
# print(arr)

inputs=torch.tensor([arr], dtype=torch.float32)

true_ans=_99_SEC_DENSITY
with torch.no_grad():
    prediction = model(inputs)
    ans=prediction.item()
    print(f"99sDensity预测值为: {ans}")
    print(f"99sDensity真实值为: {true_ans}")
    print(f"绝对误差为:{abs(ans-true_ans)}")
    if true_ans!=0:
        print(f"相对误差为:{(abs(ans-true_ans)/true_ans)*100}%")
