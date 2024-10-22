line = "ab\nc\tef\nxy"

count = 0

for _ in line.split():
    count += 1

print("Liczba wyrazow w napisie:", count)

