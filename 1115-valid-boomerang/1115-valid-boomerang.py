def slope(x1, y1, x2, y2):
    if (x2 - x1) == 0:
        return "undefined"
    print("num")
    print(x1)
    print(y1)
    print(x2)
    print(y2)
    slope = 0.5
    slope = (y2 - y1) / (x2 - x1)
    return slope

def closeEnough(a, b):
    margin = 0.000001
    if a >= b - margin and a <= b + margin:
        return True
    else:
        return False


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        x1 = float(p1[0])
        y1 = float(p1[1])

        x2 = float(p2[0])
        y2 = float(p2[1])

        x3 = float(p3[0])
        y3 = float(p3[1])


        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        
        dis = lambda x1, y1, x2, y2 : ((x2-x1)**2 + (y2-y1)**2)**0.5

        # y = mx + b
        m = slope(x1, y1, x2, y2)

        if m == "undefined":
            if x1 == x2 and x2 == x3 and x1 == x3:
                return False
            else:
                return True

        print(m)

        b = y1 - (m * x1)

        print("b = " + str(b))

        if closeEnough(y3, (m * x3 + b)):
            print("boop")
            return False
        else:
            print("beep")
            print(y3)
            print(m * x3 + b)
            return True