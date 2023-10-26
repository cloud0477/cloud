function solution(nums) {
    var dataMap = new Object();
    var cnt = 0;
    var max = nums.length/2;
    
    for(temp of nums){
        dataMap[temp] = 1;    
    }
    cnt = Object.keys(dataMap).length;
    
    if( cnt > max ){
        return max;
    }else{
        return cnt
    }
}