
let x = 0;
let y = 50;

let hitx = false;
let hity = false;

let speed = 3;

let scal = 30;

function setup() {
  createCanvas(400, 400);
  fill(255, 0, 0)
  frameRate(60)
}

function draw() {
  background(220);
  rect(x, y, scal, scal)
  move()
}

function move(){
  let rand = random(0, 10);
  if (x >= width-scal){hitx = true; x -= rand} else if (x <= 0) {hitx = false; x += rand}
  if (y >= height-scal){hity = true} else if (y <= 0) {hity = false}
  
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
