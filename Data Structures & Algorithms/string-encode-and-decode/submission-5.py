class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        temp = ""
        for i in strs:
            for j in i:
                temp = temp + (chr(ord(j) + 1))
            temp = str(len(i)) + "#" + temp
            encoding  = encoding + temp
            temp = ""
        print(encoding)
        return encoding 

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result  = []
        decoding = ""
        length = 0
        i = 0
        while i < len(s):
            if i == 0:
                length = ""
                while s[i] != "#":
                    length = length + s[i]
                    i+=1
                print(length)
                length = int(length)
                i+=1
                continue
            if length == 0:
                length = ""
                while s[i] != "#":
                    length = length + s[i]
                    i+=1
                print(length)
                length = int(length)
                result.append(decoding)
                decoding = ""
                i+=1
            decoding = decoding + (chr(ord(s[i]) - 1))
            length-=1
            i+=1
        result.append(decoding)
        print(result)
        return result





