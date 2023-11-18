A, B, C = map(int, input().split())

# 문제에서 요구하는대로 작성
print((A + B) % C)
print(((A + C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

