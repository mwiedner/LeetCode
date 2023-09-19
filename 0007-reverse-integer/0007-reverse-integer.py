class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x*=-1
        
        poop = 2**31 - 1
        strpoop = str(poop)
        print(strpoop)
        strpoop = strpoop[::-1]
        print(strpoop)


        xStr = str(x)
        lengthX = len(xStr)

        error = False
        

        if lengthX == 10:
            print("a")
            error = True

            if int(xStr[9]) < 2:
                print("ba")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) < 1:
                print("ca")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) < 4:
                print("da")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) < 7:
                print("ea")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) < 4:
                print("fa")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) == 4 and int(xStr[4]) < 8:
                print("ga")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) == 4 and int(xStr[4]) == 8 and int(xStr[3]) < 3:
                print("ha")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) == 4 and int(xStr[4]) == 8 and int(xStr[3]) == 3 and int(xStr[2]) < 6:
                print("ia")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) == 4 and int(xStr[4]) == 8 and int(xStr[3]) == 3 and int(xStr[2]) == 6 and int(xStr[1]) < 4:
                print("ja")
                error = False
            if int(xStr[9]) == 2 and int(xStr[8]) == 1 and int(xStr[7]) == 4and  int(xStr[6]) == 7 and int(xStr[5]) == 4 and int(xStr[4]) == 8 and int(xStr[3]) == 3 and int(xStr[2]) == 6 and int(xStr[1]) == 4 and int(xStr[0]) < 7:
                print("Hooraya")
                error = False



            
        if error:
            return 0

            
        
        rev = xStr[::-1]
        x = int(rev)
        if negative:
            x*=-1
        return x