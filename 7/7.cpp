#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(long long n) {
	if (n == 2) return true;
	for (int i=2; i <= ceil(sqrt(n)); i++)
		if (n%i == 0) return false;
	return true;	
}

long long primes(int n) {
	if (n == 1) return 2;
	
	int count=1, i=3;
	while (true) {
		if (is_prime(i)) count++;
		if (count == n) return i;

		i += 2;
	}
}

int main() {
	int n = 10001;
	cout << primes(n) << endl; 
	return 0;
}
