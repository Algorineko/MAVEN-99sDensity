import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

# data = pd.read_csv(r'./testData/testdata.csv')
data = pd.read_csv(r'./testData/testdata.csv')

train_data = data.sample(frac=0.8, random_state=923)
test_data = data.drop(train_data.index)

# 输出非空总数
# print(f"isnull:\n{train_data.isnull().sum()}")

# Seconds from Periapsis 类型是object,舍弃
train_data = train_data.drop(columns=['Seconds from Periapsis'])
test_data = test_data.drop(columns=['Seconds from Periapsis'])
# print(train_data.dtypes)
train_data = train_data.fillna(train_data.mean())

X_train = torch.Tensor(train_data.drop(columns=['99-SEC DENSITY']).values)
y_train = torch.Tensor(train_data['99-SEC DENSITY'].values)

# print(X_train.max(), X_train.min())
# print(y_train.max(), y_train.min())

class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.fc = nn.Linear(X_train.shape[1], 1)

    def forward(self, x):
        return self.fc(x)

model = LinearRegression()

# 损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.005)

# 训练模型
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(torch.Tensor(X_train))
    loss = criterion(outputs, torch.Tensor(y_train).unsqueeze(1))
    # 梯度剪裁
    nn.utils.clip_grad_value_(model.parameters(), clip_value=1.0)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/100] --- Loss: {loss.item():.4f}")

X_test = test_data.drop(columns=['99-SEC DENSITY']).values
y_test = test_data['99-SEC DENSITY'].values
with torch.no_grad():
    test_outputs = model(torch.Tensor(X_test))
    test_loss = criterion(test_outputs, torch.Tensor(y_test).unsqueeze(1))
    print(f'Final Loss: {test_loss.item():.4f}')
