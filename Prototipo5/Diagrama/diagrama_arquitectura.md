```mermaid
graph LR

subgraph CLIENTE
A[Frontend Web<br>HTML / CSS / JavaScript]
end

subgraph BACKEND
B[API REST Flask<br>Controllers]
C[Service Layer<br>Business Logic]
D[DAO Layer<br>Data Access]
end

subgraph DB
E[(MySQL Database)]
end

A <--> |HTTP / JSON| B
B <--> C
C <--> D
D <--> E
