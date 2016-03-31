"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""

from .simple import Stack

class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initiera det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägg till en nod i trädet."""
        if key <= self.key:
            #vänster delträd
            if self.left is None:
                self.left = BinarySearchTree(key, value)
            else:
                self.left.insert(key, value)
        else:
            #höger delträd
            if self.right is None:
                self.right = BinarySearchTree(key, value)
            else:
                self.right.insert(key, value)


    def lookup(self, key, parent=None):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """
        current = self
        while True:
            if key == current.key:
                return current, parent
            else:
                parent = current
                if key > current.key:
                    if current.right:
                        current = current.right
                    else:
                        return None, None
                else:
                    if current.left:
                        current = current.left
                    else:
                        return None, None


    def delete(self, key):
        """Radera noden med matchande key."""
        current, parent = self.lookup(key)

        number_of_children = 0
        if not current.left is None: 
            number_of_children += 1
        if not current.right is None: 
            number_of_children += 1

        if number_of_children == 0:
            if parent:
                if current == parent.left:
                    parent.left = None
                else:
                    parent.right = None
            else:
                raise Exception('Doh!')

        elif number_of_children == 1:
            if parent:
                if current == parent.left:
                    if current.left:
                        parent.left = current.left
                    else:
                        parent.left = current.right
                else:
                    if current.left:
                        parent.right = current.left
                    else:
                        parent.right = current.right
            else:
                if current.left:
                    current.key = current.left.key
                    current.right = current.left.right
                    current.value = current.left.value
                    current.left = current.left.left

                else:
                    current.key = current.right.key
                    current.value = current.right.value
                    current.left = current.right.left
                    current.right = current.right.right

        elif number_of_children == 2:
            parent = current
            successor = current.right

            while successor.left:
                parent = successor
                successor = successor.left

            current.key = successor.key
            current.value = successor.value

            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right


    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """
        if self.left:
            for node in self.left.traverse():
                yield node

        yield self

        if self.right:
            for node in self.right.traverse():
                yield node


    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        # Använd traverse...
        return ', '.join([str(x.key) for x in self.traverse()])
