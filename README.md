

## Development
* Grants permission to the entrypoint.sh
    ```bash
    chmod +x project/entrypoint.sh
    ```
* Build & run docker-compose
    ```bash
    docker-compose up --build -d  
    ```
* Run tests
    ```bash
    docker-compose exec web python -m pytest
    ```  
 