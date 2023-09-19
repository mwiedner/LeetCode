def areaCalc(point1, point2, point3):
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    x3 = point3[0]
    y3 = point3[1]

    # Negative correction cringe
    while x1 < 0 or x2 < 0 or x3 < 0 or y1 < 0 or y2 < 0 or y3 < 0:
        x1 += 100
        x2 += 100
        x3 += 100

        y1 += 100
        y2 += 100
        y3 += 100

    dis = lambda xa, xb, ya, yb: ((xb - xa)**2 + (yb - ya)**2)**0.5

    l1 = dis(x1, x2, y1, y2)
    l2 = dis(x2, x3, y2, y3)
    l3 = dis(x3, x1, y3, y1)

    s = (l1 + l2 + l3) / 2

    try:
        area = (s * (s - l1) * (s - l2) * (s - l3))**0.5
        return area
    except ValueError:
        print("fjdsa")
    

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        bigboy = 0

        i = 0
        while i < len(points):
            j = 0
            while j < len(points):
                k = 0
                while k < len(points):
                    if areaCalc(points[i], points[j], points[k]) > bigboy:
                        bigboy = areaCalc(points[i], points[j], points[k])
                    k+=1
                j+=1
            i+=1
        return bigboy