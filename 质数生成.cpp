#include <math.h>
#include <iostream>

typedef unsigned long long uint64_t;

using namespace std;
int main() {
	uint64_t n;
	cin >> n;
	while (n++) {
		uint64_t Sqrt = sqrt(n);
		for (uint64_t i = 2; i <= sqrt(n); ++i) {
			if (n % i == 0) {
				goto LOOP;
			}
		}
		cout << n;
		return 0;
	LOOP:
		;
	}
}