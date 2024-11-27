# include <iostream>

using namespace std;

int main() {
    int a, b;
    cout << "Enter 2 numbers A and B, where A <= B: " << endl;
    cin >> a >> b;

    for (int i = a; i <= b; ++i) {
        if (i >= 1 && i <= 9) {
            string words[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
            cout << words[i - 1] << endl;
        } else if (i % 2 == 0) {
            cout << "even" << endl;
        } else {
            cout << "odd" << endl;
        }
    }
    return 0;
}