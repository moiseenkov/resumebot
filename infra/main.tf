#  Copyright (c) [2024] [Maksim Moiseenkov]
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

module "image_repository" {
  source        = "./repository"
  project_id    = var.project_id
  location      = var.location
  repository_id = "resume-bot-repository-api"
}

module "api_image" {
  source        = "./gcr_image"
  project_id    = var.project_id
  location      = var.location
  repository_id = module.image_repository.repository_id
  image         = var.api_image
}

module "api_instance" {
  source = "./cloud_run"
  name = "api"
  location = var.location
  image = module.api_image.uri
  cpu = "1"
  memory = "512Mi"
  health_url = "/health"
}
