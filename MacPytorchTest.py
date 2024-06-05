import torch

# Check if Metal is available
# 检查是否可以使用Metal加速
print(torch.backends.mps.is_available())

# Check if MPS backend is available
# 检查MPS后端是否可用 
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print("Device:"+str(device))
# Create a tensor and move it to the MPS device
# 创建张量并移动到MPS设备 
x=torch.tensor([[1,2,3],[4,5,8],[9,8,7]]).to(device)
# x = torch.randn(3, 3).to(device)
print(x)
