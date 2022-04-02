class Solution:
    def interpret(self, command: str) -> str:
       command =  command.replace("()", "o")
       command = command.replace("(al)", "al")

       return command


obj = Solution()
print(obj.interpret("G()(al)"))
