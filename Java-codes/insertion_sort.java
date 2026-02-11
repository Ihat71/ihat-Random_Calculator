public class insertion_sort {
    public static void main(String[] args) {
        
    }
    public static void Insertion(int[] numbers){
        int temp, in;
        for (int out = 1; out < numbers.length; out++){
            // current position
            temp = numbers[out];
            // another loop for sorted area
            for (in = out-1; (in >= 0) && (numbers[in] > temp);in--){
                numbers[in + 1] = numbers[in];
            }
            numbers[in + 1] = temp;
        }
    }
}
