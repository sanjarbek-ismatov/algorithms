function romanToInt(s) {
  const data = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const string = [...s];
  let numdata = 0;
  string.forEach((e) => {
    numdata += data[e];
    console.log(data[e]);
  });
  return numdata;
}
romanToInt("MCMXCIV");
