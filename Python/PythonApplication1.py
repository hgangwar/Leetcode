
import textwrap

def wrap(string, max_width):
    l=len(string)
    nl=int(l/max_width);
    if l>=max_width:
        P=string[0:max_width]
    else:
        P=string
    for i in range(2,nl+1):
        P=P+"\n"+string[max_width*(i-1):max_width*i]
    if nl*max_width!=l:
        P=P+"\n"+string[max_width*nl:l]
    return P

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)