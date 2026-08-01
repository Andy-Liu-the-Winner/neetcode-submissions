class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            shifted = ""
            for ch in s:
                shifted += chr(ord(ch) + 1)
            res += str(len(shifted)) + "#" + shifted
        return res    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 找到 #，前面是长度
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # 取出编码后的字符串
            encoded = s[j + 1 : j + 1 + length]

            # 把每个字符减 1
            original = ""
            for ch in encoded:
                original += chr(ord(ch) - 1)

            res.append(original)

            # 跳到下一段
            i = j + 1 + length

        return res