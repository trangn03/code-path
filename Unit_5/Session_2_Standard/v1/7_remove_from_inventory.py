class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_item(head, item):
    # 1. The list is empty
    if head is None: 
        return head
    
    # 2. The node is delete is the head node
    if head.value == item:
        return head.next
    
    # 3. The node to delete is somewhere in the middle or at the end
    current = head
    while current.next and current.next.value != item:
        current = current.next
    
    # If found the item then remove the node
    if current.next:
        current.next = current.next.next 
        
    return head


slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))