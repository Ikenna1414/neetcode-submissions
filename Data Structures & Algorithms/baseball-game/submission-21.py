class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        sum1 = 0
        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                output.append(int(operations[i]))
            elif operations[i]=="+":
                output.append(int(output[-1]+output[-2]))
            elif operations[i]=="D":
                output.append(2*int(output[-1]))
            elif operations[i] == "C":
                output.pop()
        for x in output:
            sum1 = sum1 + x
        return sum1
