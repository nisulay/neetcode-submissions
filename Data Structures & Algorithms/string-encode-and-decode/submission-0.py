class Solution:

    def encode(self, strs: List[str]) -> str:

        single_str = ''

        for s in strs:
            single_str += str(len(s)) + '#' + s
            
        # print(single_str)
        return single_str

    def decode(self, s: str) -> List[str]:

        print(s)

        i = 0
        j = 0
        decoded_list = []

        while i < len(s):
            
            
            while j < len(s):
                j += 1

                if s[j] == '#':
                    length = int(s[i:j])
                    decoded_str = s[j + 1 : j+ 1 + length]  
                    print(decoded_str)
                    decoded_list.append(decoded_str)  
                    i = j + length  + 1
                    j = i 
                    break
    
        return decoded_list


