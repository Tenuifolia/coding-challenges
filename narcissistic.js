function narcissistic(value) {
  const valueString = value.toString()
  const numDigits = valueString.length

  let rollingSum = 0

  for (digit of valueString) {
    rollingSum += parseInt(digit, 10) ** numDigits
  }

  if (rollingSum == value) {
    return true
  }

  return false


}

console.log(narcissistic(153))
