#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;
int main(){
  int a;

  scanf("%d", &a);
  if (a == 1 or a == 9){
    cout << 1;
  } else if (a == 2 or a == 3 or a == 8 or a == 7){
    cout << 2;
  } else if (a == 4 or a == 5 or a == 6){
    cout << 3;
  }
  return 0;
}
