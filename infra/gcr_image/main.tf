module "docker_image" {
  source = "../docker_image"
  name   = var.image.name
  sha256 = var.image.sha256
}

resource "terraform_data" "copy_source_image" {
  input = var.image.sha256

  depends_on = [
    module.docker_image,
  ]

  provisioner "local-exec" {
    command = <<EOF
      docker tag ${module.docker_image.id} ${var.location}-docker.pkg.dev/${var.project_id}/${var.repository_id}/${var.image.name}:${var.image.tag}
      docker push ${var.location}-docker.pkg.dev/${var.project_id}/${var.repository_id}/${var.image.name}:${var.image.tag}
      echo ===================================================================================
      echo ${var.location}-docker.pkg.dev/${var.project_id}/${var.repository_id}/${module.docker_image.name}:${var.image.tag}
    EOF
  }
}

data "google_artifact_registry_docker_image" "gcr_image" {
  depends_on = [terraform_data.copy_source_image]

  project       = var.project_id
  location      = var.location
  repository_id = var.repository_id
  image_name    = "${var.image.name}@sha256:${var.image.sha256}"
}
