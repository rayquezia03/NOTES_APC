def check_permutation(word_one,word_two):
    permut = True
    letters1 = []
    letters2 = []
    
    for letter in word_one:
        letters1.append(letter)
    
    for letter in word_two:
        letters2.append(letter)
       
    if len(letters1) != len(letters2):
        permut = False
        
    for elem in letters1: 
        if elem not in letters2:
            print(elem)
            permut = False
     
            
    return print(permut)
  
check_permutation('amor','romal')   