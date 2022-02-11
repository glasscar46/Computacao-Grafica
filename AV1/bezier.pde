void setup()
{
  size(800,800);
}

void draw()
{
  float p1x = 100;
  float p1y = 500;
  float p2x = mouseX;
  float p2y = mouseY;
  float p4x = 700;
  float p4y = 500;
  float p3x = 600;
  float p3y = 100;
  background(120);
  beginShape();
  vertex(p1x,p1y);
  for(float t= 0; t <= 1; t += 0.01)
  {
    float Ax = p1x + t*(p2x-p1x);
    float Bx = p2x + t*(p3x-p2x);
    float Cx = p3x + t*(p4x - p3x);
    
    float Ay = p1y + t*(p2y-p1y);
    float By = p2y + t*(p3y-p2y);
    float Cy = p3y + t*(p4y-p3y);
    
    float Dx = Ax + t*(Bx-Ax);
    float Dy = Ay + t*(By-Ay);
    float Ex = Bx + t*(Cx-Bx);
    float Ey = By + t*(Cy-By);
   
    float pointY = Dy + t*(Ey-Dy);
    float pointX = Dx + t*(Ex-Dx);
    vertex(pointX,pointY);
  } 
  vertex(p4x,p4y);
  endShape();
 }
