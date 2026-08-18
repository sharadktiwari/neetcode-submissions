class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s_list = []
        for s in strs:
            s_list.append(f"{str(len(s))}#{s}")

        return "".join(s_list)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            out.append(s[i:j])
            
            i = j
        return out

            

        

