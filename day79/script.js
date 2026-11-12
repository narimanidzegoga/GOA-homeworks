// 1) მოცემულია სია const  numbers = [5, 10, 15, 25, 35] for loop ის გამოყენებით იპოვეე სიაში მყოფი რიცხვების ჯამი
// const numbers = [5, 10, 15, 25, 35]
// let total = 0

// for(let i = 0; i<=numbers.length-1; i++) {
//     total += numbers[i]
// }

// console.log(total)

// 2) მოცემულია სია   const  numbers = [5, 10, 15, 26, 35, 38, 450] for loop ის გამოყენებით ეკრანზე გამოიტანე ლუწი რიცხვების ჯამი
// const numbers = [5, 10, 15, 26, 35, 38, 450]
// let total = 0

// for (let i = 0 ; i <=numbers.length-1; i++){

//     if (numbers[i] % 2 == 0){
//         total = total + numbers[i]
//     }
// }

// 3)  შექმენით ცვლადი let number = 6; და დაბეჭდეთ მისი გამრავლების ტაბულა 1-დან 10-მდე.
let number = 6

for (let i = 1; i < 11 ;i++){
    console.log(i*number)
}


// 4) მოცემულია მასივი let numbers = [12, 45, 7, 89, 23, 56]; იპოვეთ მასივში ყველაზე დიდი რიცხვი for loop ის გამოყენებით
// let numbers = [12, 45, 7, 89, 23, 56]
// let biggest = 0
// for (let i = 0 ; i <=numbers.length-1; i++){
//     if (numbers[i] > biggest){
//         biggest = numbers[i]
//     }
// }
// console.log(biggest)


// 5) მოცემულია მასივი let names = ["Nika", "Giorgi", "Ana", "Luka"]; შეამოწმეთ, არის თუ არა მასივში სახელი "Ana"
let names = ["nika", "giorgi", "ana", "luka"];
for (let i = 0; i <names.length-1; i++){
    if (names[i] == "ana"){
        console.log("მასივში არის სახელი ანა")
    }
}