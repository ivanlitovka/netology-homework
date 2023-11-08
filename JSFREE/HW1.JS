let username = `Ivan`;
let bonusBalance = 1000;
console.log(`Пользователь: ${username}`);
console.log(`Баланс: ${bonusBalance}`);
for (let i = 1; i <= 7; i++) {
  if (i % 2 == 0) {
    bonusBalance = bonusBalance + 50;
  } else {
    bonusBalance = bonusBalance - 3;
  }
}

console.log(`Баланс через 7 дней: ${bonusBalance}`);