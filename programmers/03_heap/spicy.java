import java.util.PriorityQueue;

class Solution {

    public int solution(int[] scoville, int K) {

        int answer = 0;

        PriorityQueue<Integer> arr = new PriorityQueue<Integer>();

        for(int temp:scoville){

            arr.add(temp);

            }

        while(arr.size()>1&&arr.peek()<K){

          
            int data1 = arr.remove();

            int data2 = arr.remove();

                answer++;

               arr.add(data1+(data2*2));

        }

        if(arr.peek()<K) answer = -1;

        return answer;

    }

}