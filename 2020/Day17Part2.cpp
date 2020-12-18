#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

int arrSize = 20;
int centerIdx = 10;

char v[20][20][20][20];
queue<tuple<int, int, int, int, char>> changes;

void processChanges() {
    while (!changes.empty()) {
        auto& [x,y,z,w,c] = changes.front();
        v[x][y][z][w] = c;
        changes.pop();
    }
}

int checkCell(int x, int y, int z, int w) {
    if (x < 0 || y < 0 || z < 0 || w < 0 || x >= arrSize || y >= arrSize || z >= arrSize || w >= arrSize) {
        return 0;
    }

    if (v[x][y][z][w] == '#') {
        return 1;
    } else {
        return 0;
    }
}

int countActive(int x, int y, int z, int w) {
    int active = 0;
    int d[] = {-1, 0, 1};

    for (int i : d) {
        for (int j : d) {
            for (int k : d) {
                for (int l : d)  {
                    active += checkCell(x + i, y + j, z + k, w + l);
                }
            }
        }
    }
    
    return active;
}

void solve() {
    for (int x = 0; x < arrSize; x++) {
        for (int y = 0; y < arrSize; y++) {
            for (int z = 0; z < arrSize; z++) {
                for (int w = 0; w < arrSize; w++) {
                    if (v[x][y][z][w] == '#') {
                        int active = countActive(x,y,z,w) - 1;
                        if (active != 2 && active != 3) {
                            changes.push({x,y,z,w,'.'});
                        };
                    } else {
                        int active = countActive(x,y,z,w);
                        if (active == 3) {
                            changes.push({x,y,z,w,'#'});
                        };
                    }
                }
            }
        }
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Initialise 3d array
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            for (int k = 0; k < arrSize; k++) {
                for (int l = 0; l < arrSize; l++) {
                    v[i][j][k][l] = '.';
                }
            }
        }
    }

    // Read Input
    string s;
    int x = 0;
    int offset = centerIdx - 4;
    while(cin >> s) { 
        for (int y = 0; y < s.size(); y++) {
            if (s[y] == '#') {
                v[x + offset][y + offset][offset][offset] = '#';
            }
        }
        x++;
    }

    // Simulate Cycles
    int n = 6;
    while (n--) {
        solve();
        processChanges();
    }

    //Count cubes
    int part2 = 0;
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            for (int k = 0; k < arrSize; k++) {
                for (int l = 0; l < arrSize; l++) {
                     if (v[i][j][k][l] == '#') {
                        part2++;
                    }   
                }
            }
        }
    }

    cout << part2;

}