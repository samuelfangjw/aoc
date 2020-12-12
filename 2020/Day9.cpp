#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> v;
    int t;
    while (cin >> t) {
        v.push_back(t);
    }

    // Part 1
    vector<int> v1(25, 0);
    int ans;

    for (int i = 0; i < 25; i++) {
        v1[i] = v[i];
    }

    for (int k = 25; k < v.size(); k++) {
        bool res = true;
        for (int i = 0; i < 25; i++) {
            for (int j = i+1; j < 25; j++) {
                if (v1[i] + v1[j] == v[k]) {
                    res = false;
                }
            }
        }

        if (res) {
            cout << "Part 1:\n";
            cout << v[k] << "\n\n";
            ans = v[k];
            break;
        }

        v1.erase(v1.begin());
        v1.push_back(v[k]);
    }

    // Part 2
    vector<ll> prefixSum(v.size()+1, 0);
    ll sum;

    for (int i = 1; i <= v.size(); i++) {
        sum += v[i];
        prefixSum[i] = sum;
    }

    int i = 0;
    int j = 0;

    while(i < prefixSum.size()) {
        j = i + 2;
        bool found = false;
        while(j < prefixSum.size()) {
            if (prefixSum[j] - prefixSum[i] == ans) {
                found = true;
                break;
            }
            j++;
        }

        if (found) {
            break;
        }

        i++;
    }

    int smallest = INT32_MAX;
    int largest = 0;
    for (int k = i+1; k <= j; k++) {
        smallest = min(smallest, v[k]);
        largest = max(largest, v[k]);
    }

    cout << "Part 2:\n";
    cout << smallest + largest;

    // Original Part 2 Solution
    // for (int i = 3; i < 100; i++) {
    //     for (int j = 0; j < v.size() - i; j++) {
    //         int sum = 0;
    //         int smallest = INT32_MAX;
    //         int largest = 0;

    //         for (int k = 0; k < i; k++) {
    //             sum += v[j+k];
    //             smallest = min(smallest, v[j+k]);
    //             largest = max(largest, v[j+k]);
    //         }

    //         if (sum == ans) {
    //             cout << "\nPart 2:\n";
    //             cout << smallest + largest;
    //             return 0;
    //         }
    //     }
    // }
}