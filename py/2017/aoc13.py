class Scanner():
    def __init__(self, depth, range):
        self.position = 0
        self.delta = 1
        self.depth = depth
        self.range = range
    
    def __repr__(self):
        return 'depth: {0}, range: {1}'.format(self.depth, self.range)

    def update_position(self):
        if self.range > 0:
            self.position += self.delta
            if self.position == self.range - 1:
                self.delta = -1
            if self.position == 0:
                self.delta = 1
    
    def caught_position(self):
        return self.position == 0
    
    def severity(self):
        return self.depth * self.range if self.caught_position() else 0

def process_input(filename):
    scanners_dict = {}
    max_layer = 0
    with open(filename) as f:
        for l in f:
            (d, r) = l.replace(' ', '').split(':')
            scanners_dict[int(d)] = Scanner(int(d), int(r))
            if int(d) > max_layer : max_layer = int(d)
    return (scanners_dict, max_layer)

def severity(scanners_dict, max_layer):
    total_severity = 0
    for layer in range(0, max_layer + 1):
        if scanners_dict.get(layer, None) != None:
            scanner = scanners_dict[layer]
            total_severity += scanner.severity()
        update_positions(scanners_dict)
    return total_severity

def update_positions(scanners_dict):
    for scanner in scanners_dict.values():
        scanner.update_position()

def can_pass(scanners_dict, delay):
    for scanner in scanners_dict.values():
        if not ((scanner.depth + delay) % (2 * scanner.range - 2)):
            return False
    return True

def min_pass_delay(scanners_dict):
    delay = 0
    while not can_pass(scanners_dict, delay):
        delay += 1
    return delay

if __name__ == '__main__':
    scanners, max_layer = process_input('input13.txt')
    result1 = severity(scanners, max_layer)
    print('Result part 1: {0}'.format(result1))
    result2 = min_pass_delay(scanners)
    print('Result part 2: {0}'.format(result2))