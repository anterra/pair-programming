# Imports?

def j(arg1, arg2):
    if sorted(arg1) == sorted(arg2):
        return 1.0
#     elif len(set(arg1).intersection(arg2))/len(arg2) == 0.5:
#         return float(0.5)
    elif len(arg2) == 2*len(arg1):
        return 0.5
#     elif arg1 != arg2:
#         return 0
    else:
        return 0

    