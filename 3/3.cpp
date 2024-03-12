#include <iostream>
#include <cmath>
using namespace std;


bool is_prime(long long n) {
	for (long long i=2; i <= ceil(sqrt(n)); i++) {
		if (n%i == 0) return false;
	}
	return true;
}


long long biggest_prime_factor(long long n) {
	for (long long i=ceil(sqrt(n)); i >= 2; i--) {
		if (n%i == 0 and is_prime(i))
			return i;
	} 
	return n;
}


int main() {
	unsigned long long n = 600851475143;
	cout << biggest_prime_factor(n) << endl;
	return 0;
}
