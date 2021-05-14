import cv2
# import pandas as pd
import json
import os
 
# ground-truth
def select(json_path, outpath, image_path):
    json_file = open(json_path)
    infos = json.load(json_file)
    images = infos["images"]
    annos = infos["annotations"]
    assert len(images) == len(images)
    # import pdb;pdb.set_trace()
    for i in range(len(images)):
        im_id = images[i]["id"]
        im_path = image_path + images[i]["file_name"]
        img = cv2.imread(im_path)
        for j in range(len(annos)):
            if annos[j]["image_id"] == im_id:
                x, y, w, h = annos[j]["bbox"]
                x, y, w, h = int(x), int(y), int(w), int(h)
                x2, y2 = x + w, y + h
                # object_name = annos[j][""]
                img = cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), thickness=1)
                img_name = outpath + images[i]["file_name"]
                # import pdb;pdb.set_trace()
                cv2.imwrite(img_name, img)
                # continue
        # print(i)
    print("Done!")

# predict
# def select(json_path, outpath, image_path):
#     json_file = open(json_path)
#     infos = json.load(json_file)
#     for i in range(len(infos)):
#         im_id = infos[i]["image_id"]
#         im_path = image_path + str(infos[i]["image_id"]) + '.jpg' 
#         # import pdb;pdb.set_trace()
#         img_name = outpath + str(infos[i]["image_id"]) + '.jpg'
#         score = str(infos[i]["score"])
#         if not os.path.exists(img_name):
#             img = cv2.imread(im_path)
#         else: 
#             img = cv2.imread(img_name)
#         # if float(score) < 0.5:
#         #     continue
#         # else:
#         x, y, w, h = infos[i]["bbox"]
#         x, y, w, h = int(x), int(y), int(w), int(h)
#         x2, y2 = x + w, y + h
#         c_x, c_y = int((x + x2) / 2), int((y + y2) / 2)
#         cla = str(infos[i]["category_id"])
#         # import pdb;pdb.set_trace()
#         # img = cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 255), thickness=2)
#         if float(score) <= 0.3:
#             cv2.circle(img, (c_x, c_y), 5, (0,0,int(255*float(score))), -1) # red
#             continue
#         elif float(score) > 0.3 and float(score) <= 0.6:
#             cv2.circle(img, (c_x, c_y), 5, (int(255*float(score)),255,0), -1)  # green
#         elif float(score) > 0.6:
#             cv2.circle(img, (c_x, c_y), 5, (0,int(255*float(score)),255), -1)   # yellow
#             # cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), thickness=2)
#             # cv2.putText(img, score, (x, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#             # cv2.putText(img, cla,(c_x, c_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         img_name = outpath + str(infos[i]["image_id"]) + '.jpg'
#         # import pdb;pdb.set_trace()
#         cv2.imwrite(img_name, img)
#     print("Done!")


if __name__ == "__main__":
    json_path = "/home/jjliao/faceDetection/data/wider_coco/annotations/val.json"
    out_path = "/home/jjliao/faceDetection/data/json_output/"
    image_path = "/home/jjliao/faceDetection/data/wider_coco/images/val/"
    select(json_path, out_path, image_path)

