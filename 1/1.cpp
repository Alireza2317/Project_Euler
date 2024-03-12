#include <iostream>
using namespace std;

bool is_divisable_5or3(const int n) {
	if (n%3 == 0 or n%5 == 0) return true;
	return false;
}       


int main() {
	int n = 1000;
	int sum = 0;

	for (int i=1; i<n; i++) {
		if (is_divisable_5or3(i)) {
			sum += i;
		}
	}
	cout << sum << endl;
	return 0;
}


