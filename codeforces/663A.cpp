#include <bits/stdc++.h>

using namespace std;

int x1, yy1, x2, y2, x, y; 


int main(){
  scanf("%d %d %d %d", &x1, &yy1, &x2, &y2); 
  scanf("%d %d", &x, &y); 

  string ans = "NO"; 

  if ((x2-x1) % x == 0 && (y2-yy1) % y == 0 && (abs(y2-yy1)/y % 2 == abs(x2-x1)/x % 2)) {
    ans = "YES"; 
  }
  cout << ans;
  return 0;
}
 