#include <ros.h>
#include <std_msgs/Int32.h>

const int InfraredSensorPin = 4;
ros::NodeHandle nh;
std_msgs::Int32 msg;
ros::Publisher pub("/ir", &msg);


void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(pub);
  pinMode(InfraredSensorPin,INPUT);
}

void loop() {
  msg.data = int(digitalRead(InfraredSensorPin));
  pub.publish(&msg);
  nh.spinOnce();
  delay(50);
}
