import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    public static void main(String[] args) {
        try{
            System.setIn(new FileInputStream("./input.txt"));
        }
        catch(Exception e){
            System.out.println("파일이 존재하지 않습니다.");
        }
        Scanner sc = new Scanner(System.in);
        int N =  Integer.parseInt(sc.nextLine());
        String[] arr = sc.nextLine().split(" ");
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0; i<N; i++){
            list.add(Integer.parseInt(arr[i]));
        }
        Collections.sort(list);
        System.out.println(list.get(list.size()/2));
    }
}