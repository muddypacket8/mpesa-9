// Javascript code to product elements in array
  
// array Elements
let arr = [1,2,3,4,5];
let product = 1;
  
// initialize start and last pointers
let i = 0;
let j = arr.length-1;
  
// add first and last simultaneously 
while(i < j)
{
    product *= arr[i]*arr[j];
    i += 1;
    j -= 1;
}
      
// multiply only one element
if(i == j)
    product *= arr[i];
  
// printing product
console.log(product);