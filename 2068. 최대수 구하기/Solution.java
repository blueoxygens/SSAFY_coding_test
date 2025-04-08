import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Stack;
import java.util.Arrays;

class Solution{
    public static void main(String args[]) throws Exception{
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
		int T;
		T= Integer.parseInt(sc.nextLine());
        for(int test_case = 1; test_case <= T; test_case++)
		{
            int[] numbers = Arrays.stream(sc.nextLine().trim().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
            Arrays.sort(numbers);
            Stack<Integer> stack = new Stack<>();
            for (int num : numbers){
                stack.push(num);
            }
            System.out.println("#"+test_case + " "+stack.pop());
        }
        sc.close();
    }
}