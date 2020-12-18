#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

queue<char> q;

ll solve1() {
    ll sum = 0;
    char op = '+';

    while (!q.empty()) {
        char next = q.front();
        q.pop();

        if (next == '(') {
            if (op == '+') {
                sum += solve1();
            } else {
                sum *= solve1();
            }
        } else if (next == ')') {
            break;
        } else if (next == '+') {
            op = '+';
        } else if (next == '*') {
            op = '*';
        } else { 
            if (op == '+') {
                sum += (next - '0');
            } else {
                sum *= (next - '0');
            }
        }
    }

    return sum;
}

void toPostfix(string t){
    stack<char> s;
    for (char c : t) {
        if (c == '(') {
            s.push('(');
        } else if (c == '+') {
            s.push('+');
        } else if (c == '*') {
            while (!s.empty() && s.top() == '+') {
                q.push('+');
                s.pop();
            }
            s.push('*');
        } else if (c == ' ') {
            continue;
        } else if (c == ')') {
            while (s.top() != '(') {
                q.push(s.top());
                s.pop();
            }
            s.pop();
        } else {
            q.push(c);
        }
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }
}

ll solve2() {
    stack<ll> s;
    while (!q.empty()) {
        if (q.front() == '+') {
            ll first = s.top();
            s.pop();
            ll second = s.top();
            s.pop();
            s.push(first + second);
        } else if (q.front() == '*') {
            ll first = s.top();
            s.pop();
            ll second = s.top();
            s.pop();
            s.push(first * second);
        } else {
            s.push(q.front() - '0');
        }
        q.pop();
    }

    ll result = s.top();
    s.pop();
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string t;
    ll part1 = 0;
    ll part2 = 0;
    while (getline(cin, t)) {
        q.push('(');
        for (int i = 0; i < t.length(); i++) {
            if (t[i] != ' ') {
                q.push(t[i]);
            }
        }
        q.push(')');

        part1 += solve1();

        toPostfix(t);
        part2 += solve2();
    }

    cout << "Part 1: " << part1 << '\n';
    cout << "Part 2: " << part2 << '\n';
}