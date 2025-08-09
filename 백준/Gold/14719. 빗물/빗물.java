import java.util.*;
import java.io.*;

public class Main{

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int H = Integer.parseInt(st.nextToken()); // 높이
		int W = Integer.parseInt(st.nextToken());
		
		List<Integer> list = new ArrayList<>();
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<W ; i++) {
			list.add(Integer.parseInt(st.nextToken()));
		}
		
		int rightMax =0, leftMax=0, quantity=0;
		for(int i=1; i<W-1; i++) {
			rightMax = Collections.max(list.subList(i+1,W));
			leftMax = Collections.max(list.subList(0,i));
			
			int lowerOne = Math.min(leftMax,rightMax);
			if(list.get(i)<lowerOne) {
				quantity += lowerOne-list.get(i);
			}
		}
		System.out.println(quantity);
		
	}

}
