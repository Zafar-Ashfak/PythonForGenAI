text = "    the power           of your subconscious mind   "
print(text, type(text))

# STRING METHODS
# 1. upper() -> Convert to uppercase
upr = text.upper()
print(upr)

# 2. lower() -> Convert to lowercase
lwr = text.lower()
print(lwr)

# 3. capitalize() -> Capitalize the first letter
cap = text.capitalize()
print(cap)

# 4. title() -> Capitalize each word
cap_each = text.title()
print(cap_each)

# 5. strip() -> remove spaces from both sides
s = text.strip()
print(s)

# 6. lstrip() -> remove spaces from left side
ls = text.lstrip()
print(ls)

# 7. rstrip() -> remove spaces from right side
rs = text.rstrip()
print(rs)

# 8. find() -> Find first occurrence (-1 if absent)
t = text.find("pow")
print(t)

f = text.find("python")
print(f)

# 9. index() -> Find first occurrence (raises error if absent)
print(text.index("o"))

# 10. count() -> Count occurrences (0 if absent)
print(text.count("of"))
print(text.count("md"))

# 11. replace() -> Replace substring
new_str = "I love Java"
rp = new_str.replace("Java", "Python")
print(new_str)
print(rp)
