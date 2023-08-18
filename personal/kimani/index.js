function filterStringsStartingWithA(strings) {
    return strings.filter(function(s) {
      return s.startsWith("A");
    });
  }
  var words = ["batman", "Barry", "Appeal", "app", "Apes of the dawan"];
  var aWords = filterStringsStartingWithA(words);
  console.log(aWords);
  