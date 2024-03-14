#include <math.h>
#include <iostream>
using namespace std;

bool is_prime(long long n) {
	if (n == 2) return true;
	for (long long i=2; i <= ceil(sqrt(n)); i++) {
		if (n%i == 0)	return false;
	}
	return true;
}

int main() {
	long long sum=2;
	for (long long i=3; i < 2000000; i += 2) {
		if (is_prime(i)) sum += i;
	}
	cout << sum << endl;
	return 0;
}
