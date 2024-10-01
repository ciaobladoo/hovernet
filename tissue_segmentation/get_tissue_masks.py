import os
import cv2
from argparse import ArgumentParser
import openslide
import extract_tissue

SIZE = 256
MAG = 20

parser = ArgumentParser()
parser.add_argument("slide", type=str)
parser.add_argument("--save", type=str)
args = parser.parse_args()


slide = openslide.OpenSlide(args.slide)
overlay = extract_tissue.save_mask(slide, patch_size=SIZE, res=MAG, min_cc_size=10, erode=True)
cv2.imwrite(os.path.join(args.save, '{}.png'.format(os.path.basename(args.slide).strip('.svs'))), overlay)

