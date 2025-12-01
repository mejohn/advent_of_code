from itertools import combinations
from dataclasses import dataclass

def intersection(line1, line2):
    # Cramer's rule
    D  = line1[0] * line2[1] - line1[1] * line2[0]
    Dx = line1[2] * line2[1] - line1[1] * line2[2]
    Dy = line1[0] * line2[2] - line1[2] * line2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

@dataclass
class Hail:
    position: tuple[int, int, int]
    velocity: tuple[int, int, int]

    # # linear system https://stackoverflow.com/a/20679579
    # @cached_property
    # def line(self):
    #     next_position = (self.position[0]+self.velocity[0], self.position[1] + self.velocity[1])
    #     A = -1 * self.velocity[1]
    #     B = self.velocity[0]
    #     C = (self.position[0]*next_position[1] - next_position[0]*self.position[1])
    #     return A, B, -C  # A*x + B*y - C = 0

    @property
    def slope(self):
        return self.velocity[1] / self.velocity[0]
    
    def point_in_future(self, x, y):
        if self.velocity[0] > 0 and self.position[0] > x: 
            return False
        if self.velocity[1] > 0 and self.position[1] > y:
            return False
        if self.velocity[0] < 0 and self.position[0] < x:
            return False
        if self.velocity[1] < 0 and self.position[1] < y:
            return False
        return True


hail = {}
with open("input.txt") as f:
    for id,line in enumerate(f):
        pos,vel = line.strip().split(" @ ")
        pos = eval(pos)
        vel = eval(vel)
        hail[id] = Hail(pos,vel)

print(hail)
# test area 7 to 27 inclusive
# input area 200000000000000 to 400000000000000 inclusive
        
area_min = 200000000000000
area_max = 400000000000001

explosions = []
for hail1, hail2 in combinations(hail.keys(), r=2):
    h1 = hail[hail1]
    h2 = hail[hail2]
    print(h1, h2)
    if h1.slope == h2.slope:
        continue
    x_intersect = ((h2.slope*h2.position[0]) - (h1.slope*h1.position[0]) + (h1.position[1] - h2.position[1])) / (h2.slope - h1.slope)
    if x_intersect >= area_min and x_intersect <= area_max:
        y_intersect = (h1.slope * (x_intersect - h1.position[0])) + h1.position[1]
        if y_intersect >= area_min and y_intersect <= area_max:
            if h1.point_in_future(x_intersect, y_intersect) and h2.point_in_future(x_intersect, y_intersect):
                print(hail1, hail2)
                explosions.append((hail1, hail2))

print(explosions)
print(len(explosions))
