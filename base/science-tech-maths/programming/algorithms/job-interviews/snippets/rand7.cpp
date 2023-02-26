int rand5() { return 4; }

// rand5: 0 1 2 3 4
// 2*rand5: 0 2 4 6 8 we need 5 between consecutive items, to be able to add an other rand5
// 3*rand5: 0 3 6 9 12 still not good...

// 5*rand5: 0 5 10 15 20 better! now add rand5
// 5*rand5: 0+rand5 5+rand5 etc...

// if > 21: resample...
// else %7

// Incorrect Solutions:
// Addition: rand5() + rand5() +...
// When you add, the probability of the middle numbers become more as there are more ways to get them. For example, when
// you roll a pair of dice, you can get numbers from 2 to 12. However the probability for getting a 2 is 1/36, and the
// probability of getting a 7 is 1/6.

// The rand5()%2 will generate  0 and 1 with equal probability and we need 3 bits since we are going from 000 upto 111.
// So we call this function thrice for each bit position.
int rand7_binary() {
    while (true) {
        int n = ((rand5() % 2) * 4 + (rand5() % 2) * 2 + (rand5() % 2) * 1);
        if (n == 0) continue;
        return n;
    }
}

int rand7_two_axes() {
    int vals[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 1, 2, 3}, {4, 5, 6, 7, 1}, {2, 3, 4, 5, 6}, {7, 0, 0, 0, 0}};

    int result = 0;
    while (result == 0) {
        int i = rand5();
        int j = rand5();
        result = vals[i - 1][j - 1];
    }
    return result;
}
