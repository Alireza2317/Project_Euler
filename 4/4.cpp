#include <iostream>
using namespace std;


bool is_palindrome(int n) {
	int nd=n;
	int n_rev=0;
	
	while (nd) {
		n_rev *= 10; 
		n_rev += nd%10;
		nd /= 10;
	}
	if (n == n_rev) 
		return true;
	return false;	
}

int main() {
	const int N = 9;
	const int M = 1;
	
	int j;
	for (int total=2*N; total >= 2*M; total--) {
		for (int i=std::max(M, total - N); i <= std::min(N, total - M); i++) {
			j = total - i;
			cout << i << " " << j << endl;
			if (is_palindrome(i*j)) {
				//cout << i*j << endl;
				//return 0;
			}
		}
	}
	return 0;
}