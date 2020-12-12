#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int max = 0;
    vector<bool> v(1024, 0);
    while (cin >> s) {
        int id = 0;

        for (int i = 0; i < 10; i++) {
            if (s[9-i] == 'B' || s[9-i] == 'R') {
                id += pow(2, i);
            }
        }

        v[id] = true;
        if (id > max) {
            max = id;
        }
    }

    cout << "Part 1:\n";
    cout << max << "\n\n";
    cout << "Part 2:\n";

    for (int i = 1; i < v.size() - 1; i++) {
        if (!v[i] && v[i-1] && v[i+1]) {
            cout << i;
            break;
        }
    }
}