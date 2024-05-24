def chek_repitation(seq):
    if len(seq) == len(set(seq)):
        print("No Repeatation!")
    else:
        print("Repeatation!")
    return

chek_repitation([1,2,3,4,5,8,8,8])