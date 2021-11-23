

def isPalindrome(a):
    ll = len(a) - 1
    isPalindrome = True
    for idx, aa in enumerate(a):  # Loop over a list while keeping track of indexes with enumerate
        #print(aa, idx)
        if ( aa != a[ll-idx]):
            isPalindrome = False
            break;

    print(a, isPalindrome)
    return isPalindrome


if __name__ == "__main__":
    isPalindrome("aba")
    isPalindrome("abbbbbbbbbbbbbba")
    isPalindrome("abaaba")
    isPalindrome("abas")
