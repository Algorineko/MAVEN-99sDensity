from training import LinearRegression
import torch

model = LinearRegression()

# 加载保存的模型权重
model.load_state_dict(torch.load('model/solar_distance_model.pth'))
model.eval()  # 设置模型为评估模式

solar_longitude=float(input())
solar_latitude=float(input())
spacecraft_longitude=float(input())
spacecraft_latitude=float(input())
altitude=float(input())

inputs = torch.tensor(
    [
    solar_longitude,
    solar_latitude,
    spacecraft_longitude,
    spacecraft_latitude,
    altitude
    ], dtype=torch.float32)

with torch.no_grad():
    predicted_distance = model(inputs)
    print(f"预测太阳距离为: {predicted_distance.item()}")



