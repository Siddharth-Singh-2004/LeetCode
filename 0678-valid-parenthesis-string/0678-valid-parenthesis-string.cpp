class Solution {
public:
    bool checkValidString(string s) {
        int leftmin = 0;
        int leftmax = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                leftmin++;
                leftmax++;
            }
            else if (s[i] == ')') {
                leftmin--;
                leftmax--;
            }
            else if (s[i] == '*') {
                leftmin--;
                leftmax++;
            }

            if (leftmax < 0) {
                return false;
            }
            if (leftmin < 0) {
                leftmin = 0;
            }
        }

        if (leftmin == 0) {
            return true;
        }
        else {
            return false;
        }
    }
};