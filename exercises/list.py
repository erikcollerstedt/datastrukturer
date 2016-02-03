"""Övningar på ADTn unordered list."""

from .exceptions import EmptyList

class Node():
    """Implementation av nod för `UnorderedList`."""

    def __init__(self, data, next):
        """Initiera noden med attributen `self.data` och `self.next`."""
        self.data = data
        self.next = next


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):
        """Initiera den tomma listan."""
        self.head = None

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`."""
        return self.head is None

    def add(self, item):
        """Lägg till `item` i början av listan."""
        self.head = Node(item, self.head)

    def size(self):
        """Returnerar antalet värden i listan."""
        count = 0
        current = self.head

        while current:
            current = current.next
            count += 1

        return count

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`."""
        current = self.head

        while current:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Raderar första förekomsten av `item` från listan."""
        if self.head == None:
            raise EmptyList

        if self.head.data == item:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next and current.next.data == item:
                current.next = current.next.next

                return True
            current = current.next

        return False

    def append(self, item):
        """Lägg till `item` i slutet av listan."""
        if self.head is None:
            self.head = Node(item, self.head)

        current = self.head
        while current:
            if current.next is None:
                current.next = Node(item, None)
                break
            current  = current.next

    def insert(self, position, item):
        """Lägg till `item` på index `position`."""
        pass

    def index(self, item):
        """Returnerar index i listan för första förekomsten av `item`."""
        pass

    def pop(self, postition=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """
        pass
