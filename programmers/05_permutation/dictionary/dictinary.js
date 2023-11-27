function solution(ori) {
    var answer = 0;
    var len = ori.length;
    var firstW = ori[0];
    var cicleCnt = 0;
    //미리 배열 만들어둠
    const cdata = ['A','E','I','O','U'];
    const CIRCLE_1 = 1;
    const CIRCLE_5 = 5;  //오직 하나의 문자(ex A AA AAA AAAA AAAAA)

    const CIRCLE_4 = 4;  //4자리 총개수 (AAAAX)

    const CIRCLE_24 = 24; //3자리 총개수 (AAAXX)    
    const CIRCLE_6 = 6; //3자리 중간 고정개수 (AAAXX)

    const CIRCLE_124 = 124;//2자리 총 고정개수 (AAXXX)
    //const CIRCLE_6 = 6;//2자리 초반 고정개수 (AAXXX)
    const CIRCLE_31 = 31;//2자리 마지막 고정개수 (AAXXX)

    const CIRCLE_624 = 624;//1자리 총개수 (AXXXX)
    //const CIRCLE_6 = 6;//1자리 초반 고정개수 (AXXXX)
    //const CIRCLE_31 = 31;//1자리 중간 고정개수 (AXXXX)
    const CIRCLE_156 = 156;//1자리 마지막 고정개수 (AXXXX)

    const CIRCLE_SUM = 781; //총합

    //첫번째 문자 확인
    switch(firstW){
        case 'E':
            answer = CIRCLE_SUM;
            break;
        case 'I':
            answer = CIRCLE_SUM*2;
            break;
        case 'O':
            answer = CIRCLE_SUM*3;
            break;
        case 'U':
            answer = CIRCLE_SUM*4;
    }

    //5글자일 경우
    switch(len){
        case 5: //5글자 일경우
            if(ori === 'AAAAA'){ answer += 5; break;}
            else{
                const secondW = ori[1];
                const thirdW = ori[2];
                const fourW = ori[3];
                const fixW = ori[4];
                answer += CIRCLE_5;
                if(secondW === 'A' && thirdW === 'A' && fourW === 'A'){
                    answer += fnSwitch(4,fixW,CIRCLE_1);
                }else if(secondW === 'A' && thirdW === 'A'){
                    answer += CIRCLE_4;
                    answer += fnSwitch(4,fourW,CIRCLE_6)+1;
                    answer += fnSwitch(5,fixW,CIRCLE_1);
                    answer -= 1;//마지막1때문에
                }else if(secondW === 'A'){
                    answer += CIRCLE_4 + CIRCLE_24;
                    answer += fnSwitch(4,thirdW,CIRCLE_31)+1;
                    answer += fnSwitch(5,fourW,CIRCLE_6)+1;
                    answer += fnSwitch(5,fixW,CIRCLE_1);
                }else{
                    answer += CIRCLE_4 + CIRCLE_24 + CIRCLE_124;
                    answer += fnSwitch(4,secondW,CIRCLE_156)+1;
                    answer += fnSwitch(4,thirdW,CIRCLE_31)+1;
                    answer += fnSwitch(5,fourW,CIRCLE_6)+1;
                    answer += fnSwitch(5,fixW,CIRCLE_1);
                }
                answer += 1;
            }
            break;
        case 4: //4글자 일경우
            if(ori === 'AAAA'){ answer += 4; break;}
            else{
                const secondW = ori[1];
                const thirdW = ori[2];
                const fourW = ori[3];
                answer += CIRCLE_5 + CIRCLE_4;
                if(secondW === 'A' && thirdW === 'A'){
                    answer += fnSwitch(4,fourW,CIRCLE_6);
                }else if(secondW === 'A'){
                    answer += fnSwitch(4,thirdW,CIRCLE_31)+1;
                    answer += fnSwitch(5,fourW,CIRCLE_6);
                }else{
                    answer += CIRCLE_24 + CIRCLE_124;
                    answer += fnSwitch(4,secondW,CIRCLE_156)+1;
                    answer += fnSwitch(5,thirdW,CIRCLE_31)+1;
                    answer += fnSwitch(5,fourW,CIRCLE_6);
                }
                answer += 1;
            }
            break;
        case 3: //3글자 일경우
            if(ori === 'AAA'){ answer += 3; break;}
            else{
                const secondW = ori[1];
                const thirdW = ori[2];
                answer += CIRCLE_5 + CIRCLE_4 + CIRCLE_24;
                if(secondW === 'A'){
                    answer += fnSwitch(4,thirdW,CIRCLE_31);
                }else{
                    answer += CIRCLE_124;
                    answer += fnSwitch(4,secondW,CIRCLE_156);
                    answer += fnSwitch(5,thirdW,CIRCLE_31)+1;
                }
                answer += 1;
            }
            break;
        case 2: //2글자 일경우
            if(ori === 'AA'){ answer += 2; break;}
            else{
                const secondW = ori.slice(ori.length-1);
                answer += CIRCLE_5 + CIRCLE_4 + CIRCLE_24 + CIRCLE_124;
                answer += fnSwitch(4,secondW,CIRCLE_156);
            }
            answer += 1;
            break;
        case 1:
            answer += 1;
    }

    console.log('answer : ' + answer);
    return answer;
}

const fnSwitch = function(len, word, value){
    var result = 0;
    if(len === 4){
        switch(word){
            case 'E':
                break;
            case 'I':
                result += value;
                break;
            case 'O':
                result += value*2;
                break;
            case 'U':
                result += value*3;
        }
    }else if(len === 5){
        switch(word){
            case 'A':
                break;
            case 'E':
                result += value;
                break;
            case 'I':
                result += value*2;
                break;
            case 'O':
                result += value*3;
                break;
            case 'U':
                result += value*4;
        }
    }
    return result;
}

const getPermutations= function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1){
        return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

    }
  
    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] // 해당하는 fixed를 제외한 나머지 배열 
      const permutations = getPermutations(rest, selectNumber - 1); // 나머지에 대해 순열을 구한다.
      const attached = permutations.map((permutation) => [fixed, ...permutation].join('')); // 돌아온 순열에 대해 떼 놓은(fixed) 값 붙이기
      results.push(...attached); // 배열 spread syntax 로 모두다 push
    });
  
    return results; // 결과 담긴 results return
};

solution('I');
//const test = ['A','E','I','O','U'];
//const result = getPermutations(test,2)
//console.log('========');
//console.log(result);

/*
기본 5가지
"A", "AA", "AAA", "AAAA", "AAAAA",

1가지경우수(4)  AAAAX
"AAAAE", "AAAAI", "AAAAO", "AAAAU"

2가지경우수(24) AAAXX
"AAAE"(6개) answer += fnSwitch(4,fourW,CIRCLE_6);
    "AAAEA", "AAAEE", "AAAEI", "AAAEO", "AAAEU" answer += fnSwitch(5,fixW,CIRCLE_1);
"AAAI"(6개)
    "AAAIA", "AAAIE", "AAAII", "AAAIO", "AAAIU"
"AAAO"(6개)
    "AAAOA", "AAAOE", "AAAOI", "AAAOO", "AAAOU"
"AAAU"(6개)
    "AAAUA", "AAAUE", "AAAUI", "AAAUO", "AAAUU"

3가지 경우수(124) AAXXX
(31개 * 4 = 124)
AAE(31개) answer += fnSwitch(4,thirdW,CIRCLE_31);
    AAEA(6개) answer += fnSwitch(5,fourW,CIRCLE_6);
        AAEAA,AAEAE,AAEAI,AAEAO,AAEAU answer += fnSwitch(5,fixW,CIRCLE_1);
    AAEE(6개)
        AAEEA,AAEEE,AAEEI,AAEEO,AAEEU
    AAEI(6개)
        AAEIA,AAEIE,AAEII,AAEIO,AAEIU
    ...
AAI(31개)...
AAO(31개)...
AAU(31개)...

4가지 경우수(624) AXXXX
AE (31개*5 + 1 = 156) answer += fnSwitch(4,secondW,CIRCLE_156);
    AEA(31개) answer += fnSwitch(5,thirdW,CIRCLE_31);
        AEAA(6개) answer += fnSwitch(5,fourW,CIRCLE_6);
            AEAAA AEAAE AEAAI AEAAO AEAAU answer += fnSwitch(5,fixW,CIRCLE_1);
        AEAE...
        AEAI...
        AEAO...
        AEAU...
    AEE(31개)...
    AEI(31개)...
    AEO(31개)...
    AEU(31개)...
AI (156개)...
AO (156개)...
AU (156개)...
157*4 = 624

총 => 781

E차례

기본 5가지
E EA EAA EAAA EAAAA

1가지 경우수(4) EAAAX
EAAAE EAAAI EAAAO EAAAI EAAAU

2가지 경우수(24) EAAXX
"EAAE"(6개)
    "EAAEA", "EAAEE", "EAAEI", "EAAEO", "EAAEU"
"EAAI"(6개)
    "EAAIA", "EAAIE", "EAAII", "EAAIO", "EAAIU"
"EAAO"(6개)
    "EAAOA", "EAAOE", "EAAOI", "EAAOO", "EAAOU"
"EAAU"(6개)
    "EAAUA", "EAAUE", "EAAUI", "EAAUO", "EAAUU"

3가지 경우수(124) EAXXX

4가지 경우수(624) EXXXX

반복...

*/