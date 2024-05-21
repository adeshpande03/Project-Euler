from math import dist, sqrt


def main():
    f = open("./supplements/0102_triangles.txt")
    lines = f.readlines()

    def triangleArea(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    c = 0
    for line in lines:
        line = line.split(",")
        line = list(map(int, line))
        p1, p2, p3 = line[0:2], line[2:4], line[4:6]
        totalArea = triangleArea(p1, p2, p3)
        print(totalArea)
        noP1 = triangleArea([0, 0], p2, p3)
        noP2 = triangleArea(p1, [0, 0], p3)
        noP3 = triangleArea(p1, p2, [0, 0])
        if noP1 + noP2 + noP3 == totalArea:
            print(p1, p2, p3)
            c += 1
    print(c)


main()
