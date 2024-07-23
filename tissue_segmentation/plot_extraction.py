import os
from tqdm import  tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from argparse import ArgumentParser
os.add_dll_directory("C:/Users/chfe/Documents/tools/openslide-win64-20230414/bin")
import openslide
import extract_tissue

SIZE = 256
MAG = 20

parser = ArgumentParser()
parser.add_argument("slide", type=str)
parser.add_argument("--save", type=str)
args = parser.parse_args()


slide = openslide.OpenSlide(args.slide)
grid,_ = extract_tissue.make_sample_grid(slide, patch_size=SIZE, res=MAG, min_cc_size=0, erode=True)
thumb = slide.get_thumbnail((np.round(slide.dimensions[0]/50.), np.round(slide.dimensions[1]/50.)))

ps = []
for x,y in tqdm(grid, total=len(grid)):
    ps.append(patches.Rectangle(
        (x/50., y/50.), SIZE/50., SIZE/50., fill=False, lw=0.3,
        edgecolor="red"))

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.imshow(thumb)
ax.axis("off")
for p in ps:
    ax.add_patch(p)
plt.savefig(os.path.join(args.save, os.path.basename(args.slide).split('.')[0]+'.png'),dpi=512,bbox_inches='tight')
