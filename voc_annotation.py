import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor", "rummy o"]


def convert_annotation(year, image_id, list_file):
    ## in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    in_file = open('../rummy-data-backup/convert_YOLO_to_VOC/converted_labels/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        # cls_id = 21
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    # image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    image_ids = open('../rummy-data-backup/convert_YOLO_to_VOC/%s.txt'%(image_set)).read().strip().split()
    # list_file = open('%s_%s.txt'%(year, image_set), 'w')
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('../rummy-data-backup/convert_YOLO_to_VOC/images/%s.jpg'%(image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

