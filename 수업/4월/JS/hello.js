/*
const threeArgs = function (arg1, arg2, arg3) {
  console.log([arg1, arg2, arg3])
}

threeArgs(1, 2, 3)
threeArgs(1, 2)
threeArgs(1)

const restArgs = function (ar1, ar2, ...restArgs) {
  console.log(restArgs)
}

restArgs(1, 2, 3, 4, 5)

const arrow = name => `hello ${name}`
console.log(arrow('world'))

let noArgs = _ => console.log('no args')

let returnObject = _ => { return { name: 'world' } }

returnObject() = () => ({ name: 'world' })

const myfunction = _ => {
  console.log(this)
}

myfunction()

const myobj = {
  numbers : [1,2],
  myfunc(){
    console.log(this)
    this.numbers.forEach(function(numbers){
      console.log(numbers)
      console.log(this)
    })
  }
}

myobj.myfunc()

const myobj = {
  numbers : [1,2],
  myfunc(){
    console.log(this)
    this.numbers.forEach((numbers)=>{
      console.log(numbers)
      console.log(this)
    })
  }
}

myobj.myfunc()

let x = 1

function first() {
  let x = 10
  second()
}

function second() {
  console.log(x)
}

first()
second()

const numbers = [1, 2, 3, 4, 5, 6, 7]

numbers.reverse()
console.log(numbers)

numbers.push(10)

console.log(numbers)

numbers.unshift()

console.log(numbers)

console.log(numbers.pop())

console.log(numbers.includes(10))

const numbers = [1,2,3]
numbers.forEach(function(number){
  console.log(number**2)
})

const callback = function(num){
  console.log(num**2)
}

const numbers = [1,2,3]

numbers.forEach(callback)

const obj = {
  f : () => {
    console.log(this)
  },
  f2 () {
    console.log(this)
  },
}

obj.f()
obj.f2()

//forEach - 반환값 없음.
//map - 반환값 있음.

const arr = [1,2,3,4,5,6,7,8,9,10,11,12]

const test = (el, index, array) => {
  return el + 23
}

const arr = [4,3,5,1,6,5]
let cnt = 0
const count = function(el){
  if (el%2 === 1){
    cnt += 1
  }  
}
arr.forEach(count)

console.log(cnt)

const arr = [-5,3,4,2,-7,-2,7];
const pplus = []
const mminus = []

const f = (arr)=>{
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      pplus.push(arr[i])
    }
    else if (arr[i] < 0){
      mminus.push(arr[i])
    }
  }
}

f(arr)

console.log(pplus)
console.log(mminus)

const arr = [1,2,3,4,5]

console.log(arr.map((x) =>{
  return x**2
}))

const arr = [1,2,3,4,5,6,7,8,9,10];

const arr1 = arr.filter(el => el % 2 === 1)
const arr2 = arr.filter(el => el > 3 && el < 9)

console.log(arr1)
console.log(arr2)

const bucketlist = [
  {
    id:1,
    text:"여행가기",
    done:false,
  },
  {
    id:2,
    text:"치킨 먹기",
    done:true,
  }
]

const f1 = bucketlist.filter(el => el.done === false)

console.log(f1)
const array = [1, 2, 3, 4]

console.log(array.reduce((acc, cur) =>{
  const data = cur*cur;
  acc.push(data);
  return acc;
}, []))


const me = {
  name: 'shin',
  age: '28',
  hobby: 'coding',
  phone_number: '010-1234-5678',
  adress: 'pusan',
}

console.log(me)
*/
