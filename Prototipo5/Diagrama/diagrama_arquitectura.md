```mermaid
graph LR

A[Client / View] -->|HTTP / JSON| B[Flask Server / Controller]

B --> C[DAO Layer]
C --> D[(MySQL)]

D --> C
C --> B
B --> A
