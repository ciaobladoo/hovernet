import os
import cv2
from argparse import ArgumentParser
os.add_dll_directory("C:/Users/chfe/Documents/tools/openslide-win64-20230414/bin")
import openslide
import extract_tissue

SIZE = 256
MAG = 40

parser = ArgumentParser()
parser.add_argument("slide", type=str)
parser.add_argument("--save", type=str)
args = parser.parse_args()


slide = openslide.OpenSlide(args.slide)
overlay = extract_tissue.save_mask(slide, patch_size=SIZE, res=MAG, min_cc_size=10)
cv2.imwrite(os.path.join(args.save, '{}.png'.format(os.path.basename(args.slide).strip('.svs'))), overlay)

