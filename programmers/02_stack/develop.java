import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<Integer>(); 
        List<Integer> data1 = Arrays.stream(progresses).boxed().collect(Collectors.toList());
        List<Integer> data2 = Arrays.stream(speeds).boxed().collect(Collectors.toList());
        int save = 0;
        while(!data1.isEmpty() && !data2.isEmpty()) {
        	int cnt = 0;
        	for(int i=0;i<data1.size();i++) {
        		data1.set(i, data1.get(i) + data2.get(i));
        	}
        	while(data1.size()>0 && data1.get(0)>99) {
        		cnt++;
        		data1.remove(0);
        		data2.remove(0);
        	}
        	if(cnt>0) {
        		answer.add(cnt);
        	}
        }
        
        return convertIntArray(answer);
    }
    
    public int[] convertIntArray(List<Integer> data) {
		int[] answer = new int[data.size()];
		
		for(int i=0;i<data.size();i++) {
			answer[i] = data.get(i);
		}
		
		return answer;
	}
}