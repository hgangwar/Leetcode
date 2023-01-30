class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    def num_concat(self, word, index):
        if index >= len(word):
            return 1
        node = self.root
        for i in range(index, len(word)):
            if word[i] not in node.children:
                return 0
            if node.children[word[i]].is_end_of_word:
                if i == len(word) - 1:
                    return 1
                next = self.num_concat(word, i + 1)         
                if next > 0:
                    return next + 1
            node = node.children[word[i]]
        return 0
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        Ans=[]
        trie=Trie()
        for x in words: 
            trie.insert(x)
        for i,x in enumerate(words):
            count=trie.num_concat(x,0)
            if(count>1):  Ans.append(x)
        return Ans
if __name__ == "__main__":
    obj=Solution()
    words = ["a","b","ab","abc"]
    Op=obj.findAllConcatenatedWordsInADict(words)
    print(Op)
    """def search(self, curr):
        Root = self.root
        all_Words,ndx=0
        queue=[[Root.children[curr], curr[0]]]
        while(curr[ndx] in Root.children):
            current, curr_word=queue.pop()
            if not current.children: 
                all_Words.append(curr_word)
                continue
            for child in current.children.keys():
                queue.append([current.children[child], curr_word+child])        
        return all_Words"""