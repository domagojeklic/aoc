class Node:
    def __init__(self, score, parent):
        self.score = score
        self.parent = parent
        self.children = []
    def addchild(self, child):
        self.children.append(child)

def totalScore(node):
    if len(node.children) == 0:
        return node.score

    score = node.score
    for child in node.children:
        score += totalScore(child)
    
    return score

def process_input(filname):
    with open(filname) as file:
        current_node = None
        is_garbage = False
        should_escape = False
        garbage_count = 0
        content = file.read()
        for c in content:
            if is_garbage:
                if should_escape:
                    should_escape = False
                    continue
                elif c == '!':
                    should_escape = True
                elif c == '>':
                    is_garbage = False
                else:
                    garbage_count += 1
            else:
                if c == '<':
                    is_garbage = True
                elif c == '{':
                    current_score = current_node.score if current_node else 0
                    node = Node(current_score + 1, current_node)
                    if current_node:
                        current_node.addchild(node)
                    current_node = node
                elif c == '}':
                    if not current_node.parent:
                        return (current_node, garbage_count)
                    else:
                        current_node = current_node.parent

if __name__ == '__main__':
    (root_node, count) = process_input('input09.txt')
    total_score = totalScore(root_node)
    print("Total score: {0}".format(total_score))
    print("Garbage count: {0}".format(count))