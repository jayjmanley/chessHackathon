import h5py
import numpy as np

# Open GM and LC0 boards.h5
gm_file = h5py.File('/root/chess-hackathon/combined/gm/boards.h5', 'r')
lc0_file = h5py.File('/data/lc0/boards.h5', 'r')

# Create a new combined file
combined_file = h5py.File('/root/chess-hackathon/combined/boards.h5', 'w')

# Copy GM data with a prefix
for key in gm_file.keys():
    combined_file.create_dataset(f'gm_{key}', data=gm_file[key][...])

# Copy LC0 data with a prefix
for key in lc0_file.keys():
    combined_file.create_dataset(f'lc0_{key}', data=lc0_file[key][...])

# Close files
gm_file.close()
lc0_file.close()
combined_file.close()
