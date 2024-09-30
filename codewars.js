function arrayDiff(a, b) {
  for (elemA of a) {
    for (elemB of b) {
      let elemIndex = a.indexOf(elemB);
      while (elemIndex > -1) {
        a.splice(elemIndex, 1);
        elemIndex = a.indexOf(elemB);
      }
    }
  }
  return a
}


console.log(arrayDiff([1,2,2,2,3,3,4], [1,3]))