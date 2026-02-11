import java.util.Arrays;

public class Quiz_idk{
    public static void main(String[] args){
    float[] buildingHeights = {2.56f, 6.54f, 7.12f, 4.45f, 3.22f};
    insertionSort(buildingHeights);
    // displayArray(buildingHeights)
    System.out.println(Arrays.toString(buildingHeights));


    }
    public static void insertionSort(float[] heights){
        // idkidkidkidkidkidkidkidkidk
        int in, out;
        float temp;
        for (out = 1; out <= heights.length - 1; out++){
            temp = heights[out];
            
            for (in = out - 1; in >= 0 && heights[in] > temp;in--){
                heights[out] = heights[in];   
            }
            heights[in+1] = temp;
        }
    }
    public static void selectionSort(float[] heights){
        int min;
        for (int out = 0; out < heights.length-1;out++){
            System.out.println("Outer: " + out); 
            min = out; //consider the number I am pointing at as the minimum #. Now we need to check the neighbors
            // we need an inner loop that will scan the remaining number
            for (int in = out + 1; in < heights.length; in++){
                System.out.println("Inner:" + in); 
                if (heights[in] < heights[min]){
                    min = in; // now we found the smallest number
                }
        }
        }
        
    }
    public static void swap(float[] heights, int min, int out){
        float temp = 2;
    }
}