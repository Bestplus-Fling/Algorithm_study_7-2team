import sys
n = int(sys.stdin.readline().rstrip())
wordlist = [sys.stdin.readline().rstrip() for _ in range(n) ]
wordlist = list(set(wordlist))

wordlist.sort()
wordlist.sort(key=len)

for i in range(len(wordlist)):
    print(wordlist[i])