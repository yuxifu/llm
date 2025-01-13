# import torch and print the version
import torch
print("torch version: " + torch.__version__)

# check if Apple GPU is available
device = torch.device("cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA device seleted.")
elif torch.mps.is_available():
    device = torch.device("mps")
    print("MPS device seleted.")
else:
    print ("CPU device seleted.")

# print the device type
print("device type: " + device.type)
