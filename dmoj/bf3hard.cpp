#include <bits/stdc++.h>
typedef unsigned long long ull;
using namespace std;
ull mult(ull a, ull n, ull p) {
	ull curr = a;
	ull res = 0;
	while (n != 0) {
		if (n & 1 == 1) {
			res = (res + curr) % p;
		}
		curr = (curr + curr) % p;
		n = n >> 1;
	}
	return res;
}
ull exp(ull a, ull n, ull p) {
	ull curr = a;
	ull res = 1;
	while (n != 0) {
		if (n & 1 == 1) {
			res = mult(res, curr, p);
		}
		curr = mult(curr, curr, p);
		n = n >> 1;
	}
	return res;
}
bool fermat(ull p) {
	ull a;
	for (ull i = 0; i < 1; i++) {
		a = rand() % (p - 1) + 1;
		if (exp(a, p - 1, p) != 1) {
			return false;
		}
	}
	return true;
}
int main(){
	ull n;
	cin >> n;
	if (n <= 2) {
		cout << 2 << endl;
		return 0;
	}
	if (n == 4 or n== 5) {
		cout << 5 << endl;
		return 0;
	}
	if (n % 2 == 0) {
		n++;
	}
	while (true) {
		if (n % 10 != 5) {
			if (fermat(n)) {
				cout << n << endl;
				return 0;
			}
		}
		n += 2;
	}
	return 0;
}
