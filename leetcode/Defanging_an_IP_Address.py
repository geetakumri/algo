class Solution(object):
    def defangIPaddr(self, address:str)->str:
        """
        :type address: str
        :rtype: str"""

       #return address.replace('.','[.]')
        #return '[.]'.join(address.split('.'))"""

        output = ""
        for c in address:
            if c == '.':
                output += '[.]'
            else:
                output += c
        return output

