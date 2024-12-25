"""
Remember the goal here is to evict the LRU node when capacity is exceeded. Do this by maintaining a Dict for the cache
and sentinel nodes (head and tail). Head points to the oldest node and tail the newest.
Basic implementation rules:
1. Store Actual cache (key val pairs) in a map
2. To maintain LRU store keys in a doubly linked list. The head and tail pointers for this LL point to sentinel nodes
3. Create helper methods to add and remove a Node from doubly linked list (just the basic ops and no capacity checks)
4. Implement get and put methods with capacity checks (for put). Always add to tail and remove from head. For both
get and put you would need to call _remove and _add
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1) #Sentinel or dummy nodes
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self._remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self._add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def _add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

#In doubly linked list you need 2 lines to remove a node, seocnd line is to adjust the prev pointer of the next node
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)