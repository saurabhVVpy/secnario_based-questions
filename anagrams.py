def ch_count(user_input):
    count={}
    for ch in user_input:
        if ch in count:
            count[ch]=count[ch]+1
        else:
            count[ch]=1
    return count

def main():
    str_1=input('ENTER: ')
    str_2=input('ENTER: ')
    dict1=ch_count(str_1)
    dict2=ch_count(str_2)
    if dict1==dict2:
        print("it's anagrams")
    else:
        print("it's not anagrams")
main()