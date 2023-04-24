
// const button = document.querySelector('button')

// console.log(button)

// // 1. button.addEventListener( 이벤트 종류, 실행시킬 함수)
// // 2. button.addEventListener( 이벤트 종류, 실행시킬 콜백 함수 )


// button.addEventListener('click', function(){
//   console.log('hello wolrd')
// })

// const input_text = document.querySelector('.text_input')

// input_text.addEventListener('input', function(event){
//   // console.log(event)
//   // console.log(event.target)
//   console.log(event.target.value)

//   const pTag = document.querySelector('p')
//   pTag.textContent = event.target.value
// })


const button = document.querySelector('.plz_button')

button.addEventListener('click',()=>{
  console.log('hello wolrd')
  console.log(this)
})

button.addEventListener('click',function(){
  console.log('hello wolrd')
  console.log(this)
})