def non_repeating_characters(str1):
    char_order=[]
    counts={}
    for c in str1:
        if c in counts:
            counts[c]+=1
        else:
            counts[c]=1
            char_order.append(c)
    for c in char_order:
        if counts[c]==1:
            return c
        
print(non_repeating_characters("djebdebdedbekfrnkfnduwbdwkd"))
        