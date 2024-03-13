# -*- coding: utf-8 -*-

import os
import cv2
import json
import numpy as np


def load_annotations(annotation_file):
    with open(annotation_file, 'r', encoding="utf-8") as f:
        annotations = json.load(f)
    return annotations


def process_frame(frame_path, contours):
    frame = cv2.imread(frame_path)
    # mask = np.zeros_like(frame, dtype=np.uint8)
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [np.array(contour).reshape(-1, 2) for contour in contours], contourIdx=-1, color=255,
                     thickness=-1)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result


def main(video_frames_folder, annotation_file, output_folder, file):
    annotations = load_annotations(annotation_file)

    frame_obj = annotations.get('objs', {})

    for obj_id, frame_data in frame_obj.items():

        for frame_count, frame_info in frame_data.items():
            if frame_info and isinstance(frame_info, list):
                contours = frame_info
                # print(contours)
                # input()
            elif frame_info and isinstance(frame_info, dict):
                contours = frame_info.get("contours", [])
            else:
                contours = []

            frame_path = os.path.join(video_frames_folder, f"{frame_count.zfill(6)}.jpg")
            output_path = os.path.join(output_folder,
                                       f"{file.replace('_anno', '')}_{frame_count.zfill(6)}_processed.jpg")

            if os.path.exists(frame_path):
                processed_frame = process_frame(frame_path, contours)
                cv2.imwrite(output_path, processed_frame)
                print(f"Processed {frame_path} and saved to {output_path}")
            else:
                print(f"Frame {frame_path} not found.")


if __name__ == "__main__":
    root_folder = r"/mnt/nas0-pool0/datasets/Pharmacy_for_label/"
    output_folder = "/mnt/nas0-pool0/personal/zhouzihao/datasets/output/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for subdir, dirs, files in os.walk(root_folder):
        for file in files:

            if file.endswith("_anno.json"):
                annotation_file = os.path.join(subdir, file)

                video_frames_folder = os.path.join(subdir, 'images')
                # print(video_frames_folder)
                main(video_frames_folder, annotation_file, output_folder, file)