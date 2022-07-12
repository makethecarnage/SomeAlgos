from collections import deque

def bfs (name):

    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    searched.add(name)
    level = 0

    while search_queue:

        level += 1
        person = search_queue.popleft()

        for neighbour in graph[person]:
            if neighbour not in searched:
                if function_with_person(neighbour):
                    return level
                searched.add(neighbour)
                search_queue.append(neighbour)

    return False


def function_with_person(name):
    return name == 'Alex'


if __name__ == '__main__':

    graph = {}
    name = input()
    if function_with_person(name):
        print(0)
    else:
        search(name)
