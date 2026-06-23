class Solution:
    def encode(self, strs: List[str]) -> str:
        e_string=""
        for s in strs:
            e_string+= str(len(s)) + "#" + s
        return e_string

    def decode(self, s: str) -> List[str]:
        d_strs=[]

        i=0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            w_start= j+1
            w_end= w_start+length
            d_strs.append(s[w_start:w_end])
            i=w_end

        return d_strs