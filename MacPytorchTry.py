import torch

# 检查是否可以使用Metal加速
print(torch.backends.mps.is_available())

# 检查MPS后端是否可用
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

# 创建张量并移动到MPS设备
x = torch.randn(3, 3).to(device)
print(x)
