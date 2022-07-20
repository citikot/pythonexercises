aclNum = int(input("What is the IPv4 ACL number? "))
if 1 <= aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif 100 <= aclNum <= 199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
