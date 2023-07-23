import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] p;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		//컴퓨터 = 노드 개수 입력 받기 
		int N = Integer.parseInt(st.nextToken());
		//가중치(랜선의 길이)를 기준으로 오름차순 정렬을 위한 우선순위 큐
		PriorityQueue<int[]> q = new PriorityQueue<>((o1,o2)->o1[2]-o2[2]);
		
		//노드 개수 만큼 부모테이블 생성하기 
		p = new int[N+1];
		for(int n=1; n<=N; n++) p[n]=n;

		int length = 0;
		int sumLength = 0;

		for(int i=0; i<N;i++) {
			String line = br.readLine();
			for (int j=0; j<N; j++) {
				length = line.charAt(j)-0;
				//a-z면 1-26으로 저장
				if(length>=97) length-= 96;
				//A-Z면 27-52로 저장
				else length -=38;
				
				//0일 떄를 제외하고 현재 갖고 있는 모든 랜선의 길이를 구한다. 
				if(line.charAt(j)=='0') continue;
				sumLength += length;
				if(i==j) continue;
				//큐에 i와 j 그리고 랜선의 길이를 배열로 삽입한다.
				q.add(new int[] {i,j,length});
			}
		}
		
		//모두 연결이 되어있지 않으면 -1출력해야 하므로 결과갑의 초기값을 -1로 설정함.
		int cnt =0; int result=-1;
		length=0;
		
		if(!q.isEmpty()) {
			int[] comp;
			//큐에서 i,j,랜선의 길이 배열을 꺼내고
			while(!q.isEmpty()) {
				comp = q.poll();
				//i와 j가 같은 그룹이 아니라면 union을 진행한다.
				if(findSet(comp[0])!=findSet(comp[1])) {
					if(union(comp[0],comp[1])) {
						cnt++;
						length+=comp[2];
					}
					//확인한 간선 개수는 N-1이 되면 다 연결된 것이므로 소유길이 - 최소 연결 길이 값을 저장한다.
					if(cnt==N-1) {
						result = sumLength - length;
						break;
					}
				}
				
			}
		}
        if(N==1) result = sumLength;
		System.out.println(result);
		
	}
	public static int findSet(int n) {
		if (p[n]==n) return n;
		return p[n]=findSet(p[n]);
	}
	public static boolean union(int a, int b) {
		if(a>b) p[findSet(a)]=findSet(b);
		else p[findSet(b)]=findSet(a);
		return true;
	}

}
