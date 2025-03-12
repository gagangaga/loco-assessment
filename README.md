# Simple Flask Application

This is a simple Flask web application that demonstrates basic web page rendering and a JSON API endpoint.

## Features

* **Root Route (`/`)**:
    * Displays the current date and time.
    * Displays a random number between 1 and 100.
    * Renders an HTML template (`index.html`).
* **API Endpoint (`/api/random`)**:
    * Returns a JSON response containing a random number (1-1000) and a timestamp.


## Prerequisites

* EKS cluster
* `kubectl` configured

## Deployment

1.  Clone: `git clone <repo>`
2.  Go to the deploy folder and run the below commands 
3.  Apply: `kubectl apply -f deployment.yaml`, `kubectl apply -f service.yaml` , `kubectl apply -f hpa.yaml`


