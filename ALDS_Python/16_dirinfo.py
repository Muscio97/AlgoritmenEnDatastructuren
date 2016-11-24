import os

def treewalk(root, nspaces=0):
    # nspaces : aantal spaties dat ingesprongen wordt
    a = os.listdir(root)
    for f in a:
        print(' '*nspaces,end = '')
        if os.path.isdir(root + '/' + f):
            print('[' + f + ']')
            treewalk(root + '/' + f,nspaces+3) # recursieve aanroep
        else:
            print(f)
                
root = os.getcwd()
treewalk(root + '/../..')