resource "google_cloud_run_v2_service" "cloudrun-service" {
  name     = var.name
  location = var.location
  ingress  = "INGRESS_TRAFFIC_ALL"
  deletion_protection = false
  template {
    containers {
      image = var.image
      ports {
        container_port = 8080
      }
      resources {
        limits = {
          cpu    = var.cpu
          memory = var.memory
        }
      }
      liveness_probe {
        http_get {
          path = var.health_url
        }
        timeout_seconds   = 10
        period_seconds    = 60
        failure_threshold = 3
      }
    }
    scaling {
      min_instance_count = 1
      max_instance_count = 2
    }
  }
}

resource "google_cloud_run_v2_service_iam_binding" "binding" {
  project = google_cloud_run_v2_service.cloudrun-service.project
  location = google_cloud_run_v2_service.cloudrun-service.location
  name = google_cloud_run_v2_service.cloudrun-service.name
  role = "roles/run.invoker"
  members = [
    "allUsers", # TODO: Make more strict in the future
    ]
}