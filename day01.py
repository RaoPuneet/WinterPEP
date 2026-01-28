from collections import Counter

s = input().strip()

freq = Counter(s)

sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for ch, count in sorted_chars[:3]:
    print(ch, count)
