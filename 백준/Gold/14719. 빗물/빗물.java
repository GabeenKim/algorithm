import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int H = Integer.parseInt(st.nextToken()); // 높이
		int W = Integer.parseInt(st.nextToken());
		
		int[] blocks = new int[W];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<W ; i++) {
			blocks[i]= Integer.parseInt(st.nextToken());
		}
		
		int quantity=0;
		int left=0, right = W-1;
		int leftMax=0, rightMax=0;
		
		//양쪽 포인터가 만날 때까지 반복
		while(left<right){
			//더 낮은 쪽을 기준으로 물이 고인다. 
			if(blocks[left]<blocks[right]) {
				//현재 외쪽 블록이 이전에 만난 왼쪽 최대높이 보다 높으면 새로운 벽이 되므로 물이 고일 수 없다. 따라서 leftMax 갱신
				if(blocks[left]>=leftMax) {
					leftMax = blocks[left];
				}else {
					//현재 블록이 leftMax보다 낮으면 그 차이만큼 물이 고인다.
					quantity += leftMax - blocks[left];
				}
				//포인터 한 칸 이동
				left++;
			}else { 
				if(blocks[right]>=rightMax) {
					rightMax = blocks[right];
				}else {
					quantity += rightMax - blocks[right];
				}
				right--;
				
			}
		}
		System.out.println(quantity);
		
	}

}
