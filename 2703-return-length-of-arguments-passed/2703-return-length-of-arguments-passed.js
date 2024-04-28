function argumentsLength(...args) {
  let length = 0;
  for (let arg of args) length += 1;
  return length;   
}