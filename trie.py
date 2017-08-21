class TrieNode:
    
    def __init__(self):
        self._children = [0]*26
        self.is_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for ch in word:
            if ptr._children[ord(ch)-97] == 0:
                ptr._children[ord(ch)-97] = TrieNode()
            ptr = ptr._children[ord(ch)-97]
        ptr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        res = self._find(word)
        return res != None and res.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._find(prefix) != None
    
    def _find(self, word):
        ptr = self.root
        for ch in word:
            if ptr._children[ord(ch) - 97] == 0:
                return None
            ptr = ptr._children[ord(ch) - 97]
        return ptr


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)