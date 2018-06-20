#include <iostream>
#include <unordered_set>
#include <queue>
using namespace std;

const int MAXN = 1000010;
int n, b[MAXN], a[MAXN];
unordered_set<int> s;
queue<int> l8r;

int main(){
  scanf("%d", &n);

  for (int i = 0; i < n; i++){
    scanf("%d", a+i);
    s.insert(a[i]);
  }
  if (s.size() == 1){
    printf("-1\n");
    return 0;
  }

  for (int i = 0; i < n; i++){
    if (s.count(i + 1) == 0){
      l8r.push(i + 1);
    }
  }
  for (int i = n - 1; i > -1; i--){
    if(s.count(a[i]) == 0){
      continue;
    }
    s.erase(a[i]);
    if (i == n - 1) {
      for (int j = 0; j < i; j++){
        if (a[j] != a[i]) {
          b[j] = a[i];
          break;
        }
      }
    } else {
      b[i + 1] = a[i];
    }
  }

  for(int i =0; i < n; i++){
    if (b[i] == 0){
      b[i] = l8r.front();
      l8r.pop();
    }
  }

  for (int i = 0; i < n; i++){
    printf("%i ", b[i]);
  }
  return 0;
}
