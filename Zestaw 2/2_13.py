line = "ab\nc\tef\nxy"

length = sum(len(word) for word in line.split())

print("Laczna dlugosc w napisie line", length)