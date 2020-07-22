import heapq


class Node(object):
    def __init__(self, left_index, right_index, init=False):
        self.left_index = left_index
        self.right_index = right_index
        if(init):
            self.dist = right_index - left_index
        else:
            self.dist = (right_index - left_index) // 2

    def __repr__(self):
        return f'Node value: {self.left_index, self.right_index}'

    def __lt__(self, other):
        #  同じ左優先
        if(self.dist == other.dist):
            return self.left_index < other.left_index
        # max heap
        return self.dist > other.dist


def solve(n, a_1):
    # 初期値は2つ
    even_a_sum = 0
    heapq_list = [Node(0, a_1 - 2, init=True), Node(a_1, n - 1, init=True)]
    heapq.heapify(heapq_list)

    # それぞれ端に座ったか
    most_left_empty, most_right_empty = True, True
    if(a_1 == 1):
        most_left_empty = False
    elif(a_1 == n):
        most_right_empty = False

    a_count = 1
    while(len(heapq_list) > 0):
        p_node = heapq.heappop(heapq_list)

        if(p_node.right_index - p_node.left_index < 0):
            continue

        # 一番左まだ座ってなかったら
        if(p_node.left_index == 0 and most_left_empty):
            most_left_empty = False
            sat_index = 0

        # 一番右まだ座ってなかったら
        elif(p_node.right_index == n - 1 and most_right_empty):
            most_right_empty = False
            sat_index = n - 1

        else:
            sat_index = p_node.left_index + p_node.dist

        # 左の区間まだ誰も座っていない区間の大きさ
        heapq.heappush(heapq_list, Node(p_node.left_index, sat_index - 1))
        # 右の区間まだ誰も座っていない区間の大きさ
        heapq.heappush(heapq_list, Node(sat_index + 1, p_node.right_index))

        a_count += 1
        if(a_count % 2 == 0):
            even_a_sum += sat_index + 1

    return even_a_sum


if __name__ == "__main__":
    # in, outのテキスト同時に開く
    with open('q3_in.txt') as f_in, open('q3_out.txt', mode='w') as f_out:
        for line in f_in:
            n, a_1 = list(map(lambda v: int(v), line.rstrip('\n').split(' ')))
            print('processing', n, a_1)
            solv = solve(n, a_1)
            f_out.write('{}\n'.format(solv))
