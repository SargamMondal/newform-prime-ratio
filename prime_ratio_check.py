from sage.all import Integer, divisors, is_prime

filename = "lmfdb_mf_newforms.txt"


def number_of_primes(degree):
    M = 4 * degree
    return sum(1 for d in divisors(M) if is_prime(d + 1))


threshold = 0.025751

print(f"{'Status':<9} | {'Level':<6} | {'Deg':<5} | {'M':<5} | {'Primes':<6} | {'Ratio':<8}")
print("-" * 60)

with open(filename) as F:
    for line in F:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        cols = line.split("\t")

        # Columns:
        # 0 Label
        # 1 Level
        # 2 Weight
        # 3 Relative Dimension
        # 4 Hecke field label

        label = cols[0].strip('"')
        level = Integer(cols[1])
        degree = Integer(cols[3])

        M = 4 * degree
        num_primes = number_of_primes(degree)
        ratio = float(num_primes / level)

        status = "[FLAGGED]" if ratio > threshold else "[OK]"

        print(
            f"{status:<9} | "
            f"{level:<6} | "
            f"{degree:<5} | "
            f"{M:<5} | "
            f"{num_primes:<6} | "
            f"{ratio:.6f}"
        )
