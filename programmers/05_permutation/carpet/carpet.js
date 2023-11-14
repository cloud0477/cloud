
function solution(brown, yellow) {
    var answer = [];

    var n=1;
    while(n <= yellow/2){
        if( (yellow/n)*2 + (n+2)*2 == brown ) break;
        else n++;
    }
    console.log([(yellow/n)+2, n+2]);
    return [(yellow/n)+2, n+2];
}

//solution(10,2);
//solution(8,1);
solution(24,24);
//solution(4004,999999);

//[4004,999999]
//맞는답: [1003,1001]

//1 => 24*2 + 3*2
//2 => (24/2)*2 + 4*2
//3 => (24/3)*2 + 5*2
//4 => (24/4)*2 + 6*2 = 12 + 12 = 24
//....
//n => (y/n)*2 + (n+2)*2 = b
//width = (y/n)+2, length = n+2