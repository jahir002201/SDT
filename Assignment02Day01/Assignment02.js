1.
var result=50;
if(result<0){
    console.log("failed");
}else if(result>=0 && result<40){
    console.log("tumi C grade paico");
}else if(result>=40 && result<60){
    console.log("tumi B grade paico");
}else if(result>=60 && result<70){
    console.log("tumi A- grade paico");
}else if(result>=70 && result<80){
    console.log("tumi A grade paico");
}else if(result>=80 && result<=100){
    console.log("tumi A+ grade paico");
}else{
    console.log("invalid");
}

2.
checkEvenOdd=(number)=>{
    if(number%2==0){
        return "even";
    }else{
        return "odd";
    }
}
var number=15;
var result=checkEvenOdd(number);
console.log(result);

3.
let numbers=[15,3,9,12,6,7,19,8,2,11,5,14,18,17,4,1,10,20,16,13];
for(let i=0;i<numbers.length;++i){
    for(let j=i+1;j<numbers.length;++j){
        if(numbers[i]>numbers[j]){
            let temp=numbers[i];
            numbers[i]=numbers[j];
            numbers[j]=temp;
        }
    }
}
console.log(numbers);

4.
checkLeapYear=(year)=>{
    if((year%4==0 && year%100!=0) || (year%400==0)){
        return "leap year";
    }else{
        return "not a leap year";
    }
}
let year=2025;
let result=checkLeapYear(year);
console.log(result);

5.
for(let i=1;i<=50;++i){
    if(i%3==0 && i%5==0){
        console.log(i);
    }
}

6.
var friends=["rahim","karim","abdul","sadsd","heroAlom"];
let longestName="";
for(let i=0;i<friends.length;++i){
    if(friends[i].length>longestName.length){
        longestName=friends[i];
    }
}
console.log("Longest name is:",longestName);

7.
var numbers=[1,2,3,3,4,4,5,6,7,8,9,10];
let uniqueNumbers=[];
for(let i=0;i<numbers.length;++i){
    if(numbers[i]!=numbers[i+1]){
        uniqueNumbers.push(numbers[i]);
    }
}
console.log("Unique numbers are:",uniqueNumbers);

8.
var numbers=[1,2,3,3,4,4,5,6,7,8,9,10];
let biggestNumber=numbers[0];
for(let i=0;i<numbers.length;++i){
    if(numbers[i]>biggestNumber){
        biggestNumber=numbers[i];
    }
}
console.log("Biggest number is:",biggestNumber);

9.
monthlySavings=(payments,livingCost)=>{
    if(!Array.isArray(payments) || typeof livingCost!='number'){
        return "invalid input";
    }
    let totalIncome=0;
    let totalTax = 0;
    for(let payment of payments){
        totalIncome+=payment;
        if(payment>=3000){
            totalTax+=payment*0.20;
        }
    }
    let totalSavings=totalIncome-totalTax-livingCost;
    if(totalSavings>=0){
        return totalSavings;
    }else{
        return "earn more";
    }
}
let payments=[2503,3230,4310,1503,2830];
let livingCost=3010;
let result=monthlySavings(payments,livingCost);
console.log(result);