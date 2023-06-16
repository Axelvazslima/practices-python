def serie_two(n):
    if n < -5.8:
        print(f"{n:.1f}")
        return n
    elif n >= -5.8:
        print(f"{n:.1f}")
        return serie_two(n - 1.5)

serie_two(15.2)
