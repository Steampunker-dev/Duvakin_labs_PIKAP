import sys
import math
def get_coef(index, prompt):
    try: coef_str = sys.argv[index]
    except:
        print(prompt,sep=" ",end=" ",)
        coef_str = input()
        while True:
            try:
                float(coef_str)
                break
            except: coef_str = float(input())
    coef = coef_str
    return coef
def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
        elif root == 0:
            result.append(0)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        elif root1 == 0:
            result.append(root1)
        if root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
        elif root2 == 0:
            result.append(math.fabs(root2))
    result = sorted(result)
    return result
def main():
    
    a = get_coef(1, ' А:')
    b = get_coef(2, ' B:')
    c = get_coef(3, ' C:')
    roots = get_roots(a, b, c)
    roots = sorted(roots)
    len_roots = len(roots)
    if len_roots == 0: print('Have no roots')
    elif len_roots == 1: print('One root: {}'.format(roots[0]))
    elif len_roots == 2: print('Two roots: {}, {}'.format(roots[0], roots[1]))
    elif len_roots == 3: print('Three roots: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4: print('Four корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2],
    roots[3]))

if __name__ == "__main__":
    main()
