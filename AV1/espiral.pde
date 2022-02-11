import java.util.concurrent.TimeUnit;
float r = 1;
float theta = 0;

void setup() {
  size(600,600);
  stroke(255);
  background(0);
  strokeWeight(5);
}

void draw() { 
    //limitar o tamanho da espiral
  if(r< 200){
  float x = r * cos(theta);
  float y = r * sin(theta);
  translate(width/2,height/2);
  print(r);
  point(x,y);
  r += 0.1;
  theta += 0.05;
  }
  else{
    //quero pausar por 5 segundos para mostrar a imagem final
    try{
    TimeUnit.SECONDS.sleep(5);
    }
    catch(InterruptedException ex){}
    //limpar a tela e recomecar o desenho
    background(0);
    r = 0;
  }
}