 int E =13;
  int D =12;
  int C =11;
  int DP =10;
  int B =9;
  int A =8;
  int F =7;
  int G =6;
void one()
{
  digitalWrite(E, HIGH);
  digitalWrite (D, HIGH);
  digitalWrite (C, HIGH);
  digitalWrite (DP, HIGH);
  digitalWrite (B,HIGH);
  digitalWrite (A, HIGH);
  digitalWrite (F, LOW);
  digitalWrite (G, HIGH);
}
void setup() {
  // put your setup code here, to run once:
 pinMode(E,OUTPUT);
pinMode(D,OUTPUT);
pinMode(C,OUTPUT);
pinMode(DP,OUTPUT);
pinMode(B,OUTPUT);
pinMode(A,OUTPUT);
pinMode(F,OUTPUT);
pinMode(G,OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
one();
}
