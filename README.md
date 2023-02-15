# RSA_CRYPTO_SYSTEM
RSA  encryption algorithm
	1. Choose 2 prime numbers p and q (p != q), independently random
	2. Calculate n = p*q
	3. Calculate the value of the Euler function: Phi(n) = (p -1)*(q - 1)
	4. Choose a number e such that 1 < e < Phi(n) and gcd(e, Phi(n)) = 1
	5. Calculate d such that d*e == 1 mod Phi(n) (or d = e^-1, d invermultiply e)
	6. Encoding: c = m^e mod n
	7. Decode: m = c^d mod n