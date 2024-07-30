# SWS(SimAM With Slicing) Attention 
for Small object detection

<div align="center">
    <a href="./">
        <img src="sws_fig.jpg" width="80%"/>
    </a>
</div>

## Abstract
SimAM is a feature enhancement module without neural networks, offering the advantage of being lightweight and demonstrating potential in improving recognition performance. Based on this, we developed the new module SWS. The reason for incorporating the "slicing" operation is that when SimAM calculates the average pixel difference of the entire feature map, weighting may overlook the importance of small objects. Small objects occupy a relatively small proportion in aerial images and may be similar to background information compared to the overall average value, resulting in weaker weighting enhancement and consequently poorer enhancement ability of SimAM for small objects.

Therefore, we introduced a slicing operation. when the feature map is sliced into different blocks, larger objects, due to their prominent texture features, influence the average value of the block they are in, reducing the additional weighting they receive. After merging the feature maps, larger objects can still maintain high recognizability and may even be further enhanced. In contrast, the features of smaller objects differ more from the local average value, resulting in more weighting and enhanced small object features. In other words, the SWS module ensures that both large and small objects receive fair attention and enhancement.

### VisDrone2019-testset-dev Evaluation
#### Detection base on PRB-FPN-ELAN [(here)](https://github.com/pingyang1117/PRBNet_PyTorch)
|Model           |mAP50      |mAP50-95   |P    |R        |F1-score  |Prams |
|:----:          |:----:     |:---:      |:--: |:----:   |:---:     |:--: |
|base            |39.5       |22.0       |49.9 |43.0     |46.2      |- |
|SimAM           |39.4       |22.0       |51.2 |42.1     |46.2      |+460K |
|Coordinate      |39.6       |22.2       |49.7 |43.6     |46.5      |+560K |
|SE              |39.7       |22.2       |49.1 |43.8     |46.3      |+590K |
|CBAM            |39.7       |22.1       |53.0 |41.3     |46.4      |+590K |
|Biformer        |39.8       |22.2       |48.1 |44.6     |46.3      |+4.67M |
|SWS(Ours)       |39.9       |22.3       |53.3 |41.7     |46.8      |+460K |
