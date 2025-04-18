#include <math.h>
#include <iostream>
#include <Windows.h>
#include <cstdint>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <stdint.h>
#include <deque>
#include "lib\rand.h"

#define endl "\n"

using namespace std;
int main() {
	//对于输入的n， 输出大等于n的最小素数
	uint64_t n;
	cin >> n;
	--n;
	while (n++) {
		for (uint64_t i = 2; i <= sqrt(n); ++i) {
			if (n % i == 0) {
				goto LOOP;
			}
		}
		cout << n << endl;
		system("pause");
		return 0;
	LOOP:
		;
	}

	system("pause");
	return 0;
}