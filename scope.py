
# example of scoping issue. Bad practice!
# please tweak the script to learn about scoping
def f():
    global s
    print(s)
    s = 'ATCCGAATC'
    print(s)

s = 'ATCG'
f()
print(s)
