const isArmstrong = (num) => {
    const digits = num.toString().split('');
    const power = digits.length;
    return digits.reduce((sum, digit) => sum + Math.pow(digit, power), 0) === num;
};


const n = 500; // This number is onlyfor testing
const armstrongNumbers = [];
for (let i = 0; i < n; i++) {
    if (isArmstrong(i)) armstrongNumbers.push(i);
}
console.log(`Armstrong numbers up to ${n}: ${armstrongNumbers.join(', ')}`);
