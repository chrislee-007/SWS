# SWS((SimAM With Slicing)) Attention

<div align="center">
    <a href="./">
        <img src="sws_fig.jpg" width="80%"/>
    </a>
</div>

## Abstract
SimAM is a feature enhancement module without neural networks, offering the advantage of being lightweight and demonstrating potential in improving recognition performance. Based on this, we developed the new module SWS. The reason for incorporating the "slicing" operation is that when SimAM calculates the average pixel difference of the entire feature map, weighting may overlook the importance of small objects. Small objects occupy a relatively small proportion in aerial images and may be similar to background information compared to the overall average value, resulting in weaker weighting enhancement and consequently poorer enhancement ability of SimAM for small objects.

Therefore, we introduced a slicing operation. when the feature map is sliced into different blocks, larger objects, due to their prominent texture features, influence the average value of the block they are in, reducing the additional weighting they receive. After merging the feature maps, larger objects can still maintain high recognizability and may even be further enhanced. In contrast, the features of smaller objects differ more from the local average value, resulting in more weighting and enhanced small object features. In other words, the SWS module ensures that both large and small objects receive fair attention and enhancement.

### VisDrone2019-testset-dev Evaluation
#### Detection with PRB-FPN-ELAN [(here)](https://github.com/pingyang1117/PRBNet_PyTorch)

|Model          |AP     |AP_50      |AP_75|AP_S     |AP_M      |AP_L |
|:----:         |:----: |:---:      |:--: |:----:   |:---:     |:--: |
|SimAM   |39.2   |60.7       |40.8 |22.8     |43.0      |50.6 |
|Coordinate  |41.2   |62.4       |45.0 |24.0     |45.6      |52.8 |
|SE   |39.8   |61.0       |43.4 |23.1     |43.7      |51.4 |
|CBAM  |41.8   |62.8       |46.0 |24.8     |46.2      |53.9 |
