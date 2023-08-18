// set the grade of student
var grade = 1

// assign letter grade based on numerical grade
let letter_grade;

if (grade >= 80 && grade <= 100) {
  letter_grade = 'A';
} else if (grade >= 70 && grade < 80) {
  letter_grade = 'B';
} else if (grade >= 60 && grade < 70) {
  letter_grade = 'C';
} else if (grade >= 50 && grade < 60) {
  letter_grade = 'D';
} else {
  letter_grade = 'E';
}
Document.getElementById("letter_grade").innerHTML
// print the result
console.log(letter_grade);
