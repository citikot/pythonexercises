a_str = 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C'
b_str = 'RJUAKY9QKJVJIDWFZQPJ8293EEEO9SB8ZH832HTOP'
res = 0  

a_len = len(a_str)
b_len = len(b_str)

min_len = a_len if a_len - b_len < 0 else b_len

i = 0

while (i < (min_len)):
    res += abs(ord(a_str[i]) - ord(b_str[i]))
    i += 1

if b_len > a_len:
    i_str = b_str[i:]
else:
    i_str = a_str[i:]

for ch in i_str:
    res += ord(ch)

print(res)
