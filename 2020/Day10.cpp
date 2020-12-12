#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

vector<int> v;

vector<vector<double>> multip(const vector<vector<double>>& A, const vector<vector<double>>& B) {
    size_t n = A.size();
    vector<vector<double>> result(n, vector<double>(n));
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            for (size_t k = 0; k < n; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i;
    while(cin >> i) {
        v.push_back(i);
    }

    v.push_back(0);
    sort(v.begin(), v.end());

    // Part 1
    int on = 0;
    int th = 0;

    if (v[0] == 1) {
        on++;
    } else if (v[0] == 3) {
        th++;
    }

    for (int i = 1; i < v.size(); i++) {
        if (v[i] - v[i-1] == 1) {
            on++;
        } else if (v[i] - v[i-1] == 3) {
            th++;
        }
    }

    th++; // for last adapter

    // Part 2
    vector<vector<double>> m(v.size(), vector<double>(v.size()));
    vector<vector<double>> p(v.size(), vector<double>(v.size()));

    for (int i = 0; i < v.size(); i++) {
        if (i + 1 < v.size() && v[i+1] - v[i] <= 3) {
            m[i][i+1] = 1;
            p[i][i+1] = 1;
        }
        if (i + 2 < v.size() && v[i+2] - v[i] <= 3) {
            m[i][i+2] = 1;
            p[i][i+2] = 1;
        }
        if (i + 3 < v.size() && v[i+3] - v[i] <= 3) {
            m[i][i+3] = 1;
            p[i][i+3] = 1;
        }
    }

    ll count = 0;
    
    for (int i = 2; i < v.size(); i++) {
        cout << i << "/" << v.size()-1 << '\n';
        p = multip(m, p);
        count += p[0][v.size()-1];
    }

    // Printing results
    cout << "\nPart 1:\n";
    cout << th * on << "\n\n";
    cout << "Part 2:\n";
    cout << count;
}