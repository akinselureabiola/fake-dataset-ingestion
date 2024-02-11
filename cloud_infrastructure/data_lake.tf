resource "aws_s3_bucket" "faker" {
  bucket = "faker-raw-dataset"

  tags = {
    Team        = "Data Engineers"
    Manage_by_terraform = "True"
    service = "Airflow"
  }
}
