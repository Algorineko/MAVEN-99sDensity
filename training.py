import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim

# 加载数据集
class SolarDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        inputs = torch.tensor(self.data.iloc[idx, 1:6].values, dtype=torch.float32)
        target = torch.tensor(self.data.iloc[idx, 6], dtype=torch.float32)
        return inputs, target

dataset = SolarDataset('data/processed_data.csv')
train_loader = DataLoader(dataset=dataset, batch_size=5, shuffle=True)

# 线性回归模型
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(5, 1)
    def forward(self, x):
        return self.linear(x)
if __name__ == "__main__":
    model = LinearRegression()

    # 损失函数和优化器
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # 训练模型
    epochs=100
    for epoch in range(epochs):
        for i, data in enumerate(train_loader):
            inputs, target = data
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, target.unsqueeze(1))
            loss.backward()
            optimizer.step()
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{epochs}]')

    print('训练完成')
    torch.save(model.state_dict(), 'model/solar_distance_model.pth')
    print('保存成功')
    # 训练时长约 6:10


