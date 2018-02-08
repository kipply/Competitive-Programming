#include <bits/stdc++.h>

using namespace std;

int city[30001][1001];

int main(){
    // how does cpp work?
    int r, c, k;
    int x, y, ra, b;

    scanf("%d%d%d", &r, &c, &k);

    for (int i = 0; i < k; i++){
        scanf("%d %d %d %d", &x, &y, &ra, &b);
        y--; x--;
        for (int j = -ra; j <= ra; j++){
            int w = (int)sqrt(ra * ra - j * j);
            int x1 = max((int)(x - w), 0);
            int x2 = min((int)(x + w), c - 1);
            if (y + j < r && y + j >= 0){
                city[y + j][x1] += b;
                city[y + j][x2 + 1] -= b;
            }
        }
    }

    int bit = 0, num = 0;

    for (int i = 0; i < r; i++){
        int temp = 0;
        for (int j = 0; j < c; j++){
            temp += city[i][j];

            if (temp > bit){
                bit = temp;
                num = 1;
            } else if (temp == bit){
                num++;
            }
        }
    }

    printf("%d\n%d", bit, num);

    return 0;
}
