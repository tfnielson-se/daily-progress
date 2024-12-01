#include <iostream>
#include <string>
#include <vector>
#include <cstdlib> // For rand()
#include <ctime>   // For seeding rand()

using namespace std;

int main()
{
    vector<string> words = {"one", "two", "three", "four", "five"};
    int words_len = words.size();

    // Seed the random number generator
    srand(time(0));

    // Generate a random index
    int rand_word = rand() % words_len;

    // Output the randomly selected word
    cout << "Random word: " << words[rand_word] << endl;

    return 0;
}
