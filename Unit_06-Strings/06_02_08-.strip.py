love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []

for i in love_maybe_lines:
    love_maybe_lines_stripped.append(i.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# strip can be used more than once in the same string
# hello = !!!world !!!
# hello_fixed = hello.strip('!').strip()
# print(hello_fixed)