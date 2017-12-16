#include <bits/stdc++.h>
using namespace std;


typedef pair<int, int> pii;

vector<pii> locations[1000001];
int main() {
  int n, q, x, y, d;
  char c;
  scanf("%d", &n);
  for (int i = 1, a; i <= n; i++) {
    scanf("%d", &a);
    locations[n].push_back(make_pair(0, a));
  }

  scanf("%d", &q);
  for (int i = 0; i < q; i++) {
      scanf("%c %d %d", &c, &x, &y);
      if (c == 'C') {
          locations[x].push_back(make_pair(++d, y));
      }
      else {
			printf("%d\n", locations[x][upper_bound(locations[x].begin(), locations[x].end(), make_pair(y, 0x3F3F3F3F)) - locations[x].begin()].second);
        }

  }
  return 0;
}
