// Find the shortest string such that the sum of differences of letters
// results in a target number
#include <string>
#include <iostream>
#include <cstdlib>
int char_diff(const char& a, const char& b){
   if (b > a) return b - a;
   else return a - b;
}

int str_diff(const std::vector<unsigned char>& chars) {
   int sum = 0;
   std::vector<unsigned char>::const_iterator that_it = chars.cbegin();
   for ( ; that_it != chars.cend() - 1; ++that_it) {
      sum += char_diff(*that_it, *(that_it+1));
   }
   return sum
}

bool str_equals_n (const std::vector<unsigned char>& chars, int n) {
   return str_diff(chars, n) == n;
}

for (int n = 0; n <= 4000000; ++n) {
   
}
