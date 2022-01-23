### Docker Flask Example
A very small micro-service architecture: Two simple web-app containers that communicate to each other through a docker network.

### Flask Validator
The validator's role is to serve as an orchestrator and gatekeeper, ensuring that the input into the system is clean and valid. 
It must: 
- Listen on exposed port 5000 for JSON input sent via an HTTP POST to "/definition", e.g. "http://localhost:5000/definition" 
- Validate the input JSON to ensure a word was provided. If the "word" parameter is null, return the invalid JSON input result. 
- Clean the input JSON to ensure the word passed to container 2 does not have any extra spaces, and is in a consistent format: 
 - Trim whitespace from the start and end of the word 
 - Convert the word to all lowercase 
- Send the "word" parameter to the processor (JSON) and return the response from the processor (Container 2). 

### Flask Processor
The processor's role is to listen to port 5000 and port 5050 within the docker network for requests to look up definitions. 
It must:
- Mount the host machine directory '.' to a docker volume
- Load the contents of dictionary.txt in the docker volume
- Listen on an endpoint/port you define to respond to definition requests:
 - Lookup the input word in the dictionary
 - Return the definition in the appropriate JSON format, or, if the word is not found
the word not found response (see errorresponses.json for exact response formats).