#include <iostream>
using namespace std;
const int N = 10e6 + 10;
int a[N], q[N], hh, tt = -1;

int main(){
    int n = 0, k = 0;
    cin >> n >> k;
    for (int i = 0;i < n;i ++) cin >> a[i];
    
    for (int i = 0;i < n;i ++) {
    	printf("insert a[i] = %d\n", a[i]);
    	q[++ tt] = a[i];
    	printf("after insert hh: %d, tt: %d\n", hh, tt);
    	if (tt - hh + 1 > k) hh ++;
    	printf("after limit size hh: %d, tt: %d\n", hh, tt);
    	while (hh < tt && q[hh] >= q[tt]) hh ++;
		printf("after monotone hh: %d, tt: %d\n", hh, tt);
		for (int j = hh;j <= tt; j ++) cout << q[j] << '~';
    	cout << endl;
    	for (int i = 0;i <= tt; i ++) cout << q[i] << '/';
    	cout << endl;
    	if (i >= k - 1) cout << "answer: " <<q[hh] << endl << endl;
	}
    return 0;
}