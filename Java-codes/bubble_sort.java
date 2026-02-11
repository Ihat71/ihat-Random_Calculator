import java.util.Arrays;

public class bubble_sort{
    public static void main(String[] args){
        //int[] arr = {5, 7, 3, 2, 4, 1, 0, 6};
        int[] arr = {0,1,2,3,4,5,6,7};
        boolean swapped;
        int counter = 0;
        int temp = 0;
        for (int i = 0; i<arr.length-1;i++){
            swapped = false;
            for (int j = 0; j<arr.length - 1 - i;j++){
                if (arr[j] <= arr[j+1]){
                    continue;
                }
                else if (arr[j] > arr[j+1]){
                    temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                    swapped = true;
                
                }
            }
            if (swapped == false){
                break;
            }
            counter++;
            
        }
        System.out.println(Arrays.toString(arr));
        System.out.println(counter);


    }

}