public class L_2 {
    public static void main(String[] args){
        char[][] charsArray={
            {'c', 'e'},
            {'c', 's'}
        };
        for (int i = 0; i<charsArray.length; i++){
            for (int j = 0; j<charsArray[i].length; j++){
                System.out.print(charsArray[i][j]);
            }
            System.out.println(' ');

        }
    }
}
