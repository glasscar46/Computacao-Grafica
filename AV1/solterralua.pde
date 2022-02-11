
void setup(){
  size(800,800);
  frameRate(24);
}

void draw(){
  background(100);
  translate(width/2,height/2);
  fill(255,0,0);
  circle(0,0,120);
  rotate(frameCount/(20*TWO_PI));
  translate(width/8,-height/4);
  fill(0,0,255);
  circle(0,0,60);
 rotate(frameCount/(5*TWO_PI));
  translate(width/20,-height/10);
  fill(240,240,240);
  circle(0,0,30);
}
