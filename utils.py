# utils.py
import random
import numpy as np
import torch
import os

def set_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    print(f"Seeds set to {seed}")

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    print(f"Directory ensured: {directory}")