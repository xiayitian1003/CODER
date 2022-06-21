//#include <iostream>
//#include <cstring>
//using namespace std;
//
//int main(){
//	string S, P;
//	int n, m;
//	cin >> n >> P >> m >> S;
//	
//	for (int i = 0, j = 0;i < m;i ++) {
//		
//		while(P[j] == S[i] && j < n) {
//			j ++;
//			i ++;
//		}
//		if (j == n) { 
//			cout << i - n;	
//		} 
//		j = next[j] + 1;
//	}
//	return 0;
//}
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1000010;

int n, m;
char s[N], p[N];
int ne[N];

int main()
{
    cin >> m >> p >> n >> s;

	ne [0] = -1;
	for (int i = -1, j = 1;j < m;j ++) {
		while (i > -1 && p[i + 1] != p[j]) i = ne[i];
		
		if(p[i + 1] == p[j]) i ++;
		ne[j] = i;
	}
	
	for (int i = 0;i < m;i ++) {
		cout << ne[i] << endl;
	}
	
	for (int i = -1, j = 0;j < n;j ++) {
		while (i > -1 && p[i + 1] != s[j]) i = ne[i];
		
		if (p[i + 1] == s[j]) i ++;
		if (i == m - 1) {
			cout << j - m + 1 << endl;
		}
	}
    return 0;
}