import torch

def inspect_dtype(dtype):
    info=torch.finfo(dtype)
    return {'tiny':info.tiny,'eps':info.eps,'max':info.max}
