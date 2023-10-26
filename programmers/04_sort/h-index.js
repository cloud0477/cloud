function solution(citations) {
    var answer = 0;
    var arrSort = citations.sort((a,b)=>a-b);
    var cnt = 0;
    var len = arrSort.length;
    var i = arrSort.length-1;
    console.log('arrSort : ' + arrSort);
    for(var index=0; index<len ; index++){

        console.log('index : ' + arrSort[index] + ', cnt : ' + cnt);
        while(arrSort[index] >= cnt && len - index >= cnt){
            cnt++;
        }
    }
    return cnt-1;
}