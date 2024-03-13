#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
	// make sure a is always bigger
	if (a < b) { 
		auto t = a;
		a = b;
		b = t;
	}
	long long rem;
	rem = a % b;
	while (rem) {
		// the new bigger number is the original smaller number (b)
		// and the new smaller number is the new remainder
		a = b;
		b = rem;
		rem = a % b;
	}
	// the last smaller number would be the gcm
	return b;
}

long long lcm(long long a, long long b) {
	return (a*b) / gcd(a, b);
}
int main() {
	long long p=1;
	for (int i=2; i <= 20; i++) {
		// find the lcm along the number line
		p = lcm(p, i);
	}
	cout << p << endl;
	return 0;
}
