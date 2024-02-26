#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;
std_msgs::Int16 sensorData;

///pub sup
ros::Publisher pub ("Topic_led", &sensorData);

//สร้ างตัวแปร cmd_msg มารั บ std_msgs
void control_LED( const std_msgs::Int16& cmd_msg){
  int value = cmd_msg.data;
  //int sensor = digitalRead(3);
  digitalWrite(13, value );   // blink the led
  //digitalWrite(13, sensor);   // blink the led BT
}
ros::Subscriber<std_msgs::Int16> sub("Topic_led", &control_LED );


void setup()
{ 
  pinMode(13, OUTPUT); ///led
  pinMode(3, INPUT);  //SW
  nh.initNode();
  nh.subscribe(sub); ///สำคัญ
  nh.advertise(pub);
}

void loop()
{  
  sensorData.data = digitalRead(3);
  pub.publish(&sensorData);
  nh.spinOnce();
  delay(1);
}
