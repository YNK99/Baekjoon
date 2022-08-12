def solution(new_id):
    one = new_id.lower()
    
    two = ''
    
    ok = [c for c in range(48, 58)] + [ord('-'), ord('_'), ord('.')]
    ok = ok + [c for c in range(97, 123)]
    
    for o in one:
        if ord(o) in ok:
            two += o
        else:
            continue
    three = ''
    
    for t in range(len(two) + 1, 1, -1):
        two = two.replace('.' * t, ".")
    
    three = two
    
    four = three
    
    if len(three) != 0 and three[0] == ".":
        four = three[1:]
    
    if len(four) != 0 and four[-1] == "." :
        four = four[0:len(four) - 1]
        
    five = four
    
    if len(five) == 0:
        five += "a"
    six = five
    
    if len(six) >= 16:
        six = six[:15]
    
    if six[-1] == ".":
        six = six[:len(six) - 1]
        
    seven = six
    
    last = seven[-1]
    
    if len(seven) <= 2:
        while len(seven) != 3:
            seven += last
              
    answer = seven
    return answer