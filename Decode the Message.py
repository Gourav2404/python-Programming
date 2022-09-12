class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        temp = dict.fromkeys(key)
        val = 97
        for keys in temp.keys():
            temp[keys] = chr(val)
            val+=1
        temp[" "] = " "
        string=''
        for ch in message:
            string+=temp[ch]
        return string