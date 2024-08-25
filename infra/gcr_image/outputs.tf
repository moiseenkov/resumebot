output "uri" {
  value = data.google_artifact_registry_docker_image.gcr_image.self_link
}
