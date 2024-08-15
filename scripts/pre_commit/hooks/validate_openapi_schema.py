#!/usr/bin/env python3
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
import json
import logging
import os
import pathlib
import subprocess
import sys
from typing import Any, MutableMapping

from fastapi.openapi.utils import get_openapi
from rich.console import Console

PROJECT_ROOT_PATH = str(pathlib.Path(__file__).parents[3])
OPEN_API_SCHEMA_PATH = "docs/openapi.json"
OPEN_API_SCHEMA_FULL_PATH = f"{PROJECT_ROOT_PATH}/{OPEN_API_SCHEMA_PATH}"
sys.path.append(PROJECT_ROOT_PATH)


log = logging.getLogger(__name__)


console = Console(color_system="standard", width=200)


def get_openapi_schema() -> MutableMapping[str, Any]:
    """Retrieves the OpenAPI schema of the current api."""
    from api.main import app, get_app_version

    if app.openapi_schema:
        return app.openapi_schema

    return get_openapi(
        title="ResumeBot REST API",
        version=get_app_version(),
        routes=app.routes
    )


def is_file_staged(filename: str) -> bool:
    """Checks if a file is staged for commit."""
    result = subprocess.run(['git', 'diff-index', '--cached', 'HEAD', filename], capture_output=True, text=True)
    return result.stdout.strip() == ""


def save_schema_to_file(filename: str, schema: MutableMapping[str, Any]) -> None:
    """Save OpenAPI schema to a file."""
    console.print("[yellow]Saving OpenAPI schema. Updating.[/]")
    with open(filename, "w") as schema_file:
        schema_file.write(json.dumps(schema))


def validate_openapi_schema() -> bool:
    """Ensures a valid OpenAPI schema."""
    schema = get_openapi_schema()

    if not os.path.exists(OPEN_API_SCHEMA_FULL_PATH):
        console.print(f"[red]The OpenAPI schema file '{OPEN_API_SCHEMA_PATH}' is missing. It will be generated.[/]")
        save_schema_to_file(filename=OPEN_API_SCHEMA_FULL_PATH, schema=schema)
        return False

    if not is_file_staged(OPEN_API_SCHEMA_FULL_PATH):
        console.print(f"[red]The OpenAPI schema file '{OPEN_API_SCHEMA_PATH}' contains unstages changes.[/]")
        return False

    with open(OPEN_API_SCHEMA_FULL_PATH, "r") as schema_file:
        source_schema = schema_file.read()

    generated_schema = json.dumps(schema)
    if source_schema == generated_schema:
        return True

    console.print(f"[red]Invalid OpenAPI schema  in the file '{OPEN_API_SCHEMA_PATH}'. It will be re-generated.[/]")
    save_schema_to_file(filename=OPEN_API_SCHEMA_FULL_PATH, schema=schema)
    return False


def main() -> int:
    if not validate_openapi_schema():
        console.print(
            f"[yellow]Please run `git add {OPEN_API_SCHEMA_FULL_PATH} && git commit --amend` for applying changes.[/]",
            style="bold"
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
