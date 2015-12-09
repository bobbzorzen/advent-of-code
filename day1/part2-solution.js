function calculateSanta(levelString) {
  var currentLevel = 0;
  for(var i = 0; i < levelString.length; i++) {
    levelString.charAt(i) == "(" = currentLevel++ : currentLevel--;
    if(currentLevel < 0) {return i+1}
  }
  return -1;
}
console.log(calculateSanta(input));