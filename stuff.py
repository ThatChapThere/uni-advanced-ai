# note: it seems to like truncation rather than rounding

for number in numbers:
    four_dp(number / sum(numbers))

four_dp(sum(numbers[:-1]) / sum(numbers))

print('passing prob:')
four_dp((20+11) / (20+11+2+1))

print('female passing prob:')
four_dp(11 / (20+11+2+1))

print('sunny 0.4')

print('rainy if cold')
four_dp(5/6)

print('sun if winter')
dp(3, (0.1+0.15) / (0.1+0.05+0.15+0.2))

print('no measles if rash')
dp(3, 8/9)

print('measles if rash')
dp(3, 1/9)

print('probability of KJ given hamburger')
"""
bayes rule :

         P(B|A) * P(A)
P(A|B) = -------------
             P(B)

here A = KJ
     B = hamburger
"""
print((0.9 * (1/100000)) / 0.5)

print('P(d|t):')
t_d = 0.99
d = 1/10000
t = t_d * d + (1-0.95) * (1-d)
d_t = t_d * d / t
print(d_t)
