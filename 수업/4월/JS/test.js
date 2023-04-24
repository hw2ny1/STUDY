const arr = [1,2,3,4,5]

const rlt = arr.reduce((acc, el) =>{
  if (!(el % 2)) acc.push(el**2)
  return acc
},[])

console.log(rlt)

///////////////////////////////////////



///////////////////////////////////////

