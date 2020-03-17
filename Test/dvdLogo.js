
// using p5.js lib

let x = 200;
let y = 200;

let th = 0;

let hitx = false;
let hity = false;

let speed = 3;

let scal = 30;

function setup() {
  createCanvas(400, 400);
  fill(0, 0, 0)
  frameRate(180)
}

function draw() {
  background(220);
  rect(x, y, scal, scal)
  line(x, y, 0, 0)
  line(x+scal, y, width, 0)
  line(x, y+scal, 0, height)
  line(x+scal, y+scal, width, height)
  // move()
  circeler()
}

function move(){
  let rand = random(0, 30);
  if (x >= width-scal){
    hitx = true;
    x -= rand;
  } else if (x <= 0) {
    hitx = false;
    x += rand;
  }
  if (y >= height-scal){
    hity = true
  } else if (y <= 0) {
    hity = false
  }
  
  if (hitx == true){
    x -= speed;
  }else{
    x += speed;
  }
  
  if (hity == true){
    y -= speed;
  }else{
    y += speed;
  } 
}

function circeler(){
  let r = 100;
  let i = 200;
  let j = 200;
  x = i + r * cos(th);
  y = j + r * sin(th);
  th += 0.05
}
       
       
       
       
       
       



