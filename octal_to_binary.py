class CodesCracker:
    def OctToBin(self, o):
        return bin(int(o, 8))
onum = input()
obj = CodesCracker()
bnum = obj.OctToBin(onum)
print(bnum[2:])