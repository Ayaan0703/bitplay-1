input("First set bit -  the rightmost 1 in the binary number. press Enter")
print("5 -> binary:", bin(5)[2:],"first one at position 0")
print("8 -> binary:", bin(8)[2:],"first one at position 3")

n = int(input("Enter a number(try 8 or 14):"))
input("Watch bits drop until the first 1 appears. press Enter")
temp = n
pos = 0 
while temp>0:
    print("binary", bin(temp)[2:],"Last bit:", temp & 1)
    if temp & 1:
        break
    pos += 1
    temp >>=1
print("First set bit in",n,"is at position", pos)