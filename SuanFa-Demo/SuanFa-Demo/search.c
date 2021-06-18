//
//  search.c
//  SuanFa-Demo
//
//  Created by Alan on 2021/6/18.
//

#include <stdio.h>

int binarySearch(int listArray[], int count, int value) {
//    int a[] = {1,2,3,4,5,6,7,8,9,10};
    int index = 0;
    int low = 0;
    
    for (count; count != 0; count >>= 1) {
        index = low + (count >> 1);
        printf("value = %d\n", listArray[index]);
        if (listArray[index] == value) {
            printf("index = %d\n", index);
            return index;
        }
        if (listArray[index] < value) {
            low = index + 1;
            count--;
        }
    }
    return -1;
}
