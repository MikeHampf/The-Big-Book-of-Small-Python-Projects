r"""Diamonds, by A. Sweigart
Draws diamonds of various sizes.
View this code at https://nostarch.com/big-book-small-python-projects
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
  """

def main():
    print('Diamonds, by A. Sweigart')
    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlineDiamond(size):
    for i in range(size):
        print(' '*(size-i-1), end='')
        print('/', end='')
        print(' '*(i*2), end='')
        print('\\')
    for i in range(size):
        print(' '*i, end='')
        print('\\', end='')
        print(' '*((size-i-1)*2), end='')
        print('/')
        
def displayFilledDiamond(size):
    pass

if __name__=='__main__':
    main()