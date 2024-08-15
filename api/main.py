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
from fastapi import FastAPI

from api.routers import health


__version__ = "0.0.0"


def get_app_version() -> str:
    return __version__


app = FastAPI(swagger_ui_parameters={"docExpansion": "list"}, version=get_app_version())


app.include_router(health.router)
