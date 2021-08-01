#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>

int main() {
	std::greater<int> gt;
	std::vector<int> myvec = {3, 6, 7, 8, 1};
	std::sort(myvec.begin(), myvec.end(), gt);
	for (auto x : myvec)
		std:: cout << x << " ";
	std::cout << std::endl;
	return 0;

}
