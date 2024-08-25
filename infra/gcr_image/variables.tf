variable "project_id" {
  type        = string
  description = "Project ID"
}

variable "location" {
  type        = string
  description = "Location"
}

variable "repository_id" {
  type        = string
  description = "Artifact Registry Repository ID"
}

variable "image" {
  type = object({
    name   = string
    sha256 = string
    tag    = optional(string, "")
  })
  description = "Source image from DockerHub"
}
