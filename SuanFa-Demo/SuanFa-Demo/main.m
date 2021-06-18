//
//  main.m
//  SuanFa-Demo
//
//  Created by Alan on 2021/6/17.
//

#import <Foundation/Foundation.h>

void printList(int a[], int count) {
    for (int i = 0; i < count - 1; i++) {
        printf("%d  ", a[i]);
    }
    printf("\n");
}

// 1. 冒泡排序
/// 一个一个比较，然后交换位置
void bubbleSort(int a[], int count) {
    for (int i = 0; i < count - 1; i ++) {
        for (int j = i+1; j < count - 1; j ++) {
            if (a[i] > a[j]) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}

// 2. 冒泡进阶
/// 添加flag标志，如果没有发生交换，则不继续执行for
void bubleSort2(int a[], int count) {
    BOOL flag = YES;
    for (int i = 0; flag && i < count - 1; i ++) {
        flag = NO;
        for (int j = i + 1; j < count - 1; j ++) {
            if (a[i] > a[j]) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                flag = YES;
            }
        }
    }
}

// 3. 选择排序
/**
 两层for：
    第一层：从小到大，约定当前下标 为最小值为index
    第二层：从小到大，查询比a[i]小的值所在的下标
        第二层for结束之后，交换，i和最新值index的位置
*/
void selectSort(int a[], int count) {
    int i, j, temp, minIndex;
    for (i = 0; i < count - 1; i ++) {
        minIndex = i;
        for (j = i + 1; j < count - 1; j++) {
            // 如果后面有比较小的，记录下标
            if (a[j] < a[minIndex]) {
                minIndex = j;
            }
        }
        // 最小值的下标与i不一致，进行交换
        if (i != minIndex) {
            temp = a[i];
            a[i] = a[minIndex];
            a[minIndex] = temp;
        }
    }
}

// 4.插入排序
/**
 两层for循环:
    第一层是 1->10                   从小到大
    第二层则是通过第一层的下标往前 i->1  从大到小
    前面的数据比后面的大，交换。
    找到位置插入
 1: 4  2  7  5  6  1  9  0  8
 2: 4  4  7  5  6  1  9  0  8
 3: 2  4  7  5  6  1  9  0  8
 4: 2  4  7  7  6  1  9  0  8
 5: 2  4  5  7  6  1  9  0  8
 */
void insertSort(int a[], int count) {
    int i, j, temp;
    
    for (i = 1; i < count - 1; i ++) {
        // 把当前元素当做标杆
        temp = a[i];
        // 所有元素与标杆比较，大于temp则交换位置。
        for (j = i; j > 0 && a[j-1] > temp; j --) {
            a[j] = a[j-1];
        }
        // 找到位置了，插入数据
        a[j] = temp;
    }
}

int main(int argc, const char * argv[]) {
    
    int a[10] = {4,2,7,5,6,1,9,0,8,3};
    
    printList(a, 10);
    
    // 冒泡排序
//    bubbleSort(a, 10);
//    bubleSort2(a, 10);
    
    // 选择排序
//    selectSort(a, 10);
    
    //
//    insertSort(a, 10);
    
    printList(a, 10);

    return 0;
}


