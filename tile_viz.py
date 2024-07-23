import os
import json
from misc.viz_utils import visualize_instances_dict
from PIL import Image
from tqdm import tqdm
import pandas as pd
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("img", type=str)
parser.add_argument("--json", type=str)
parser.add_argument("--save", type=str)
parser.add_argument("--dic", type=str)
args = parser.parse_args()


imgs = os.listdir(args.img)
#dic = pd.read_csv(args.dic)
for img_name in tqdm(imgs):
    img_name_list = img_name.split('_')
    #img_name_key = '_'.join(img_name_list[:-1]) + '.ome.tiff'
    #json_name = dic[dic['cd3a'] == img_name_key].iloc[0]['grid'].strip('.csv')
    #json_name = '_'.join([json_name, img_name_list[-1]]).replace('.png','.json')
    json_name = '_'.join(img_name_list[:-1]+[img_name_list[-1].split('.')[0]]+['fake'])+'.json'
    img = Image.open(os.path.join(args.img, img_name))
    imp = json.load(open(os.path.join(args.json, json_name)))['nuc']
    overlay = visualize_instances_dict(img, imp, type_colour=None)
    Image.fromarray(overlay).save(os.path.join(args.save, img_name), dpi=(256,256))

