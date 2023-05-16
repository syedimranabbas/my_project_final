provider "aws" {
  region = "region"
}
resource "aws_instance" "Demo" {
  ami           = "instance_id"
  instance_type = "instance_type"
  key_name = "key_name"
  tags = {
    Name = "instance_name"
  }
}