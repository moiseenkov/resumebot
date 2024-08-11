<!--
 Copyright (c) [2024] [Maksim Moiseenkov]

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
## Architecture 2

![Architecture](/docs/images/architecture.png)

The chatbot consists of three main components:
1. ChatBot server for interaction with user.
2. REST API for handling requests and providing the Chatbot with data.
3. MongoDB M0 Cluster for storing and serving resume data.

ChatBot and REST API are intended to be deployed in cloudRun instances under free tier so no expenditure is expected.
