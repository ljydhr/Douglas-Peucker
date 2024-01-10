# Douglas-Peucker
一种常用的轨迹压缩算法，用于减少轨迹数据中的冗余点，提取出关键的特征点；A commonly used trajectory compression algorithm is used to reduce redundant points in trajectory data and extract key feature points.
算法的步骤如下：
1.给定一个轨迹数据集，其中包含一系列的点构成的轨迹曲线。
2.连接轨迹曲线的起点和终点，形成一条直线段。
3.找到曲线上离该直线段距离最远的点，记为C，计算其与直线段的垂直距离d。
4.如果距离d大于预设的阈值（限差），则将轨迹曲线分成两部分：AC和CB。
5.对AC和CB两部分分别递归执行步骤2~4，直到所有的垂直距离都小于阈值，停止递归。
6.当递归结束后，从起点到终点经过的所有分割点即为提取的特征点，它们可以用来近似表示原始轨迹。
Douglas-Peucker算法通过不断划分轨迹曲线，找到与直线段距离最远的点，并与阈值进行比较，从而决定是否保留该点。通过递归的方式，算法能够在保持轨迹形状的前提下，大大减少数据点的数量，从而实现轨迹的压缩和特征提取。
