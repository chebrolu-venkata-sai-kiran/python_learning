import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "The quick brown fox jumps over the lazy dog."

encoded_text = enc.encode(text)

print(encoded_text)

decoded = enc.decode([976, 4853, 19705, 68347, 65613, 1072, 290, 29082, 6446, 13])

print(decoded)