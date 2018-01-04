import re
from collections import namedtuple

Vector3 = namedtuple('Vector3', 'x y z')
Particle = namedtuple('Particle', 'p v a')

def load_input(filename):
    paricles_list = []
    with open(filename) as f:
        r = re.compile('p=<(.+?)>.+?v=<(.+?)>.+?a=<(.+?)>')
        for l in f:
            (pstr, vstr, astr) = r.search(l).groups()
            (px, py, pz) = pstr.split(',')
            (vx, vy, vz) = vstr.split(',')
            (ax, ay, az) = astr.split(',')
            p = Vector3(int(px), int(py), int(pz))
            v = Vector3(int(vx), int(vy), int(vz))
            a = Vector3(int(ax), int(ay), int(az))
            particle = Particle(p, v, a)
            paricles_list.append(particle)
    return paricles_list

def distance(vec):
    return abs(vec.x) + abs(vec.y) + abs(vec.z)

def min_acceleration_particle(particles):
    return min(particles, key=lambda p: distance(p.a))

if __name__ == '__main__':
    particles_list = load_input('input20.txt')
    p = min_acceleration_particle(particles_list)
    print('Result part 1: {0}'.format(particles_list.index(p)))