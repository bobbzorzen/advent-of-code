function calculateSanta(levelString) {
  var currentLevel = 0;
  for(var i = 0; i < levelString.length; i++) {
    levelString.charAt(i) == "(" = currentLevel++ : currentLevel--;
  }
  return currentLevel;
}
console.log(calculateSanta(input));