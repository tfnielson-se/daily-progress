#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  int list_length;
  cout << "Enter number of numbers to input: ";
  cin >> list_length;

  vector<int> nums(list_length);

  cout << "Enter numbers one at a time, followed by enter: ";
  for (int i = 0; i < list_length; i++)
  {
    cin >> nums[i];
  }

  vector<int> nums_reversed = nums;
  reverse(nums_reversed.begin(), nums_reversed.end());

  cout << "Numbers reversed: ";
  for (int i = 0; i < list_length; i++)
  {
    cout << nums_reversed[i] << " ";
  }
  return 0;
}
