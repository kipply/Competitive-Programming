#include <bits/stdc++.h>
using namespace std;


int H, W, h, w;

int main() {
  scanf("%d %d\n%d %d", &H, &W, &h, &w);
  cout << H * W - h * W - (H - h) * w;
  return 0;
} 