from collections import deque

def search(name):

    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if function_with_person(person):
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

def function_with_person(name):
    return name == 'Alex'


if __name__ == '__main__':

    graph = {}
    search(name)

