from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        key_set = set()
        key_q = deque()

        for key in rooms[0]:
            key_q.append(key)

        while key_q:
            top = key_q.popleft()
            if top not in key_set and top != 0:
                key_set.add(top)
                key_q.append(top)
                for key in rooms[top]:
                    key_q.append(key)

        return True if len(key_set) == len(rooms)-1 else False
