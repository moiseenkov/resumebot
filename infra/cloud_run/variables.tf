variable "name" {
  type        = string
  description = "CloudRun service name"
}

variable "location" {
  type        = string
  description = "CloudRun service location"
}

variable "image" {
  type        = string
  description = "Docker Image URL"
}

variable "cpu" {
  type        = string
  description = "CPU limit"
}

variable "memory" {
  type        = string
  description = "Memory limit"
}


variable "health_url" {
  type        = string
  description = "Health check URL"
}