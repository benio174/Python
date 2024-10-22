line = "abc\nd\tef\nxy"

biggest = max(len(word) for word in line.split())
smallest = min(len(word) for word in line.split())

print("Najdluzszy wyraz w napisie line:", biggest)
print("Najkrotszy wyraz w napisie line:", smallest)

