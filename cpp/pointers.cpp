#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a, b;
    cout << "Enter 2 numbers (a,b): ";
    cin >> a >> b;
    
    int a1 = a+b;
    int b1 = abs(a-b);
    
    cout << "The sum is: " << a1 << endl;
    cout << "The absolute value of (a-b) is: " << b1 << endl;
    
    
    return 0;
}
