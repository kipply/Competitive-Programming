#include <iostream>
using namespace std;

int n, c, a, b, cactus[1000000];
int main(){
	scanf("%i %i", &n, &c);
	for (int i = 0; i < c; i++){
		scanf("%i %i", &a, &b);
		cactus[a] += 1;
		cactus[b] += 1;
	}
	int hi = 1;
	c = cactus[1];
	for(int i = 1; i <= n; i++){
		if (cactus[i] >= hi){
			hi = cactus[i];
			c = i;
		}
	}
	cout << c;
	return 0;
}
