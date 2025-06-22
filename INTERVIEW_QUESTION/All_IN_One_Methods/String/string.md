s = "  Hello, World!  "

# 🧼 Modify and Clean
print(s.strip())           # 'Hello, World!'
print(s.lstrip())          # 'Hello, World!  '
print(s.rstrip())          # '  Hello, World!'
print(s.replace("World", "Python"))  # '  Hello, Python!  '

# 🔠 Change Case
print(s.lower())           # '  hello, world!  '
print(s.upper())           # '  HELLO, WORLD!  '
print(s.capitalize())      # '  hello, world!  '
print(s.title())           # '  Hello, World!  '
print(s.swapcase())        # '  hELLO, wORLD!  '
print("Straße".casefold()) # 'strasse'

# 🔍 Find and Search
print(s.find("o"))         # 6
print(s.rfind("o"))        # 9
print(s.index("W"))        # 8
print(s.rindex("l"))       # 10
print(s.count("l"))        # 3
print(s.startswith("  He")) # True
print(s.endswith("!  "))    # True

# ✅ Check Types
print("Hello123".isalnum())     # True
print("Hello".isalpha())        # True
print("123".isdigit())          # True
print("Ⅳ".isnumeric())          # True
print("123".isdecimal())        # True
print("hello".islower())        # True
print("HELLO".isupper())        # True
print("Hello World".istitle())  # True
print("   ".isspace())          # True
print("name_1".isidentifier())  # True
print("hello\n".isprintable())  # False

# 🔗 Join, Split & Partition
print(", ".join(["a", "b", "c"]))       # 'a, b, c'
print("one,two,three".split(","))       # ['one', 'two', 'three']
print("line1\nline2".splitlines())      # ['line1', 'line2']
print("a=b".partition("="))             # ('a', '=', 'b')
print("a=b=c".rpartition("="))          # ('a=b', '=', 'c')
print("key=value=again".split("=", 1))  # ['key', 'value=again']

# 📐 Align and Pad
print("42".zfill(5))       # '00042'
print("hi".center(6))      # '  hi  '
print("hi".ljust(6))       # 'hi    '
print("hi".rjust(6))       # '    hi'

# 🧠 Format Strings
print("Hello, {}".format("Alice"))                    # 'Hello, Alice'
print("Name: {name}".format_map({'name': 'Bob'}))     # 'Name: Bob'

# 🧹 Prefix/Suffix Removal (Python 3.9+)
print("unhappy".removeprefix("un"))         # 'happy'
print("filename.txt".removesuffix(".txt"))  # 'filename'
