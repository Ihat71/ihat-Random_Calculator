import java.util.Arrays;
import java.util.Scanner;
public class selection_sort {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        System.out.println("Enter array size");
        int size = sc.nextInt();
        int[] arr = new int[size];
        System.out.println("Put in numbers");
        for (int x = 0; x < arr.length - 1; x ++){
            int y = sc.nextInt();
            arr[x] = y;
        }
        int min;
        int temp;
        
        for (int i = 0; i<arr.length; i++){
            min = i;
            for (int j = i + 1; j<arr.length; j++){
                if (arr[j] < arr[min]){
                    min = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        
            
    }
    System.out.println(Arrays.toString(arr));

    
}
}
