#include <iostream>
using namespace std;

unsigned long long fibonacci(int n) {
	if (n <= 2) return n;

	unsigned long long f1=1, f2=2, f;
	for (int i=3; i <= n; i++) {
		f = f1 + f2;
		f1 = f2;
		f2 = f;
	}	
	return f;
}

bool is_even(int n) {
	if (n%2 == 0)	return true;
	return false;
}

int main() {
	unsigned long long sum=0;
	for (int i=0; fibonacci(i) <= 4000000; i++) {
		if (is_even(fibonacci(i)))
			sum += fibonacci(i);
	}
	
	cout << sum << endl;
	return 0;
}
