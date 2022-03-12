def count_substring(s, ss):
    x=len(ss)
    y=0
    for i in range(0,len(s)):
        if s[i:i+x]==ss[::]:
            y+=1
    return y

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
