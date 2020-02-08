import math 

cached = {}
dcached = {}
L = {}
mod = 10**9

def mobius(N):
    global L
    L = [1]*(N+1)
    i = 2
    while i <= N:
        # if i is not sq. free, then no multiple is
        if L[i] == 1 or L[i] == -1:
            L[i] = -L[i]
            sq = i * i
            j = i + i
            while j <= N:
                # we use 2 to mark non-primes
                if abs(L[j]) == 2:
                    L[j] = -L[j]
                else:
                    L[j] = -L[j]*2
                j += i
            j = sq
            while j <= N:
                L[j] = 0
                j += sq
        i += 1
    i = 2
    while i <= (N):
        if abs(L[i]) == 2:
            L[i] = L[i] // 2
        i += 1
    return L

def square_root_time_sum_of_sum_of_divisors(N):
    global dcached
    if N in dcached: return dcached[N]
    div_sum, i = 0, 1
    q = int(math.sqrt(N))
    while i <= q:
        div_sum += (i * (N // i))
        i += 1
    i = 1
    while i <= N // (q + 1):
        m = N // i
        k = N // (i + 1)
        div_sum += (i * (m * (m + 1) - k * (k + 1)) // 2)
        i += 1
    dcached[N] = div_sum
    return div_sum

def S(N):
    global cached
    if N in cached: return cached[N]
    dv = square_root_time_sum_of_sum_of_divisors(N)
    S_sum, i = 0, 2
    while i <= N:
        S_sum += (i * S(N // i)) % mod
        i += 1
    cached[N] = (dv * dv - S_sum) % mod
    return cached[N]


def SV2(N): 
    total = 0
    i, j = 1,1
    mobius(N)
    while i <= N:
        div = square_root_time_sum_of_sum_of_divisors(N//i) % mod 
        total = (((div**2)*L[i]*i) % mod + total) % mod 
        i += 1
    return total

if __name__ == "__main__":
  #  print(SV2(10**11))
    print(S(10**9))


