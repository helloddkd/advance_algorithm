import sys
from collections import deque
from itertools import product

sys.stdin = open('12100.txt', 'r')


def up(m):
    global max_block

    result_matrix = [[0] * N for _ in range(N)]
    for j in range(N):
        q = deque()
        for i in range(N):
            element = m[i][j]
            if element != 0:
                q.append(element)

        temp_arr = deque()
        while len(q):
            temp_q = q.popleft()
            if len(temp_arr) != 0 and temp_q == temp_arr[-1]:
                temp_arr.append(temp_arr.pop() + temp_q)
                if len(q):
                    temp_arr.append(q.popleft())
            else:
                temp_arr.append(temp_q)

        for i in range(len(temp_arr)):
            new_element = temp_arr.popleft()
            if new_element > max_block:
                max_block = new_element

            result_matrix[i][j] = new_element

    return result_matrix


def down(m):
    global max_block

    result_matrix = [[0] * N for _ in range(N)]
    for j in range(N):
        q = deque()
        for i in range(N):
            element = m[i][j]
            if element != 0:
                q.append(element)

        temp_arr = deque()
        while len(q):
            temp_q = q.pop()
            if len(temp_arr) != 0 and temp_q == temp_arr[-1]:
                temp_arr.append(temp_arr.pop() + temp_q)
                if len(q):
                    temp_arr.append(q.pop())
            else:
                temp_arr.append(temp_q)

        for i in range(N-1, N-1-len(temp_arr), -1):
            new_element = temp_arr.popleft()
            if new_element > max_block:
                max_block = new_element

            result_matrix[i][j] = new_element

    return result_matrix


def left(m):
    global max_block

    result_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N):
            element = m[i][j]
            if element != 0:
                q.append(element)

        temp_arr = deque()
        while len(q):
            temp_q = q.popleft()
            if len(temp_arr) != 0 and temp_q == temp_arr[-1]:
                temp_arr.append(temp_arr.pop() + temp_q)
                if len(q):
                    temp_arr.append(q.popleft())
            else:
                temp_arr.append(temp_q)

        for j in range(len(temp_arr)):
            new_element = temp_arr.popleft()
            if new_element > max_block:
                max_block = new_element

            result_matrix[i][j] = new_element

    return result_matrix


def right(m):
    global max_block

    result_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N):
            element = m[i][j]
            if element != 0:
                q.append(element)

        temp_arr = deque()
        while len(q):
            temp_q = q.pop()
            if len(temp_arr) != 0 and temp_q == temp_arr[-1]:
                temp_arr.append(temp_arr.pop() + temp_q)
                if len(q):
                    temp_arr.append(q.pop())
            else:
                temp_arr.append(temp_q)

        for j in range(N-1, N-1-len(temp_arr), -1):
            new_element = temp_arr.popleft()
            if new_element > max_block:
                max_block = new_element

            result_matrix[i][j] = new_element

    return result_matrix


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_block = 0
for permutation in product((1, 2, 3, 4), repeat=5):
    a = [matrix[i][:] for i in range(N)]
    for command in permutation:
        if command == 1:
            a = up(a)
        elif command == 2:
            a = down(a)
        elif command == 3:
            a = left(a)
        else:
            a = right(a)

        print(permutation, max_block)

# print(max_block)
