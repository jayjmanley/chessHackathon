import h5py

# Open the GM boards.h5
lc0 = '/data/lc0/boards.h5'
gm = '/root/chess-hackathon/combined/gm/boards.h5'
with h5py.File(gm, 'r') as f:
    print(f.keys())  # List top-level datasets/groups
    for key in f.keys():
        print(key, f[key].shape, f[key].dtype)  # Inspect structure
