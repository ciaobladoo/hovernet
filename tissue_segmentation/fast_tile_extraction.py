import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from argparse import ArgumentParser
import os
import multiprocessing
from glob import glob
from tqdm import tqdm
import random

import openslide
import extract_tissue

parser = ArgumentParser()
parser.add_argument("folder", type=str)
parser.add_argument("--size", type=int, default=2048)
parser.add_argument("--mag", type=int, default=40)
parser.add_argument("--save", type=str)
parser.add_argument("--tmp",type=str)
args = parser.parse_args()

def extract_svs_tiles(slide_id):
    if os.path.exists(os.path.join(args.tmp, 'viz', os.path.basename(slide_id).split('.')[0]+'.png')):
        import sys
        sys.exit()
    slide = openslide.OpenSlide(os.path.join(args.folder, os.path.basename(slide_id)))
    grid,_ = extract_tissue.make_sample_grid(slide, patch_size=args.size, res=args.mag, min_cc_size=10, erode=True)
    thumb = slide.get_thumbnail((np.round(slide.dimensions[0]/50.), np.round(slide.dimensions[1]/50.)))

    ps = []
    for x,y in tqdm(grid, total=len(grid)):
        ps.append(patches.Rectangle((x/50., y/50.), args.size/50., args.size/50., fill=False, lw=0.3, edgecolor="red"))

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.imshow(thumb)
    ax.axis("off")
    for p in ps:
        ax.add_patch(p)

    plt.savefig(os.path.join(args.tmp, 'viz', os.path.basename(slide_id).split('.')[0]+'.png'), dpi=512, bbox_inches='tight')
    grid = random.sample(grid, min(len(grid),100))
    #pd.DataFrame(grid, columns=['x','y']).to_csv(os.path.join(args.tmp, 'grid', os.path.basename(args.slide).split(".")[0]+'.csv'), index=False)
    for idx, (x,y) in tqdm(enumerate(grid),total=len(grid)):
        reg = slide.read_region((x,y), 0, (args.size,args.size))
        reg.save(os.path.join(args.save, os.path.basename(slide_id).split(".")[0] + "_" + str(idx) + '.png'))


if __name__ == '__main__':
    os.makedirs(os.path.join(args.tmp,'viz'), exist_ok=True)
    slides = glob(os.path.join(args.folder, '*.svs'))
    with multiprocessing.Pool(40) as pool:
        pool.map(extract_svs_tiles, slides)
    #for slide in tqdm(slides):
    #    extract_svs_tiles(slide)

