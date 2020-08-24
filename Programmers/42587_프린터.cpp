#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	while (true) {
		if (location == 0) {
			if (priorities[0] == *max_element(priorities.begin(), priorities.end())) {
				answer++;
				break;
			}
			else {
				priorities.push_back(priorities.front());
				priorities.erase(priorities.begin());
				location = priorities.size() - 1;
			}
		}
		else {
			if (priorities[0] == *max_element(priorities.begin(), priorities.end())) {
				priorities.erase(priorities.begin());
				location -= 1;
				answer++;
			}
			else {
				priorities.push_back(priorities.front());
				priorities.erase(priorities.begin());
				location -= 1;
			}
		}
	}
	return answer;
}