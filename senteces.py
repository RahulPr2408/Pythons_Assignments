def findDiffChar(str):
    num = 0
    ch = 0
    spch = 0
    ws = 0
    for c in str:
        if c >= '0' and c <= '9':
            num += 1
        elif c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            ch += 1
        elif c == ' ':
            ws += 1
        else:
            spch += 1

    print("Total number in String: ", num)
    print("Total characters in String: ", ch)
    print("Total white Space in String: ", ws)
    print("Total special chars in String: ", spch)


def findPercentage(lst):
    cnt = 0
    for char in lst:
        if char.isalnum():
            cnt += 1
    per = cnt / len(lst)
    per = per * 100
    print("Percentage of Alphanumerics: ", per)


str = input("Enter your string: ")

lst = str.split(" ")
print("No of words in string: ", len(lst))
findDiffChar(str)
findPercentage(lst)


