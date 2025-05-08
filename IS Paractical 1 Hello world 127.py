str_ = "HelloWorld"

print("AND with 127:")
for c in str_:
    print(f"{c} -> {ord(c)} & 127 = {ord(c) & 127}")

print("\nXOR with 127:")
for c in str_:
    print(f"{c} -> {ord(c)} ^ 127 = {ord(c) ^ 127}")
