
MAXN = 20
memo = [[-1 for _ in range(MAXN)] for _ in range(MAXN)]

def lcs(x, y, m, n):
    if m < 0 or n < 0:
        return 0
    if memo[m][n] != -1:
        return memo[m][n]
    if x[m] == y[n]:
        memo[m][n] = 1 + lcs(x, y, m-1, n-1)
    else:
        memo[m][n] = max(lcs(x, y, m-1, n), lcs(x, y, m, n-1))
    return memo[m][n]

if __name__ == '__main__':
    word = "micro-ondas"
    m = len(word) - 1
    while(True):
        '''user_input = str(input())
        n = len(user_input) - 1
        if word == user_input:
            print(f"{user_input} Green")
            break
        elif (m - lcs(word, user_input, m, n)) <= 2:
            print(f"{user_input} Yellow")
        else:
            print(f"{user_input} White")
        print(m - lcs(word, user_input, m, n))'''
        user_input = str(input())
        n = len(user_input) - 1
        print(lcs(word,user_input , m, n))