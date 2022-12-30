import glob
import os
import torch
from PIL import Image
from tqdm import tqdm

from ssd.config import cfg
from ssd.data.datasets import COCODataset, VOCDataset
from ssd.modeling.predictor import Predictor
from ssd.modeling.vgg_ssd import build_ssd_model

import argparse
import numpy as np
import json

from ssd.utils.viz import draw_bounding_boxes


def detect(cfg, weights_file, iou_threshold, score_threshold, images_dir, output_dir, dataset_type):
    
    if dataset_type == "voc":
        class_names = VOCDataset.class_names
    elif dataset_type == 'coco':
        class_names = COCODataset.class_names
    else:
        raise NotImplementedError('Not implemented now.')

    device = torch.device(cfg.MODEL.DEVICE)
    model = build_ssd_model(cfg)
    model.load(weights_file)
    print('Loaded weights from {}.'.format(weights_file))
    
    model = model.to(device)
    
    predictor = Predictor(cfg=cfg,
                          model=model,
                          iou_threshold=iou_threshold,
                          score_threshold=score_threshold,
                          device=device)
    
    cpu_device = torch.device("cpu")

    
    image_paths = glob.glob(os.path.join(images_dir, '*.jpg'))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_path in tqdm(image_paths):
        image = Image.open(image_path).convert("RGB")
        image = np.array(image)
        output = predictor.predict(image)
        boxes, labels, scores = [o.to(cpu_device).numpy() for o in output]
        drawn_image = draw_bounding_boxes(image, boxes, labels, scores, class_names).astype(np.uint8)
        image_name = os.path.basename(image_path)
        Image.fromarray(drawn_image).save(os.path.join(output_dir, image_name))


def main():

    with open("hyper_params.json") as hp:
        data = json.load(hp)
        config_file = data["configfile"]
        weights = data["weight"]
        images_dir = data["ImgDir"]
        output_dir = data["OutDir"]
        iou_threshold = data["iou"]
        score_threshold = data["score"]
        dataset_type = data["SSD_Type"]
        
    opts = []
    cfg.merge_from_file(config_file)
    cfg.merge_from_list(opts)
    cfg.freeze()

    detect(cfg=cfg,
             weights_file=weights,
             iou_threshold=iou_threshold,
             score_threshold=score_threshold,
             images_dir=images_dir,
             output_dir=output_dir,
             dataset_type=dataset_type)


if __name__ == '__main__':
    main()
