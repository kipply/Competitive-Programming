#include <bits/stdc++.h>

using namespace std;

char cactus[4][4]; 

int dx[] = {0, 0, 1, -1, 1, -1, -1, 1}; 
int dy[] = {1, -1, 0, 0, 1, -1, 1, -1}; 

int main(){
  for (int i = 0; i < 4; i++) {
    scanf("%s", cactus[i]); 
  }

  string answer = "NO"; 

  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (cactus[i][j] != 'x') {
        continue; 
      }

      for (int x = 0; x < 8; x++) {
        if (i + dx[x] * 2 >= 4 || i + dx[x] * 2 < 0) { 
          continue; 
        }
        if (j + dy[x] * 2 >= 4 || j + dy[x] * 2 < 0) { 
          continue; 
        }

        if (cactus[i + dx[x]][j + dy[x]] != 'o' && cactus[i + dx[x] * 2][j + dy[x] * 2] == 'x') {
          answer = "YES";
        }
        if (cactus[i + dx[x]][j + dy[x]] == 'x' && cactus[i + dx[x] * 2][j + dy[x] * 2] == '.') {
          answer = "YES";
        }
      }
    }
  }
  cout << answer << endl;
  return 0;
}
