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
        content = file.read()
        for c in content:
            print(c)
            if c == '{':
                current_score = current_node.score if current_node else 0
                node = Node(current_score + 1, current_node)
                if current_node:
                    current_node.addchild(node)
                current_node = node
            elif c == '}':
                if not current_node.parent:
                    return current_node
                else:
                    current_node = current_node.parent

if __name__ == '__main__':
    root_node = process_input('input09.txt')
    total_score = totalScore(root_node)
    print(total_score)