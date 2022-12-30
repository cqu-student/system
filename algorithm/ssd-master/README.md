# pytorch_ssd
Pytorch Implemetation of Single Shot Detector (SSD). The initial project is build upon the work done by [lufficc/SSD](https://github.com/lufficc/SSD/). The project as of now is designed to be used only for prediction on images. Video implementation is work in progress. 

## Requirements
  - Python 3.6
  - PyTorch 1.0
  - yacs
  - GCC >= 5
  - OpenCV v4.0.0
  
## How to use

First make sure the requirements are installed in your virtual environmet or system. 

```
sudo pip3 install -r requirements.txt
```
Once the requirements are installed, we need the weights file to predict on the image. Weights trained by Lufficc/SSD are as below

|         |    Weights   |
| :-----: | :----------: |
| SSD300* | [ssd300_voc0712_mAP77.83.pth(100 MB)](https://github.com/lufficc/SSD/releases/download/v1.0.1/ssd300_voc0712_mAP77.83.pth) |
| SSD512* | [ssd512_voc0712_mAP80.25.pth(104 MB)](https://github.com/lufficc/SSD/releases/download/v1.0.1/ssd512_voc0712_mAP80.25.pth) |

Add the path of the weights file and the SSD Type(300/512) to the *hyper_params.json* file.

You can run the program as
```
python3 detect.py
```

