#include<iostream>
using namespace std;

void Reverse(int* arr, int length){
    for(int i = 0; i <= length/2-1; i++){
        swap(arr[i],arr[length-i-1]);
    }
}

void BubbleSort(int* arr, int length){
    //从小到大排序
    for (int i = length-1; i >= 1; i--){
        for(int j = 0; j<i ;j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void QuickSort(int* arr, int left, int right){
    if(left>=right){
        return;
    }

    int temp,i,j;
    i = left;
    j = right;
    temp = arr[left];
    while(i!=j){
        while(arr[j] <= temp && i<j){
            j--;
        }
        while(arr[i] >= temp && i<j){
            i++;
        }
        if(i<j){
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[left],arr[i]);
    QuickSort(arr, left,i-1);
    QuickSort(arr,i+1,right);
}


int main(){
    int arr[8] = {1,5,6,3,4,2,7,8};
    QuickSort(arr,0,7);
    for(int i = 0;i<8;i++){
        printf("%d",arr[i]);
    }
    getchar();
    return 0;
}





