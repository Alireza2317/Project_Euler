#include <iostream>
using namespace std;

int main() {
	unsigned long long sum_of_squares=0;
	unsigned long long squares_of_sum=0;
	for (unsigned long long i=1; i<=100; i++) {
		sum_of_squares += (i*i);
		squares_of_sum += i;
	}
	squares_of_sum *= squares_of_sum;
	cout << squares_of_sum - sum_of_squares << endl;
	return 0;
}
