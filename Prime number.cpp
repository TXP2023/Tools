#include <math.h>
#include <iostream>

typedef unsigned long long uint64_t;

using namespace std;
int main() {
	//对于输入的n， 输出大等于n的最小素数
	uint64_t n;
	cin >> n;
	--n;
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