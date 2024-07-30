# SWS((SimAM With Slicing)) Attention

<div align="center">
    <a href="./">
        <img src="sws_fig.jpg" width="80%"/>
    </a>
</div>

## Abstract
SimAM is a feature enhancement module without neural networks, offering the advantage of being lightweight and demonstrating potential in improving recognition performance. Based on this, we developed the new module SWS. The reason for incorporating the "slicing" operation is that when SimAM calculates the average pixel difference of the entire feature map, weighting may overlook the importance of small objects. Small objects occupy a relatively small proportion in aerial images and may be similar to background information compared to the overall average value, resulting in weaker weighting enhancement and consequently poorer enhancement ability of SimAM for small objects.

Therefore, we introduced a slicing operation. when the feature map is sliced into different blocks, larger objects, due to their prominent texture features, influence the average value of the block they are in, reducing the additional weighting they receive. After merging the feature maps, larger objects can still maintain high recognizability and may even be further enhanced. In contrast, the features of smaller objects differ more from the local average value, resulting in more weighting and enhanced small object features. In other words, the SWS module ensures that both large and small objects receive fair attention and enhancement.
