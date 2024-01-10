import math

def douglas_peucker(points, epsilon):
    # 寻找离起始点和结束点距离最远的点
    dmax = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        d = perpendicular_distance(points[i], points[0], points[end])
        if d > dmax:
            dmax = d
            index = i

    # 如果最远距离大于阈值epsilon，则递归地对子段进行压缩
    result = []
    if dmax > epsilon:
        rec_results1 = douglas_peucker(points[:index + 1], epsilon)
        rec_results2 = douglas_peucker(points[index:], epsilon)
        result = rec_results1[:-1] + rec_results2
    else:
        result = [points[0], points[end]]

    return result

def perpendicular_distance(point, start, end):
    # 计算点到起始点和结束点连线的垂直距离
    numerator = abs(
        (end[1] - start[1]) * point[0] - (end[0] - start[0]) * point[1] + end[0] * start[1] - end[1] * start[0])
    denominator = math.sqrt((end[1] - start[1]) ** 2 + (end[0] - start[0]) ** 2)
    distance = numerator / denominator
    return distance

def batch_douglas_peucker(point_sets, epsilon):
    compressed_sets = []
    for points in point_sets:
        compressed_points = douglas_peucker(points, epsilon)
        compressed_sets.append(compressed_points)
    return compressed_sets

# 示例数据
point_sets = [
    [(0, 0), (1, 1), (2, 2), (3, 1), (4, 0)],
    [(0, 0), (2, 2), (4, 4), (6, 2), (8, 0)],
    [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
]
epsilon = 1.0  # 设置阈值

compressed_sets = batch_douglas_peucker(point_sets, epsilon)
for compressed_points in compressed_sets:
    print(compressed_points)