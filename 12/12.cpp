#include <iostream>
#include <cmath>
using namespace std;

unsigned long long tri_num(const int &n) {
	unsigned long long sum=0;
	for (int i=1; i <= n; i++) {
		sum += i;
	}
	return sum;
}

int count_divisors(const unsigned long long &n) {
	int count=2;
	for (auto i=2ull; i <= sqrt(n); i++) {
		if (i*i == n) count++;
		else if (n%i == 0) count+=2;
	}
	return count;
}

int main() {
	for (auto i=1ull; true; i++) {
		if(count_divisors(tri_num(i)) > 500) {
			cout << tri_num(i) << endl;
			return 0;	
		}
	}
	return 0;
}
