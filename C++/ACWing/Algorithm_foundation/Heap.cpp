#include <iostream>
#include <algorithm>
using namespace std;

const int N = 10e5 + 10;
int heap[N], heap_size;

void heap_up(int k) {
    int cur = k;
    while(cur > 1 && heap[cur] < heap[cur / 2]) {
        swap(heap[cur], heap[cur / 2]);
        cur /= 2;
    }
}

void heap_down(int k) {
    int t = k;
    if (k * 2 <= heap_size && heap[k * 2] < heap[k]) t = k * 2;
    if (k * 2  + 1 <= heap_size && heap[k * 2 + 1] < heap[t]) t = k * 2 + 1;
    if (t != k) {
        swap(heap[t], heap[k]);
        heap_down(t);
    }
}

void heap_insert(int value) {
	
}
int main(){
    int n, m;
    cin >> n >> m;
    // for (int i = 0;i < n;i ++) { //插入O(NlogN)复杂度建堆
    //     int x;
    //     cin >> x;
    //     heap[++ idx] = x;
    //     heap_up(idx);
    // }
    for (int i = 0;i < n;i ++) cin >> heap[++ heap_size];

    for (int i = n / 2;i > 0;i --) heap_down(i);

    while (m --) {
        printf("%d ", heap[1]);
        heap[1] = heap[heap_size --];
        heap_down(1);
    } 
    return 0;
}