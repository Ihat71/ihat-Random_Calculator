import java.util.Scanner;

public class bi_search0 {
    /**
     * @param args
     */
    public static void main(String[] args){
        //In binary search, the array has to be already sorted from either ascending or descending
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

        int low = 0;
        int high = (arr.length-1);
        int mid = mid_getter(low, high);
        int search_value;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter a number between 10 and " + arr[(arr.length-1)] + " in increments of 10: ");
            search_value = sc.nextInt();
        }
            int count = 0;
            //While loop to iteratively make the boundaries smaller. This loop is if the array is ascending order
            while (low <= high){
                if ((arr[low] == search_value)||(arr[high] == search_value)){
                    if (low == search_value){
                    System.out.println("The number is at index: " + low);
                    }
                    else{
                        System.out.println("The number is at index: " + high);
                    }
                    System.out.println("It took " + count + " tries to find");
                    break;
                }
                //This conditional is a secondary base case. As the boundary gets smaller, we get closer to the value and eventually hit this base case.
                else if (arr[mid] == search_value){
                    System.out.println("The number is at index: " + mid);
                    System.out.println("It took " + count + " tries to find");
                    break;
                }
                //If the value at index mid is smaller than the search value, we make the boundary smaller rightwards
                else if (arr[mid] < search_value){
                    low = mid + 1;
                    mid = mid_getter(low, high);
                }
                //Same idea but leftwards
                else if (arr[mid] > search_value){
                    high = mid - 1;
                    mid = mid_getter(low, high);
                }
            
            count++;
            }
        }
    //Method to get the middle index, makes the code simpler
    public static int mid_getter(int low, int high){
            int mid = (low + high)/2;
            return mid;

    }
}
    