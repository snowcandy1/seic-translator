# -- coding: utf-8 --

class Trie:

    def __init__(self):
        self.root = {}
        self.end = "*EOF*"
        self.wordmean = {}

    def insert(self, word, mean):
        """
        在Trie树中添加词汇
        :type word: str
        :rtype: void
        """
        if not isinstance(mean, str):
            return
        word = word.replace(" ", "_").replace("-", "")
        node = self.root
        for c in word:
            if not c in node:
                node[c] = {}
            node = node[c]
        self.wordmean[word] = mean.replace(" ", "_").replace("-", "")
        if not self.end in node:
            node[self.end] = "?"

    def find(self, word):
        return word in self.wordmean


class TrieFinder:
    def __init__(self, trie: Trie):
        self.trie = trie

    def split(self, text):
        fenci = []
        length = len(text)
        L = 0
        while L < length:
            R = L + 1
            maxR = L + 1
            node = self.trie.root
            if text[L] in node:
                while R <= length:
                    ch = text[R - 1]
                    if ch in node:
                        node = node[ch]
                    else:
                        # print(ch, text[L:R])
                        break
                    if self.trie.end in node:
                        maxR = R
                        # print(L, R, text[L:R])
                    R += 1
            fenci.append(text[L:maxR])
            L = maxR



        # print(fenci)
        res = []
        word = ""
        for i in fenci:
            if i in self.trie.wordmean:
                if word != "":
                    res.append(word)
                res.append(self.trie.wordmean[i])
                word = ""
            else:
                word += i
        if word != "":
            res.append(word)
        return "_".join(res)



if __name__ == "__main__":
    test = Trie()
    test.insert("日期", "date2")
    test.insert("进站日期", "date")
    test.insert("进站", "date3")
    test.insert("时间", "time")
    finder = TrieFinder(test)
    print(finder.split("进站日期日期进站进站日期时间表"))
