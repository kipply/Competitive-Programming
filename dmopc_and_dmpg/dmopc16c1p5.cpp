#include <bits/stdc++.h>
using namespace std;
int cactus[500010], n, x, top;
void update(int p, int v) {
	for (int i = p; i < n + 1; i += i &- i)
	    cactus[i] += v;
}
int query(int p) {
	int res = 0;
	for (int i = p; i > 0; i -= i &- i)
	    res += cactus[i];
	return res;
}
int main() {
	cin >> n;
	long long ans = 0;
	for (int i = 0; i < n; i++) {
		cin >> x;
		top = query(x);
		ans += min(top, i - top);
		update(x, 1);
	}
	cout << ans;
}