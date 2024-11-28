#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int highest_num(int a, int b, int c, int d)
{
  return max({a, b, c, d});
}

int main()
{

  int a, b, c, d;
  cout << "Enter 4 random Numbers: " << endl;
  cin >> a >> b >> c >> d;

  cout << "The highest number is: " << highest_num(a, b, c, d);

  return 0;
}
